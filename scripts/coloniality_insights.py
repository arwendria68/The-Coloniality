#!/usr/bin/env python3
"""
Deep insights into coloniality patterns from the analysis
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def coloniality_insights():
    data_path = "/Users/arwendriadahlan/Documents/EFFECTS/scrap/POP/DATA GS/"
    gs_data = pd.read_csv(data_path + "GS_research.csv")
    gn_data = pd.read_csv(data_path + "GN_wos_scopus_data.csv")
    
    print("🎯 COLONIALITY RESEARCH INSIGHTS")
    print("=" * 60)
    
    # Handle missing values
    gs_data['epistemic_category'] = gs_data['epistemic_category'].fillna('Unknown')
    gn_data['epistemic_category'] = gn_data['epistemic_category'].fillna('Unknown')
    
    # Calculate percentages
    gs_epistemic = gs_data['epistemic_category'].value_counts(normalize=True) * 100
    gn_epistemic = gn_data['epistemic_category'].value_counts(normalize=True) * 100
    
    print("🔍 KEY FINDINGS - EPISTEMIC INEQUALITY:")
    print("=" * 50)
    
    print("1. DOMINANCE OF LIS IN GLOBAL NORTH:")
    print(f"   • Global North: {gn_epistemic['Library and Information Science (LIS)']:.1f}% LIS")
    print(f"   • Global South: {gs_epistemic['Library and Information Science (LIS)']:.1f}% LIS")
    print(f"   • Difference: {gn_epistemic['Library and Information Science (LIS)'] - gs_epistemic['Library and Information Science (LIS)']:+.1f}%")
    
    print("\n2. MARGINALIZATION OF SPECIALIZED FIELDS IN GN:")
    print(f"   • Information Science in GN: {gn_epistemic.get('Information Science (IS)', 0):.1f}%")
    print(f"   • Information Science in GS: {gs_epistemic.get('Information Science (IS)', 0):.1f}%")
    print(f"   • Library Science in GN: {gn_epistemic.get('Library Science (LS)', 0):.1f}%") 
    print(f"   • Library Science in GS: {gs_epistemic.get('Library Science (LS)', 0):.1f}%")
    
    print("\n3. EPISTEMIC DIVERSITY:")
    print(f"   • GS has {len(gs_epistemic)} epistemic categories")
    print(f"   • GN has {len(gn_epistemic)} epistemic categories")
    print(f"   • GS has {len(set(gs_epistemic.index) - set(gn_epistemic.index))} unique categories")
    print(f"   • GN has {len(set(gn_epistemic.index) - set(gs_epistemic.index))} unique categories")
    
    print("\n🎯 RESEARCH IMPLICATIONS:")
    print("=" * 50)
    print("1. HEGEMONI EPISTEMIK: Global North mendominasi kategori LIS")
    print("2. MARGINALISASI: Bidang khusus (IS, LS) terpinggirkan di GN")
    print("3. PLURALITAS EPISTEMIK: GS menunjukkan keragaman kategori lebih tinggi")
    print("4. COLONIALITY OF KNOWLEDGE: Pola ini mencerminkan struktur kolonial dalam produksi pengetahuan")

if __name__ == "__main__":
    coloniality_insights()
