#!/usr/bin/env python3
"""
Comprehensive data quality check
"""
import pandas as pd
import numpy as np

def data_quality_report():
    data_path = "/Users/arwendriadahlan/Documents/EFFECTS/scrap/POP/DATA GS/"
    gs_data = pd.read_csv(data_path + "GS_research.csv")
    gn_data = pd.read_csv(data_path + "GN_wos_scopus_data.csv")
    
    print("🔍 COMPREHENSIVE DATA QUALITY REPORT")
    print("=" * 60)
    
    print("📁 GLOBAL SOUTH DATA QUALITY:")
    print(f"Total records: {len(gs_data)}")
    print(f"Columns: {list(gs_data.columns)}")
    print("\nMissing values per column:")
    for col in gs_data.columns:
        missing = gs_data[col].isna().sum()
        if missing > 0:
            print(f"  {col:<25} {missing:4d} missing ({missing/len(gs_data):.1%})")
    
    print(f"\nYear statistics:")
    print(f"  Min: {gs_data['year'].min()}")
    print(f"  Max: {gs_data['year'].max()}")
    print(f"  Mean: {gs_data['year'].mean():.1f}")
    print(f"  Missing: {gs_data['year'].isna().sum()}")
    
    print(f"\n📁 GLOBAL NORTH DATA QUALITY:")
    print(f"Total records: {len(gn_data)}")
    print(f"Columns: {list(gn_data.columns)}")
    print("\nMissing values per column:")
    for col in gn_data.columns:
        missing = gn_data[col].isna().sum()
        if missing > 0:
            print(f"  {col:<25} {missing:4d} missing ({missing/len(gn_data):.1%})")
    
    print(f"\nYear statistics:")
    print(f"  Min: {gn_data['year'].min()}")
    print(f"  Max: {gn_data['year'].max()}")
    print(f"  Mean: {gn_data['year'].mean():.1f}")
    print(f"  Missing: {gn_data['year'].isna().sum()}")

if __name__ == "__main__":
    data_quality_report()
