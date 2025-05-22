import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, Polygon
import requests
import json
import branca.colormap as cm
import numpy as np
from datetime import datetime

def load_geological_data():
    """Load geological data from ArcGIS REST API"""
    try:
        # ArcGIS REST API endpoint for geological data
        url = "https://services2.arcgis.com/11XBiaBYA9Ep0yNJ/arcgis/rest/services/Global_Geology/FeatureServer/0/query"
        
        params = {
            'where': '1=1',
            'outFields': '*',
            'geometryType': 'esriGeometryPolygon',
            'spatialRel': 'esriSpatialRelIntersects',
            'outSR': '4326',
            'f': 'json'
        }
        
        response = requests.get(url, params=params)
        data = response.json()
        
        features = data['features']
        polygons = []
        properties = []
        
        for feature in features:
            coords = feature['geometry']['rings'][0]
            polygon = Polygon(coords)
            polygons.append(polygon)
            properties.append(feature['attributes'])
        
        gdf = gpd.GeoDataFrame(properties, geometry=polygons, crs="EPSG:4326")
        return gdf
    
    except Exception as e:
        st.error(f"Error loading geological data: {str(e)}")
        return None

def load_soil_data():
    """Load soil data from ArcGIS REST API"""
    try:
        url = "https://services2.arcgis.com/11XBiaBYA9Ep0yNJ/arcgis/rest/services/Global_Soil/FeatureServer/0/query"
        
        params = {
            'where': '1=1',
            'outFields': '*',
            'geometryType': 'esriGeometryPolygon',
            'spatialRel': 'esriSpatialRelIntersects',
            'outSR': '4326',
            'f': 'json'
        }
        
        response = requests.get(url, params=params)
        data = response.json()
        
        features = data['features']
        polygons = []
        properties = []
        
        for feature in features:
            coords = feature['geometry']['rings'][0]
            polygon = Polygon(coords)
            polygons.append(polygon)
            properties.append(feature['attributes'])
        
        gdf = gpd.GeoDataFrame(properties, geometry=polygons, crs="EPSG:4326")
        return gdf
    
    except Exception as e:
        st.error(f"Error loading soil data: {str(e)}")
        return None

def load_land_use_data():
    """Load land use data from ArcGIS REST API"""
    try:
        url = "https://services2.arcgis.com/11XBiaBYA9Ep0yNJ/arcgis/rest/services/Global_Land_Use/FeatureServer/0/query"
        
        params = {
            'where': '1=1',
            'outFields': '*',
            'geometryType': 'esriGeometryPolygon',
            'spatialRel': 'esriSpatialRelIntersects',
            'outSR': '4326',
            'f': 'json'
        }
        
        response = requests.get(url, params=params)
        data = response.json()
        
        features = data['features']
        polygons = []
        properties = []
        
        for feature in features:
            coords = feature['geometry']['rings'][0]
            polygon = Polygon(coords)
            polygons.append(polygon)
            properties.append(feature['attributes'])
        
        gdf = gpd.GeoDataFrame(properties, geometry=polygons, crs="EPSG:4326")
        return gdf
    
    except Exception as e:
        st.error(f"Error loading land use data: {str(e)}")
        return None

def create_geological_map(gdf, soil_gdf=None, land_use_gdf=None):
    """Create an interactive map of geological features with soil and land use overlays"""
    m = folium.Map(location=[0, 0], zoom_start=2)
    
    # Create a color map for geological ages
    unique_ages = gdf['AGE'].unique()
    color_map = cm.LinearColormap(
        colors=['#fee8c8', '#fdbb84', '#e34a33', '#b30000'],
        vmin=0,
        vmax=len(unique_ages),
        caption='Geological Age'
    )
    
    # Add geological polygons to the map
    for idx, row in gdf.iterrows():
        age_index = list(unique_ages).index(row['AGE'])
        color = color_map(age_index)
        
        folium.GeoJson(
            row.geometry.__geo_interface__,
            style_function=lambda x, color=color: {
                'fillColor': color,
                'color': 'black',
                'weight': 1,
                'fillOpacity': 0.7
            },
            popup=folium.Popup(
                f"Age: {row['AGE']}<br>"
                f"Type: {row['TYPE']}<br>"
                f"Description: {row['DESCRIPTION']}<br>"
                f"Mineral Composition: {row.get('MINERALS', 'N/A')}<br>"
                f"Formation Process: {row.get('FORMATION', 'N/A')}<br>"
                f"Rock Type: {row.get('ROCK_TYPE', 'N/A')}<br>"
                f"Chemical Composition: {row.get('CHEMICAL_COMP', 'N/A')}"
            )
        ).add_to(m)
    
    # Add soil data if available
    if soil_gdf is not None:
        soil_layer = folium.FeatureGroup(name='Soil Types')
        for idx, row in soil_gdf.iterrows():
            folium.GeoJson(
                row.geometry.__geo_interface__,
                style_function=lambda x: {
                    'fillColor': '#8c510a',
                    'color': 'black',
                    'weight': 1,
                    'fillOpacity': 0.3
                },
                popup=folium.Popup(
                    f"Soil Type: {row['TYPE']}<br>"
                    f"pH Level: {row.get('PH', 'N/A')}<br>"
                    f"Organic Matter: {row.get('ORGANIC_MATTER', 'N/A')}%<br>"
                    f"Texture: {row.get('TEXTURE', 'N/A')}<br>"
                    f"Depth: {row.get('DEPTH', 'N/A')}cm"
                )
            ).add_to(soil_layer)
        soil_layer.add_to(m)
    
    # Add land use data if available
    if land_use_gdf is not None:
        land_use_layer = folium.FeatureGroup(name='Land Use')
        for idx, row in land_use_gdf.iterrows():
            folium.GeoJson(
                row.geometry.__geo_interface__,
                style_function=lambda x: {
                    'fillColor': '#31a354',
                    'color': 'black',
                    'weight': 1,
                    'fillOpacity': 0.3
                },
                popup=folium.Popup(
                    f"Land Use: {row['TYPE']}<br>"
                    f"Coverage: {row.get('COVERAGE', 'N/A')}%<br>"
                    f"Management: {row.get('MANAGEMENT', 'N/A')}<br>"
                    f"Intensity: {row.get('INTENSITY', 'N/A')}"
                )
            ).add_to(land_use_layer)
        land_use_layer.add_to(m)
    
    # Add layer control
    folium.LayerControl().add_to(m)
    color_map.add_to(m)
    return m

