# TerraVerse — GeoAI Multi-Departmental Urban Land Record Harmonization Platform

TerraVerse is an enterprise GeoAI platform designed to ingest messy, multi-CRS, schema-inconsistent urban land records across government departments and conflate them into a single **Canonical Urban Land Layer** with complete spatial provenance and confidence scoring.

## Key Technical Features
- **Automatic CRS Normalization**: Reprojects geographic (EPSG:4326) and local projected rasters/vectors into UTM Zone 43N (EPSG:32643).
- **Fuzzy Semantic Field Mapping**: Automatically maps varying attribute names (`khasra_no`, `malik_naam`, `tax_prop_id`) into unified schemas.
- **GeoAI Matcher & Precision Conflator**: Combines spatial IoU, Hausdorff distance, and weighted authority conflation.
- **Human-in-the-Loop Review Queue**: Flags parcels with confidence score < 75% for manual web verification.
- **Interactive Dual Map Twin**: WebGL split-screen inspection powered by MapLibre GL JS.

## Quick Start
```bash
# 1. Clone repository & generate raw test data
python scripts/generate_shakti_nagar_data.py

# 2. Launch containerized backend and PostGIS database
docker-compose up --build -d

# 3. Open Web Dashboard
open http://localhost:8000


Local Prototype (Current)
└── PostGIS + FastAPI Async Worker Pipeline
│
├──> Step 1: Object Storage (MinIO / AWS S3)
│       - Store raw Shapefile/GeoTIFF uploads in cloud buckets.
│
├──> Step 2: Distributed Processing (Apache Sedona / PySpark)
│       - Scale GeoAI bipartite matching across millions of state-wide parcels.
│
├──> Step 3: Kubernetes Deployment (EKS / GKE)
│       - Autoscale FastAPI worker pods based on queue depth.
│
└──> Step 4: OGC API Gateway & Departmental Microservices
- Serve dynamic vector tiles (MVT) via GeoServer/Tessella.