#!/usr/bin/env python3
"""
Diagnose engagement metrics issues
"""
import pandas as pd
import os

def diagnose_engagement():
    data_path = "/Users/arwendriadahlan/Documents/EFFECTS/scrap/POP/DATA GS/"
    gs_file = os.path.join(data_path, "GS_research.csv")
    gn_file = os.path.join(data_path, "GN_wos_scopus_data.csv")
    
    gs_data = pd.read_csv(gs_file)
    gn_data = pd.read_csv(gn_file)
    
    print("🔍 DIAGNOSING ENGAGEMENT METRICS")
    print("=" * 50)
    
    print("Global South - Views analysis:")
    print(f"  Non-zero views: {(gs_data['views'] > 0).sum()}")
    print(f"  Zero views: {(gs_data['views'] == 0).sum()}")
    print(f"  Views range: {gs_data['views'].min()} to {gs_data['views'].max()}")
    print(f"  Views data type: {gs_data['views'].dtype}")
    
    print("\nGlobal North - Views analysis:")
    print(f"  Non-zero views: {(gn_data['views'] > 0).sum()}")
    print(f"  Zero views: {(gn_data['views'] == 0).sum()}")
    print(f"  Views range: {gn_data['views'].min()} to {gn_data['views'].max()}")
    print(f"  Views data type: {gn_data['views'].dtype}")

if __name__ == "__main__":
    diagnose_engagement()
