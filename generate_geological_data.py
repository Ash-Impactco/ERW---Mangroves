import os
import json
import pandas as pd
from pathlib import Path

def create_directory_structure():
    """Create the necessary directory structure"""
    base_dir = Path("maps")
    folders = ["basalt", "olivine", "serpentine", "volcanic", "mangrove"]
    
    for folder in folders:
        folder_path = base_dir / folder
        folder_path.mkdir(parents=True, exist_ok=True)
        
        # Create data subdirectories
        (folder_path / "csv").mkdir(exist_ok=True)
        (folder_path / "geojson").mkdir(exist_ok=True)

def create_geological_data():
    """Create sample data for each geological feature with validated coordinates"""
    base_data = {
        "basalt": {
            "name": "Basalt Deposits",
            "type": "basalt",
            "coordinates": [
                [-122.4194, 37.7749],  # San Francisco area
                [103.8198, 1.3521],   # Singapore area
                [-117.1611, 32.7157], # San Diego area
                [139.7692, 35.6895],  # Tokyo area
                [-74.0060, 40.7128]   # New York City
            ]
        },
        "olivine": {
            "name": "Olivine Deposits",
            "type": "olivine",
            "coordinates": [
                [151.2093, -33.8688],  # Sydney area
                [126.9780, 37.5665],   # Seoul area
                [114.1772, 22.2783],   # Hong Kong
                [139.6917, 35.6895],   # Tokyo area
                [106.8456, -6.2088]    # Jakarta
            ]
        },
        "serpentine": {
            "name": "Serpentine Deposits",
            "type": "serpentine",
            "coordinates": [
                [-74.0060, 40.7128],  # New York area
                [139.6917, 35.6895],   # Tokyo area
                [-118.2437, 34.0522],  # Los Angeles
                [103.8198, 1.3521],    # Singapore
                [149.1300, -35.2809]   # Canberra
            ]
        },
        "volcanic": {
            "name": "Volcanoes",
            "type": "volcano",
            "coordinates": [
                [-155.282, 19.421],    # Kilauea, Hawaii
                [140.75, 35.89],       # Fuji, Japan
                [-114.41, 44.42],      # Yellowstone, USA
                [100.49, 6.16],        # Mount Merapi, Indonesia
                [-78.15, -1.83],       # Cotopaxi, Ecuador
                [-121.1752, 45.3742],  # Mount Hood, Oregon
                [138.1644, -19.4421]   # Uluru/Ayers Rock, Australia
            ]
        }
    }
    
    # Validate coordinates
    for feature, data in base_data.items():
        valid_coords = []
        for coord in data["coordinates"]:
            if isinstance(coord, list) and len(coord) == 2:
                lon, lat = coord
                if isinstance(lon, (int, float)) and isinstance(lat, (int, float)):
                    if -180 <= lon <= 180 and -90 <= lat <= 90:
                        valid_coords.append(coord)
        base_data[feature]["coordinates"] = valid_coords
    
    return base_data

def create_mangrove_data():
    """Create mangrove data from Global Mangrove Watch"""
    mangrove_data = {
        "name": "Mangrove Areas",
        "type": "mangrove",
        "coordinates": []
    }
    
    # Add major mangrove locations
    mangrove_locations = [
        [-97.1208, 25.7673],  # Texas, USA
        [103.8198, 1.3521],  # Singapore
        [120.9842, 14.5995], # Manila, Philippines
        [131.0445, -12.4634], # Darwin, Australia
        [-80.1918, 25.7617]  # Miami, USA
    ]
    
    mangrove_data["coordinates"] = mangrove_locations
    return mangrove_data

def save_csv_data(data, folder_name):
    """Save data as CSV"""
    df = pd.DataFrame(data["coordinates"], columns=["longitude", "latitude"])
    df["type"] = data["type"]
    df["name"] = data["name"]
    
    csv_path = f"maps/{folder_name}/csv/{folder_name}_data.csv"
    df.to_csv(csv_path, index=False)

def save_geojson_data(data, folder_name):
    """Save data as GeoJSON"""
    geojson = {
        "type": "FeatureCollection",
        "features": []
    }
    
    for coord in data["coordinates"]:
        feature = {
            "type": "Feature",
            "properties": {
                "name": data["name"],
                "type": data["type"]
            },
            "geometry": {
                "type": "Point",
                "coordinates": coord
            }
        }
        geojson["features"].append(feature)
    
    geojson_path = f"maps/{folder_name}/geojson/{folder_name}_data.geojson"
    with open(geojson_path, 'w') as f:
        json.dump(geojson, f, indent=2)

def main():
    # Create directory structure
    create_directory_structure()
    
    # Create geological data
    geological_data = create_geological_data()
    
    # Save data for each geological feature
    for feature, data in geological_data.items():
        save_csv_data(data, feature)
        save_geojson_data(data, feature)
    
    # Create and save mangrove data
    mangrove_data = create_mangrove_data()
    save_csv_data(mangrove_data, "mangrove")
    save_geojson_data(mangrove_data, "mangrove")

if __name__ == "__main__":
    main()
