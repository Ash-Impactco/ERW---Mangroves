import arcgis
from arcgis.gis import GIS
from arcgis.features import FeatureLayer
import json
import os

def create_map():
    # Initialize ArcGIS Online
    gis = GIS()
    
    # Create a new map
    map_widget = gis.map()
    
    # Set initial extent to show global view
    map_widget.extent = {
        "xmin": -180,
        "ymin": -90,
        "xmax": 180,
        "ymax": 90,
        "spatialReference": {"wkid": 4326}
    }
    
    return map_widget

def add_geological_layers(map_widget):
    # Read the geological features from JSON
    with open('data/geological_features.json', 'r') as f:
        geojson_data = json.load(f)
    
    # Create feature layers for each type
    basalt_layer = FeatureLayer.from_geojson(geojson_data, layer_type='basalt')
    olivine_layer = FeatureLayer.from_geojson(geojson_data, layer_type='olivine')
    serpentine_layer = FeatureLayer.from_geojson(geojson_data, layer_type='serpentine')
    volcano_layer = FeatureLayer.from_geojson(geojson_data, layer_type='volcano')
    
    # Add layers to map with custom styles
    map_widget.add_layer(basalt_layer, {
        "renderer": "simple",
        "symbol": {
            "color": [100, 100, 100, 0.5],
            "style": "esriSFSSolid",
            "type": "esriSFS"
        },
        "title": "Basalt Deposits"
    })
    
    map_widget.add_layer(olivine_layer, {
        "renderer": "simple",
        "symbol": {
            "color": [150, 200, 150, 0.5],
            "style": "esriSFSSolid",
            "type": "esriSFS"
        },
        "title": "Olivine Deposits"
    })
    
    map_widget.add_layer(serpentine_layer, {
        "renderer": "simple",
        "symbol": {
            "color": [200, 200, 100, 0.5],
            "style": "esriSFSSolid",
            "type": "esriSFS"
        },
        "title": "Serpentine Deposits"
    })
    
    map_widget.add_layer(volcano_layer, {
        "renderer": "simple",
        "symbol": {
            "color": [255, 0, 0, 1],
            "size": 8,
            "style": "esriSMSquare",
            "type": "esriSMS"
        },
        "title": "Volcanoes"
    })
    
    return map_widget

def add_mangrove_layer(map_widget):
    # Add mangrove layer from Global Mangrove Watch
    mangrove_url = "https://services.arcgis.com/P3nPE77H505EJZ7Q/arcgis/rest/services/Global_Mangrove_Watch/FeatureServer/0"
    mangrove_layer = FeatureLayer(mangrove_url)
    
    map_widget.add_layer(mangrove_layer, {
        "renderer": "simple",
        "symbol": {
            "color": [0, 150, 0, 0.5],
            "style": "esriSFSSolid",
            "type": "esriSFS"
        },
        "title": "Mangrove Areas"
    })
    
    return map_widget

def main():
    # Create map
    map_widget = create_map()
    
    # Add all layers
    map_widget = add_geological_layers(map_widget)
    map_widget = add_mangrove_layer(map_widget)
    
    # Display the map
    map_widget.display()

if __name__ == "__main__":
    main()
