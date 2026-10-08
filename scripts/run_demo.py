"""
CLI One-Click Workflow Execution Script.
Executes data generation, seeding, and engine pipeline processing.
"""
import subprocess
import sys

def main():
    print("🚀 Running TerraVerse Full Workflow Demo...")

    # 1. Generate Demo Data
    print("\n[1/3] Generating demo geospatial datasets...")
    subprocess.run([sys.executable, "scripts/generate_demo_data.py"], check=True)

    # 2. Seed Database
    print("\n[2/3] Seeding database tables...")
    subprocess.run([sys.executable, "scripts/seed_database.py"], check=True)

    # 3. Train Match Model
    print("\n[3/3] Training record linkage ML model...")
    subprocess.run([sys.executable, "scripts/train_match_model.py"], check=True)

    print("\n✅ TerraVerse demo setup completed successfully!")

if __name__ == "__main__":
    main()