#!/usr/bin/env python3
"""
Improved analysis with better data handling and error handling
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def improved_analysis():
    data_path = "/Users/arwendriadahlan/Documents/EFFECTS/scrap/POP/DATA GS/"
    gs_data = pd.read_csv(data_path + "GS_research.csv")
    gn_data = pd.read_csv(data_path + "GN_wos_scopus_data.csv")
    
    print("🎯 IMPROVED COLONIALITY ANALYSIS")
    print("=" * 60)
    
    # Handle missing values in year column
    print("🔧 DATA QUALITY CHECK:")
    print(f"GS - Missing years: {gs_data['year'].isna().sum()}")
    print(f"GN - Missing years: {gn_data['year'].isna().sum()}")
    
    # Fill NaN years with 0 and convert to int
    gs_data['year'] = gs_data['year'].fillna(0).astype(int)
    gn_data['year'] = gn_data['year'].fillna(0).astype(int)
    
    # Filter out zero years for meaningful analysis
    gs_data_clean = gs_data[gs_data['year'] > 0]
    gn_data_clean = gn_data[gn_data['year'] > 0]
    
    print(f"📊 PUBLICATION ANALYSIS (with valid years):")
    print(f"Global South: {len(gs_data_clean)} pubs ({gs_data_clean['year'].min()}-{gs_data_clean['year'].max()})")
    print(f"Global North: {len(gn_data_clean)} pubs ({gn_data_clean['year'].min()}-{gn_data_clean['year'].max()})")
    print(f"Gap: {len(gn_data_clean) - len(gs_data_clean)} publications")
    print(f"GS/GN Ratio: {len(gs_data_clean)/len(gn_data_clean):.1%}")
    
    # Analyze epistemic categories in detail
    if 'epistemic_category' in gs_data.columns:
        print(f"\n🔍 EPISTEMIC CATEGORIES - Global South:")
        gs_epistemic_counts = gs_data['epistemic_category'].value_counts()
        total_gs = len(gs_data)
        for cat, count in gs_epistemic_counts.head(8).items():
            percentage = (count / total_gs) * 100
            print(f"  {cat:<50} {count:4d} pubs ({percentage:5.1f}%)")
    
    if 'epistemic_category' in gn_data.columns:
        print(f"\n🔍 EPISTEMIC CATEGORIES - Global North:")
        gn_epistemic_counts = gn_data['epistemic_category'].value_counts()
        total_gn = len(gn_data)
        for cat, count in gn_epistemic_counts.head(8).items():
            percentage = (count / total_gn) * 100
            print(f"  {cat:<50} {count:4d} pubs ({percentage:5.1f}%)")

if __name__ == "__main__":
    improved_analysis()
