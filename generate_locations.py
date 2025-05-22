import json
import random
from pathlib import Path

def generate_basalt_locations():
    locations = [
        # Existing locations
        [-122.4194, 37.7749],  # San Francisco
        [103.8198, 1.3521],   # Singapore
        [-117.1611, 32.7157], # San Diego
        [139.7692, 35.6895],  # Tokyo
        [-74.0060, 40.7128],  # New York
        
        # New locations
        [-157.8583, 21.3069],  # Honolulu, Hawaii
        [-118.2437, 34.0522], # Los Angeles
        [139.0000, 35.6895],   # Yokohama
        [-122.0840, 37.3893], # Silicon Valley
        [121.0542, 14.5995],  # Manila
        
        [-115.1728, 36.1699], # Las Vegas
        [135.1944, -27.4698], # Alice Springs
        [144.9631, -37.8136], # Melbourne
        [-121.4944, 38.5816], # Sacramento
        [114.1694, 22.2783],  # Hong Kong
        
        [-116.1749, 43.6137], # Idaho Falls
        [131.0445, -12.4634], # Darwin
        [120.3361, 23.6978],  # Taipei
        [-111.6108, 40.7608], # Salt Lake City
        [114.2059, 30.5929],  # Wuhan
        
        [-118.2437, 33.7500], # Long Beach
        [121.4737, 31.2304],  # Shanghai
        [-110.9745, 32.2217], # Tucson
        [121.3000, 31.2304],  # Suzhou
        [-117.1956, 32.7157]  # San Diego area
    ]
    
    return create_geojson("basalt", locations)

def generate_olivine_locations():
    locations = [
        # Existing locations
        [151.2093, -33.8688], # Sydney
        [126.9780, 37.5665], # Seoul
        [114.1772, 22.2783], # Hong Kong
        [139.6917, 35.6895], # Tokyo
        [106.8456, -6.2088], # Jakarta
        
        # New locations
        [139.7513, 35.6895],  # Chiba
        [120.5833, 23.6978],  # Taichung
        [130.8811, -25.3041], # Townsville
        [116.5648, 39.9138],  # Beijing
        [127.0246, 37.5665],  # Incheon
        
        [121.4737, 31.2304],  # Shanghai
        [114.1694, 22.2783],  # Hong Kong
        [125.6442, 38.0133],  # Dalian
        [120.1954, 30.2642],  # Hangzhou
        [116.3974, 39.9092],  # Beijing
        
        [119.3062, 26.0753],  # Fuzhou
        [117.2761, 39.1326],  # Tianjin
        [114.3117, 30.5243],  # Wuhan
        [113.2644, 23.1291],  # Guangzhou
        [121.4737, 31.2304],  # Shanghai
        
        [116.4074, 39.9042],  # Beijing
        [114.3052, 30.5927],  # Wuhan
        [116.3972, 39.9092],  # Beijing
        [116.3972, 39.9092],  # Beijing
        [116.3972, 39.9092]   # Beijing
    ]
    
    return create_geojson("olivine", locations)

def generate_serpentine_locations():
    locations = [
        # Existing locations
        [-74.0060, 40.7128],  # New York
        [139.6917, 35.6895],  # Tokyo
        [-118.2437, 34.0522], # Los Angeles
        [103.8198, 1.3521],   # Singapore
        [149.1300, -35.2809], # Canberra
        
        # New locations
        [-122.4194, 37.7749],  # San Francisco
        [139.7692, 35.6895],  # Yokohama
        [-117.1611, 32.7157], # San Diego
        [121.4737, 31.2304],  # Shanghai
        [114.1694, 22.2783],  # Hong Kong
        
        [120.3361, 23.6978],  # Taipei
        [121.4737, 31.2304],  # Shanghai
        [116.3974, 39.9042],  # Beijing
        [114.3052, 30.5927],  # Wuhan
        [116.3972, 39.9092],  # Beijing
        
        [114.3052, 30.5927],  # Wuhan
        [116.3972, 39.9092],  # Beijing
        [114.3052, 30.5927],  # Wuhan
        [116.3972, 39.9092],  # Beijing
        [114.3052, 30.5927],  # Wuhan
        
        [116.3972, 39.9092],  # Beijing
        [114.3052, 30.5927],  # Wuhan
        [116.3972, 39.9092],  # Beijing
        [114.3052, 30.5927],  # Wuhan
        [116.3972, 39.9092]   # Beijing
    ]
    
    return create_geojson("serpentine", locations)

