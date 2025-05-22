import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import requests
import json

def load_volcanic_data():
    """Load volcanic data from ArcGIS REST API"""
    try:
        # ArcGIS REST API endpoint for volcanic data
        url = "https://services2.arcgis.com/11XBiaBYA9Ep0yNJ/arcgis/rest/services/Global_Volcanoes/FeatureServer/0/query"
        
        # Parameters for the query
        params = {
            'where': '1=1',
            'outFields': '*',
            'geometryType': 'esriGeometryPoint',
            'spatialRel': 'esriSpatialRelIntersects',
            'outSR': '4326',
            'f': 'json'
        }
        
        # Make the request
        response = requests.get(url, params=params)
        data = response.json()
        
        # Convert to GeoDataFrame
        features = data['features']
        points = []
        properties = []
        
        for feature in features:
            coords = feature['geometry']['coordinates']
            points.append(Point(coords[0], coords[1]))
            properties.append(feature['attributes'])
        
        gdf = gpd.GeoDataFrame(properties, geometry=points, crs="EPSG:4326")
        return gdf
    
    except Exception as e:
        st.error(f"Error loading volcanic data: {str(e)}")
        return None

def create_volcanic_map(gdf):
    """Create an interactive map of volcanic areas"""
    # Create a base map centered on the world
    m = folium.Map(location=[0, 0], zoom_start=2)
    
    # Add volcanic points to the map
    for idx, row in gdf.iterrows():
        folium.CircleMarker(
            location=[row.geometry.y, row.geometry.x],
            radius=5,
            popup=f"Volcano: {row.get('NAME', 'Unknown')}<br>"
                  f"Type: {row.get('TYPE', 'Unknown')}<br>"
                  f"Elevation: {row.get('ELEV', 'Unknown')}m",
            color='red',
            fill=True,
            fill_color='red'
        ).add_to(m)
    
    return m

def analyze_volcanic_regions(gdf):
    """Analyze volcanic regions and their characteristics"""
    if gdf is None:
        return
    
    st.subheader("Volcanic Regions Analysis")
    
    # Basic statistics
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Total Volcanoes", len(gdf))
        st.metric("Unique Types", gdf['TYPE'].nunique())
    
    with col2:
        avg_elevation = gdf['ELEV'].mean()
        st.metric("Average Elevation", f"{avg_elevation:.1f}m")
    
    # Distribution by type
    st.subheader("Distribution by Volcano Type")
    type_counts = gdf['TYPE'].value_counts()
    st.bar_chart(type_counts)
    
    # Elevation distribution
    st.subheader("Elevation Distribution")
    st.line_chart(gdf['ELEV'].value_counts().sort_index())

def get_arcgis_data(service_name):
    base_url = "https://services2.arcgis.com/11XBiaBYA9Ep0yNJ/arcgis/rest/services"
    url = f"{base_url}/{service_name}/FeatureServer/0/query"
    
    params = {
        'where': '1=1',
        'outFields': '*',
        'geometryType': 'esriGeometryPolygon',
        'spatialRel': 'esriSpatialRelIntersects',
        'outSR': '4326',
        'f': 'json'
    }
    
    response = requests.get(url, params=params)
    return response.json()

def get_volcanic_data(query_params=None):
    base_url = "https://services2.arcgis.com/11XBiaBYA9Ep0yNJ/arcgis/rest/services/Global_Volcanoes/FeatureServer/0/query"
    
    default_params = {
        'where': '1=1',
        'outFields': '*',
        'geometryType': 'esriGeometryPoint',
        'spatialRel': 'esriSpatialRelIntersects',
        'outSR': '4326',
        'f': 'json'
    }
    
    if query_params:
        default_params.update(query_params)
    
    response = requests.get(base_url, params=default_params)
    return response.json()

def main():
    st.title("Global Volcanic Areas Analysis")
    
    # Load data
    with st.spinner("Loading volcanic data..."):
        gdf = load_volcanic_data()
    
    if gdf is not None:
        # Create and display map
        st.subheader("Interactive Volcanic Map")
        m = create_volcanic_map(gdf)
        folium_static(m)
        
        # Analysis section
        analyze_volcanic_regions(gdf)
        
        # Raw data view
        if st.checkbox("Show Raw Data"):
            st.dataframe(gdf.drop(columns=['geometry']))

if __name__ == "__main__":
    main() 