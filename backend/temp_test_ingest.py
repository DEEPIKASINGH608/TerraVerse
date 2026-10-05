from pathlib import Path
from app.services.ingestion.vector_ingestor import VectorIngestor
from app.services.ingestion.tabular_ingestor import TabularIngestor

demo_dir = Path("data/demo")
res1 = VectorIngestor.process_vector_file(demo_dir / "revenue_parcels.geojson", "demo_revenue_101")
res2 = TabularIngestor.process_tabular_file(demo_dir / "gnss_control_points.csv", "demo_gnss_102")

print("Vector Ingestion Output:", res1)
print("Tabular Ingestion Output:", res2)