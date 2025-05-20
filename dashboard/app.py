import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd
import json
import os

data_path = os.path.join(os.path.dirname(__file__), '../data/erw_projects.csv')
geojson_path = os.path.join(os.path.dirname(__file__), '../data/erw_regions.geojson')

st.title("Global Enhanced Rock Weathering (ERW) & Carbon Removal Map")

# Load sample ERW project data
df = pd.read_csv(data_path)
with open(geojson_path) as f:
    geojson = json.load(f)

# Map
m = folium.Map(location=[20, 0], zoom_start=2)
for _, row in df.iterrows():
    folium.Marker(
        [row["latitude"], row["longitude"]],
        popup=f"{row['project_name']}<br>CO₂ Removal: {row['co2_removal_mt']} Mt"
    ).add_to(m)
folium_static(m, width=900, height=500)

st.header("Project Table")
st.dataframe(df) 