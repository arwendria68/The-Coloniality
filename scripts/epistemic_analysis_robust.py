#!/usr/bin/env python3
"""
Robust epistemic analysis with error handling
"""
import pandas as pd
import numpy as np

def robust_epistemic_analysis():
    data_path = "/Users/arwendriadahlan/Documents/EFFECTS/scrap/POP/DATA GS/"
    gs_data = pd.read_csv(data_path + "GS_research.csv")
    gn_data = pd.read_csv(data_path + "GN_wos_scopus_data.csv")
    
    print("🎯 ROBUST EPISTEMIC INEQUALITY ANALYSIS")
    print("=" * 60)
    
    # Handle missing epistemic categories
    gs_data['epistemic_category'] = gs_data['epistemic_category'].fillna('Unknown')
    gn_data['epistemic_category'] = gn_data['epistemic_category'].fillna('Unknown')
    
    # Get epistemic categories
    gs_epistemic = gs_data['epistemic_category'].value_counts()
    gn_epistemic = gn_data['epistemic_category'].value_counts()
    
    print("TOP EPISTEMIC CATEGORIES COMPARISON:")
    print("\n📍 GLOBAL SOUTH (Top 10):")
    print("-" * 70)
    for i, (cat, count) in enumerate(gs_epistemic.head(10).items(), 1):
        percentage = (count / len(gs_data)) * 100
        print(f"  {i:2d}. {cat:<45} {count:4d} pubs ({percentage:5.1f}%)")
    
    print("\n📍 GLOBAL NORTH (Top 10):")
    print("-" * 70)
    for i, (cat, count) in enumerate(gn_epistemic.head(10).items(), 1):
        percentage = (count / len(gn_data)) * 100
        print(f"  {i:2d}. {cat:<45} {count:4d} pubs ({percentage:5.1f}%)")
    
    # Comparative analysis
    print(f"\n📊 COMPARATIVE ANALYSIS:")
    print(f"Total GS categories: {len(gs_epistemic)}")
    print(f"Total GN categories: {len(gn_epistemic)}")
    
    # Find overlapping and unique categories
    gs_categories = set(gs_epistemic.index)
    gn_categories = set(gn_epistemic.index)
    
    common_categories = gs_categories & gn_categories
    unique_to_gs = gs_categories - gn_categories
    unique_to_gn = gn_categories - gs_categories
    
    print(f"Common categories: {len(common_categories)}")
    print(f"Unique to Global South: {len(unique_to_gs)}")
    print(f"Unique to Global North: {len(unique_to_gn)}")
    
    # Show top common categories
    print(f"\n🏆 TOP SHARED CATEGORIES:")
    common_gs = gs_epistemic[gs_epistemic.index.isin(common_categories)].head(5)
    common_gn = gn_epistemic[gn_epistemic.index.isin(common_categories)].head(5)
    
    for (cat_gs, count_gs), (cat_gn, count_gn) in zip(common_gs.items(), common_gn.items()):
        pct_gs = (count_gs / len(gs_data)) * 100
        pct_gn = (count_gn / len(gn_data)) * 100
        print(f"  {cat_gs:<45} GS: {pct_gs:4.1f}% | GN: {pct_gn:4.1f}% | Diff: {pct_gs-pct_gn:+.1f}%")

if __name__ == "__main__":
    robust_epistemic_analysis()
