import os
import json
from pathlib import Path

def validate_coordinates(coord):
    """Validate if coordinates are valid (longitude, latitude)"""
    if not isinstance(coord, list) or len(coord) != 2:
        return False
    
    lon, lat = coord
    
    # Check if coordinates are numbers
    if not (isinstance(lon, (int, float)) and isinstance(lat, (int, float))):
        return False
    
    # Check if coordinates are within valid ranges
    if not (-180 <= lon <= 180) or not (-90 <= lat <= 90):
        return False
    
    return True

def verify_json_file(file_path):
    """Verify coordinates in a GeoJSON file"""
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            
        if data.get('type') != 'FeatureCollection':
            print(f"Error in {file_path}: Not a valid GeoJSON FeatureCollection")
            return False
            
        features = data.get('features', [])
        if not features:
            print(f"Error in {file_path}: No features found")
            return False
            
        for feature in features:
            geometry = feature.get('geometry')
            if not geometry:
                print(f"Error in {file_path}: Feature missing geometry")
                continue
                
            coordinates = geometry.get('coordinates')
            if not coordinates:
                print(f"Error in {file_path}: Feature missing coordinates")
                continue
                
            if geometry['type'] == 'Point':
                if not validate_coordinates(coordinates):
                    print(f"Error in {file_path}: Invalid point coordinates: {coordinates}")
            elif geometry['type'] == 'Polygon':
                for ring in coordinates:
                    for coord in ring:
                        if not validate_coordinates(coord):
                            print(f"Error in {file_path}: Invalid polygon coordinates: {coord}")
            else:
                print(f"Warning in {file_path}: Unsupported geometry type: {geometry['type']}")
                
        return True
        
    except json.JSONDecodeError:
        print(f"Error in {file_path}: Invalid JSON format")
        return False
    except Exception as e:
        print(f"Error in {file_path}: {str(e)}")
        return False

def verify_all_files():
    """Verify all GeoJSON files in the maps directory"""
    base_dir = Path("maps")
    valid_files = []
    invalid_files = []
    
    for folder in ["basalt", "olivine", "serpentine", "volcanic", "mangrove"]:
        folder_path = base_dir / folder / "geojson"
        if not folder_path.exists():
            print(f"Warning: Folder {folder_path} does not exist")
            continue
            
        for file in folder_path.glob("*.geojson"):
            print(f"\nVerifying {file}...")
            if verify_json_file(file):
                valid_files.append(file)
            else:
                invalid_files.append(file)
    
    print("\nVerification Summary:")
    print(f"Valid files: {len(valid_files)}")
    print(f"Invalid files: {len(invalid_files)}")
    
    if invalid_files:
        print("\nFiles with issues:")
        for file in invalid_files:
            print(file)

def main():
    verify_all_files()

if __name__ == "__main__":
    main()
