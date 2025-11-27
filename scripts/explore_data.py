#!/usr/bin/env python3
"""
Explore the structure of your actual data files
"""
import pandas as pd
import os

def explore_data_files():
    """Explore the structure of GS and GN data files"""

    # Path to your actual data
    data_path = "/Users/arwendriadahlan/Documents/EFFECTS/scrap/POP/DATA GS/"
    gs_file = os.path.join(data_path, "GS_research.csv")
    gn_file = os.path.join(data_path, "GN_wos_scopus_data.csv")

    print("🔍 EXPLORING YOUR DATA STRUCTURE")
    print("=" * 50)

    # Check if files exist
    print(f"GS file exists: {os.path.exists(gs_file)}")
    print(f"GN file exists: {os.path.exists(gn_file)}")

    if os.path.exists(gs_file):
        print(f"\n📊 GS RESEARCH DATA STRUCTURE:")
        try:
            gs_data = pd.read_csv(gs_file)
            print(f"Shape: {gs_data.shape}")
            print(f"Columns: {list(gs_data.columns)}")
            print(f"Data types:\n{gs_data.dtypes}")
            print(f"\nFirst 3 rows:")
            print(gs_data.head(3))
        except Exception as e:
            print(f"Error reading GS file: {e}")

    if os.path.exists(gn_file):
        print(f"\n🌐 GN WOS/SCOPUS DATA STRUCTURE:")
        try:
            gn_data = pd.read_csv(gn_file)
            print(f"Shape: {gn_data.shape}")
            print(f"Columns: {list(gn_data.columns)}")
            print(f"Data types:\n{gn_data.dtypes}")
            print(f"\nFirst 3 rows:")
            print(gn_data.head(3))
        except Exception as e:
            print(f"Error reading GN file: {e}")

if __name__ == "__main__":
    explore_data_files()
