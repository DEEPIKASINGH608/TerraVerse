import json
import os
import random
import numpy as np
from pathlib import Path
import geopandas as gpd
from shapely.geometry import Polygon, Point, MultiPolygon
from shapely.affinity import translate, scale, rotate

BASE_LON = 82.5000
BASE_LAT = 25.0000

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "data" / "demo"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def generate_shakti_nagar_data():
    print("Generating Shakti Nagar Multi-Source Geospatial Datasets...")

    base_parcels = []
    grid_size = 10
    step = 0.001 

    parcel_counter = 101
    for i in range(grid_size):
        for j in range(grid_size):
            min_x = BASE_LON + (i * step)
            min_y = BASE_LAT + (j * step)
            max_x = min_x + step * 0.95
            max_y = min_y + step * 0.95

            poly = Polygon([
                (min_x, min_y),
                (max_x + random.uniform(-0.00005, 0.00005), min_y),
                (max_x, max_y),
                (min_x, max_y + random.uniform(-0.00005, 0.00005))
            ])

            base_parcels.append({
                "pid": f"SN-P-{parcel_counter}",
                "khasra_no": f"{parcel_counter}",
                "geometry": poly,
                "owner": f"Owner_{parcel_counter}",
                "land_use": random.choice(["Residential", "Commercial", "Agricultural", "Mixed Use"])
            })
            parcel_counter += 1

    revenue_features = []
    for item in base_parcels:
        shifted_geom = translate(item["geometry"], xoff=0.00003, yoff=-0.00002)
        revenue_features.append({
            "type": "Feature",
            "properties": {
                "Khasra_No": item["khasra_no"],
                "Owner_Name": item["owner"],
                "Land_Type": item["land_use"],
                "Recorded_Area": round(shifted_geom.area * 10000000, 2),
                "Survey_Year": 2012
            },
            "geometry": shifted_geom.__geo_interface__
        })

    revenue_geojson = {
        "type": "FeatureCollection",
        "crs": {"type": "name", "properties": {"name": "urn:ogc:def:crs:OGC:1.3:CRS84"}},
        "features": revenue_features
    }
    with open(OUTPUT_DIR / "revenue_parcels.geojson", "w") as f:
        json.dump(revenue_geojson, f, indent=2)
    print("✓ Created revenue_parcels.geojson (Revenue Department)")

    municipal_features = []
    for idx, item in enumerate(base_parcels):
        geom = item["geometry"]
        if idx % 10 == 0:
            geom = scale(geom, xfact=1.08, yfact=1.08)

        municipal_features.append({
            "type": "Feature",
            "properties": {
                "Property_ID": f"M-SHAKTI-{1000 + idx}",
                "Khasra_Ref": item["khasra_no"] if idx % 5 != 0 else None, # Missing refs
                "Tax_Owner": item["owner"] if idx % 3 != 0 else "UNKNOWN / DISPUTED",
                "Usage_Category": item["land_use"][:3].upper(), # e.g. RES, COM
                "Assessment_Year": 2024
            },
            "geometry": geom.__geo_interface__
        })

    municipal_geojson = {
        "type": "FeatureCollection",
        "features": municipal_features
    }
    with open(OUTPUT_DIR / "municipal_parcels.geojson", "w") as f:
        json.dump(municipal_geojson, f, indent=2)
    print("✓ Created municipal_parcels.geojson (Municipal Corporation)")

    drone_features = []
    for item in base_parcels:
        drone_features.append({
            "type": "Feature",
            "properties": {
                "Drone_Feature_ID": f"DRONE-2026-{item['khasra_no']}",
                "Confidence_Score": 0.98,
                "Extracted_Buildings": random.randint(1, 4),
                "Capture_Date": "2026-03-15"
            },
            "geometry": item["geometry"].__geo_interface__
        })

    drone_geojson = {
        "type": "FeatureCollection",
        "features": drone_features
    }
    with open(OUTPUT_DIR / "drone_parcels.geojson", "w") as f:
        json.dump(drone_geojson, f, indent=2)
    print("✓ Created drone_parcels.geojson (Survey Department Drone)")

    gnss_lines = ["Point_ID,Latitude,Longitude,Elevation_m,Accuracy_mm,Surveyor_Notes\n"]
    for item in base_parcels:
        centroid = item["geometry"].centroid
        gnss_lines.append(f"GNSS-{item['khasra_no']},{centroid.y:.7f},{centroid.x:.7f},245.12,4.5,Verified Boundary Marker\n")

    with open(OUTPUT_DIR / "gnss_control_points.csv", "w") as f:
        f.writelines(gnss_lines)
    print("✓ Created gnss_control_points.csv (CORS / GNSS Control Points)")

    road_features = []
    for i in range(2):
        y_coord = BASE_LAT + (i * 0.005) + 0.0025
        line = Polygon([
            (BASE_LON - 0.001, y_coord - 0.0001),
            (BASE_LON + 0.012, y_coord - 0.0001),
            (BASE_LON + 0.012, y_coord + 0.0001),
            (BASE_LON - 0.001, y_coord + 0.0001)
        ])
        road_features.append({
            "type": "Feature",
            "properties": {"Road_Name": f"Shakti Main Avenue Line {i+1}", "Width_m": 12},
            "geometry": line.__geo_interface__
        })
    with open(OUTPUT_DIR / "roads.geojson", "w") as f:
        json.dump({"type": "FeatureCollection", "features": road_features}, f, indent=2)
    print("✓ Created roads.geojson (Road Network Infrastructure)")

    print("\nSuccessfully generated Shakti Nagar synthetic test suite in /data/demo/")

if __name__ == "__main__":
    generate_shakti_nagar_data()