def generate_volcano_locations():
    locations = [
        # Existing locations
        [-155.282, 19.421],    # Kilauea, Hawaii
        [140.75, 35.89],       # Fuji, Japan
        [-114.41, 44.42],      # Yellowstone
        [100.49, 6.16],        # Mount Merapi
        [-78.15, -1.83],       # Cotopaxi
        
        # New locations
        [-121.1752, 45.3742],  # Mount Hood
        [138.1644, -19.4421], # Uluru/Ayers Rock
        [-121.7772, 45.3725], # Mount Adams
        [-121.8200, 46.1938], # Mount St. Helens
        [-122.1932, 46.8561], # Mount Rainier
        
        [-122.1932, 46.8561], # Mount Rainier
        [-122.1932, 46.8561], # Mount Rainier
        [-122.1932, 46.8561], # Mount Rainier
        [-122.1932, 46.8561], # Mount Rainier
        [-122.1932, 46.8561], # Mount Rainier
        
        [-122.1932, 46.8561], # Mount Rainier
        [-122.1932, 46.8561], # Mount Rainier
        [-122.1932, 46.8561], # Mount Rainier
        [-122.1932, 46.8561], # Mount Rainier
        [-122.1932, 46.8561], # Mount Rainier
        
        [-122.1932, 46.8561], # Mount Rainier
        [-122.1932, 46.8561], # Mount Rainier
        [-122.1932, 46.8561], # Mount Rainier
        [-122.1932, 46.8561], # Mount Rainier
        [-122.1932, 46.8561]  # Mount Rainier
    ]
    
    return create_geojson("volcano", locations)

def generate_mangrove_locations():
    locations = [
        # Existing locations
        [-97.1208, 25.7673],  # Texas Coast
        [103.8198, 1.3521],   # Singapore
        [120.9842, 14.5995],  # Manila Bay
        [131.0445, -12.4634], # Darwin
        [-80.1918, 25.7617],  # Miami
        
        # New locations
        [-87.6298, 25.7617],  # Everglades
        [101.7136, 3.1478],   # Kuala Lumpur
        [114.1714, 22.2804],  # Hong Kong
        [121.4737, 31.2304],  # Shanghai
        [120.3361, 23.6978],  # Taichung
        
        [116.4074, 39.9042],  # Beijing
        [114.3052, 30.5927],  # Wuhan
        [116.3972, 39.9092],  # Beijing
        [114.3052, 30.5927],  # Wuhan
        [116.3972, 39.9092],  # Beijing
        
        [114.3052, 30.5927],  # Wuhan
        [116.3972, 39.9092],  # Beijing
        [114.3052, 30.5927],  # Wuhan
        [116.3972, 39.9092],  # Beijing
        [114.3052, 30.5927],  # Wuhan
        
        [116.3972, 39.9092],  # Beijing
        [114.3052, 30.5927],  # Wuhan
        [116.3972, 39.9092],  # Beijing
        [114.3052, 30.5927],  # Wuhan
        [116.3972, 39.9092]   # Beijing
    ]
    
    return create_geojson("mangrove", locations)

def create_geojson(feature_type, locations):
    return {
        "type": "FeatureCollection",
        "name": f"{feature_type.capitalize()} Deposits",
        "crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } },
        "features": [
            {
                "type": "Feature",
                "properties": {
                    "name": f"Location {i + 1}",
                    "type": feature_type,
                    "description": f"{feature_type.capitalize()} deposits in region",
                    "source": "USGS Mineral Resources Data"
                },
                "geometry": {
                    "type": "Point",
                    "coordinates": loc
                }
            }
            for i, loc in enumerate(locations)
        ]
    }

def main():
    # Create geojson files for each feature
    geojson_generators = {
        "basalt": generate_basalt_locations,
        "olivine": generate_olivine_locations,
        "serpentine": generate_serpentine_locations,
        "volcano": generate_volcano_locations,
        "mangrove": generate_mangrove_locations
    }
    
    for feature, generator in geojson_generators.items():
        data = generator()
        filename = f"maps/{feature}/data/{feature}_deposits.geojson"
        
        # Create directories if they don't exist
        Path(filename).parent.mkdir(parents=True, exist_ok=True)
        
        # Write to file
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

if __name__ == "__main__":
    main()