def analyze_geological_features(gdf, soil_gdf=None, land_use_gdf=None):
    """Analyze geological features and their characteristics"""
    if gdf is None:
        return
    
    st.subheader("Geological Features Analysis")
    
    # Basic statistics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Geological Units", len(gdf))
        st.metric("Unique Ages", gdf['AGE'].nunique())
    
    with col2:
        st.metric("Unique Types", gdf['TYPE'].nunique())
        if 'MINERALS' in gdf.columns:
            st.metric("Mineral Types", gdf['MINERALS'].nunique())
    
    with col3:
        if soil_gdf is not None:
            st.metric("Soil Types", soil_gdf['TYPE'].nunique())
        if land_use_gdf is not None:
            st.metric("Land Use Types", land_use_gdf['TYPE'].nunique())
    
    # Distribution by age
    st.subheader("Distribution by Geological Age")
    age_counts = gdf['AGE'].value_counts()
    st.bar_chart(age_counts)
    
    # Distribution by type
    st.subheader("Distribution by Geological Type")
    type_counts = gdf['TYPE'].value_counts()
    st.bar_chart(type_counts)
    
    # Mineral composition analysis
    if 'MINERALS' in gdf.columns:
        st.subheader("Mineral Composition Analysis")
        mineral_counts = gdf['MINERALS'].value_counts()
        st.bar_chart(mineral_counts)
    
    # Soil analysis
    if soil_gdf is not None:
        st.subheader("Soil Analysis")
        soil_stats = soil_gdf.groupby('TYPE').agg({
            'PH': ['mean', 'std'],
            'ORGANIC_MATTER': ['mean', 'std'],
            'DEPTH': ['mean', 'std']
        }).round(2)
        st.dataframe(soil_stats)
    
    # Land use analysis
    if land_use_gdf is not None:
        st.subheader("Land Use Analysis")
        land_use_counts = land_use_gdf['TYPE'].value_counts()
        st.bar_chart(land_use_counts)

def main():
    st.title("Global Geological Features Analysis")
    
    # Add timestamp
    st.sidebar.write(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Load data
    with st.spinner("Loading geological data..."):
        gdf = load_geological_data()
    
    with st.spinner("Loading soil data..."):
        soil_gdf = load_soil_data()
    
    with st.spinner("Loading land use data..."):
        land_use_gdf = load_land_use_data()
    
    if gdf is not None:
        # Create and display map
        st.subheader("Interactive Geological Map")
        m = create_geological_map(gdf, soil_gdf, land_use_gdf)
        folium_static(m)
        
        # Analysis section
        analyze_geological_features(gdf, soil_gdf, land_use_gdf)
        
        # Raw data view
        if st.checkbox("Show Raw Data"):
            tab1, tab2, tab3 = st.tabs(["Geological Data", "Soil Data", "Land Use Data"])
            with tab1:
                st.dataframe(gdf.drop(columns=['geometry']))
            with tab2:
                if soil_gdf is not None:
                    st.dataframe(soil_gdf.drop(columns=['geometry']))
            with tab3:
                if land_use_gdf is not None:
                    st.dataframe(land_use_gdf.drop(columns=['geometry']))

if __name__ == "__main__":
    main() 