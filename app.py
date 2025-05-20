import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd
import numpy as np
import plotly.express as px
import requests
from io import BytesIO

# Set page config
st.set_page_config(
    page_title="Enhanced Rock Weathering (ERW) Analysis",
    page_icon="🌍",
    layout="wide"
)

# Title and description
st.title("Enhanced Rock Weathering (ERW) Analysis Dashboard")
st.markdown("""
This interactive dashboard analyzes the potential of Enhanced Rock Weathering (ERW) across different regions,
evaluating decarbonization performance and economic viability under various carbon pricing scenarios.
""")

# Sidebar
st.sidebar.header("Analysis Parameters")
carbon_price = st.sidebar.slider("Carbon Price ($/ton CO2)", 0, 200, 50)
time_horizon = st.sidebar.selectbox("Time Horizon", ["2025", "2030", "2035", "2040"])

# Create tabs
tab1, tab2, tab3, tab4, tab6 = st.tabs(["Global Map", "Regional Analysis", "Economic Assessment", "Madeira Basalt Case Study", "Azores Basalt Case Study"])

with tab1:
    st.header("Global ERW Potential Map")
    
    # Create a map centered at a global view
    m = folium.Map(location=[20, 0], zoom_start=2)
    
    # Define regions with high ERW potential
    regions = {
        "Brazil": {"lat": -10, "lon": -55, "potential": "High"},
        "India": {"lat": 20, "lon": 78, "potential": "High"},
        "Southeast Asia": {"lat": 5, "lon": 100, "potential": "High"},
        "China": {"lat": 35, "lon": 105, "potential": "High"},
        "USA": {"lat": 40, "lon": -95, "potential": "Medium"},
        "Europe": {"lat": 51, "lon": 0, "potential": "Medium"},
        "Sub-Saharan Africa": {"lat": -2, "lon": 30, "potential": "High"}
    }
    
    # Add markers for each region
    for region, data in regions.items():
        folium.Marker(
            location=[data["lat"], data["lon"]],
            popup=f"{region}: {data['potential']} ERW Potential",
            icon=folium.Icon(color='green' if data["potential"] == "High" else 'orange')
        ).add_to(m)
    
    # Display the map
    folium_static(m, width=1000, height=600)

with tab2:
    st.header("Regional Analysis")
    
    # Create sample data for regional analysis
    regions_data = {
        "Region": ["Brazil", "India", "Southeast Asia", "China", "USA", "Europe", "Sub-Saharan Africa"],
        "Agricultural Land (Mha)": [238, 180, 120, 500, 400, 280, 800],
        "CO2 Sequestration Potential (Mt/year)": [120, 90, 60, 250, 200, 140, 400],
        "Economic Viability Score": [0.85, 0.75, 0.80, 0.90, 0.70, 0.65, 0.95]
    }
    
    df = pd.DataFrame(regions_data)
    
    # Create interactive bar chart
    fig = px.bar(df, 
                 x="Region", 
                 y="CO2 Sequestration Potential (Mt/year)",
                 title="CO2 Sequestration Potential by Region",
                 color="Economic Viability Score",
                 color_continuous_scale="Viridis")
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Display detailed metrics
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Top Regions by Potential")
        st.dataframe(df.sort_values("CO2 Sequestration Potential (Mt/year)", ascending=False))
    
    with col2:
        st.subheader("Economic Viability")
        st.dataframe(df.sort_values("Economic Viability Score", ascending=False))

