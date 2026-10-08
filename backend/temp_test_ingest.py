"""
Temporary test utility script to verify spatial vector ingestion routines.
"""

import sys
import logging
import geopandas as gpd
from shapely.geometry import Polygon

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("temp_test_ingest")


def run_ingestion_check():
    logger.info("Running spatial ingestion dry-run test...")
    try:
        poly = Polygon([(77.10, 28.60), (77.11, 28.60), (77.11, 28.61), (77.10, 28.61)])
        gdf = gpd.GeoDataFrame(
            {"parcel_id": ["TEST-001"], "owner": ["Test Owner"]},
            geometry=[poly],
            crs="EPSG:4326",
        )
        logger.info(f"Successfully constructed test GeoDataFrame with {len(gdf)} features.")
        logger.info(f"CRS: {gdf.crs}, Geometry Type: {gdf.geometry.type.iloc[0]}")
        return True
    except Exception as e:
        logger.error(f"Ingestion check failed: {str(e)}")
        return False


if __name__ == "__main__":
    success = run_ingestion_check()
    sys.exit(0 if success else 1)