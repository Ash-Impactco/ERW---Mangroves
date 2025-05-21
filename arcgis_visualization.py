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

def load_climate_data():
    """Load climate data from ArcGIS REST API"""
    try:
        url = "https://services2.arcgis.com/11XBiaBYA9Ep0yNJ/arcgis/rest/services/Global_Climate/FeatureServer/0/query"
        
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
        st.error(f"Error loading climate data: {str(e)}")
        return None

def create_geological_map(gdf, climate_gdf=None):
    """Create an interactive map of geological features with climate overlay"""
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
                f"Formation Process: {row.get('FORMATION', 'N/A')}"
            )
        ).add_to(m)
    
    # Add climate data if available
    if climate_gdf is not None:
        climate_layer = folium.FeatureGroup(name='Climate Zones')
        for idx, row in climate_gdf.iterrows():
            folium.GeoJson(
                row.geometry.__geo_interface__,
                style_function=lambda x: {
                    'fillColor': '#3186cc',
                    'color': 'black',
                    'weight': 1,
                    'fillOpacity': 0.3
                },
                popup=folium.Popup(
                    f"Climate Zone: {row['ZONE']}<br>"
                    f"Average Temperature: {row.get('TEMP', 'N/A')}°C<br>"
                    f"Annual Rainfall: {row.get('RAINFALL', 'N/A')}mm"
                )
            ).add_to(climate_layer)
        climate_layer.add_to(m)
    
    # Add layer control
    folium.LayerControl().add_to(m)
    color_map.add_to(m)
    return m

def analyze_geological_features(gdf, climate_gdf=None):
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
        if climate_gdf is not None:
            st.metric("Climate Zones", climate_gdf['ZONE'].nunique())
            st.metric("Average Temperature", f"{climate_gdf['TEMP'].mean():.1f}°C")
    
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
    
    # Climate correlation analysis
    if climate_gdf is not None:
        st.subheader("Climate Correlation Analysis")
        climate_stats = climate_gdf.groupby('ZONE').agg({
            'TEMP': ['mean', 'std'],
            'RAINFALL': ['mean', 'std']
        }).round(2)
        st.dataframe(climate_stats)

def main():
    st.title("Global Geological Features Analysis")
    
    # Add timestamp
    st.sidebar.write(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Load data
    with st.spinner("Loading geological data..."):
        gdf = load_geological_data()
    
    with st.spinner("Loading climate data..."):
        climate_gdf = load_climate_data()
    
    if gdf is not None:
        # Create and display map
        st.subheader("Interactive Geological Map")
        m = create_geological_map(gdf, climate_gdf)
        folium_static(m)
        
        # Analysis section
        analyze_geological_features(gdf, climate_gdf)
        
        # Raw data view
        if st.checkbox("Show Raw Data"):
            tab1, tab2 = st.tabs(["Geological Data", "Climate Data"])
            with tab1:
                st.dataframe(gdf.drop(columns=['geometry']))
            with tab2:
                if climate_gdf is not None:
                    st.dataframe(climate_gdf.drop(columns=['geometry']))

if __name__ == "__main__":
    main() 