with tab3:
    st.header("Economic Assessment")
    
    # Create economic analysis visualization
    carbon_prices = np.linspace(0, 200, 20)
    economic_viability = {
        "Brazil": [0.3, 0.5, 0.7, 0.85, 0.95],
        "India": [0.2, 0.4, 0.6, 0.75, 0.9],
        "Southeast Asia": [0.25, 0.45, 0.65, 0.8, 0.92],
        "China": [0.35, 0.55, 0.75, 0.9, 0.98],
        "USA": [0.15, 0.35, 0.55, 0.7, 0.85],
        "Europe": [0.1, 0.3, 0.5, 0.65, 0.8],
        "Sub-Saharan Africa": [0.4, 0.6, 0.8, 0.95, 0.99]
    }
    
    # Create economic viability plot
    fig = px.line(
        x=carbon_prices,
        y=[economic_viability[region] for region in regions_data["Region"]],
        title="Economic Viability vs Carbon Price",
        labels={"x": "Carbon Price ($/ton CO2)", "y": "Economic Viability Score"},
        names=regions_data["Region"]
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Display ROI calculations
    st.subheader("Return on Investment (ROI) Analysis")
    roi_data = {
        "Region": regions_data["Region"],
        "Initial Investment ($/ha)": [500, 450, 400, 550, 600, 650, 350],
        "Annual Revenue ($/ha)": [200, 180, 160, 220, 240, 260, 150],
        "Payback Period (years)": [2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.3]
    }
    
    st.dataframe(pd.DataFrame(roi_data))

with tab4:
    st.header("Basalt Availability: Madeira Island (Portugal)")
    st.markdown("""
    Madeira is a volcanic island in the North Atlantic, part of Portugal, and is primarily composed of basaltic rocks. This tool estimates the available basalt mass based on the island's area, average depth, and basalt density.
    """)

    # Madeira's approximate area and coordinates
    madeira_area_km2 = 740  # km²
    madeira_coords = {"lat": 32.7607, "lon": -16.9595}

    st.map(pd.DataFrame([{"lat": madeira_coords["lat"], "lon": madeira_coords["lon"]}], columns=["lat", "lon"]))

    st.write(f"**Madeira Island Area:** {madeira_area_km2} km²")

    # User input for depth and density
    depth = st.number_input("Average basalt depth (m)", min_value=0.1, value=10.0)
    density = st.number_input("Basalt density (kg/m³)", min_value=1000, max_value=4000, value=2900)

    # Calculation
    volume_m3 = madeira_area_km2 * 1e6 * depth
    mass_kg = volume_m3 * density
    mass_Mt = mass_kg / 1e9

    st.success(f"Estimated Basalt Mass in Madeira: {mass_Mt:,.2f} Megatonnes (Mt)")

    st.markdown("""
    *Data source: [Wikipedia - Madeira](https://en.wikipedia.org/wiki/Madeira), geological literature.*
    """)

with tab6:
    st.header("Basalt Availability: Azores Islands (Portugal)")
    st.markdown("""
    The Azores are a volcanic archipelago in the North Atlantic, part of Portugal, and are primarily composed of basaltic rocks. This tool estimates the available basalt mass based on the islands' area, average depth, and basalt density.
    """)

    # Azores' approximate area and coordinates (main island São Miguel as example)
    azores_area_km2 = 2322  # km² (total for all islands)
    azores_coords = {"lat": 37.7800, "lon": -25.4970}

    st.map(pd.DataFrame([{"lat": azores_coords["lat"], "lon": azores_coords["lon"]}], columns=["lat", "lon"]))

    st.write(f"**Azores Islands Area:** {azores_area_km2} km²")

    # User input for depth and density
    depth = st.number_input("Average basalt depth (m)", min_value=0.1, value=10.0, key="azores_depth")
    density = st.number_input("Basalt density (kg/m³)", min_value=1000, max_value=4000, value=2900, key="azores_density")

    # Calculation
    volume_m3 = azores_area_km2 * 1e6 * depth
    mass_kg = volume_m3 * density
    mass_Mt = mass_kg / 1e9

    st.success(f"Estimated Basalt Mass in Azores: {mass_Mt:,.2f} Megatonnes (Mt)")

    st.markdown("""
    *Data source: [Wikipedia - Azores](https://en.wikipedia.org/wiki/Azores), geological literature.*
    """)

# Footer
st.markdown("---")
st.markdown("""
### About this Dashboard
This dashboard provides an interactive analysis of Enhanced Rock Weathering (ERW) potential across different regions.
The data is based on publicly available datasets and research from the PEESE group.
""") 