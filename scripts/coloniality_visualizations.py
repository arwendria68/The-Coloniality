#!/usr/bin/env python3
"""
Create compelling visualizations for coloniality findings
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def create_coloniality_visualizations():
    data_path = "/Users/arwendriadahlan/Documents/EFFECTS/scrap/POP/DATA GS/"
    gs_data = pd.read_csv(data_path + "GS_research.csv")
    gn_data = pd.read_csv(data_path + "GN_wos_scopus_data.csv")
    
    # Set style
    plt.style.use('seaborn-v0_8')
    sns.set_palette("Set2")
    
    # Prepare data
    gs_data['epistemic_category'] = gs_data['epistemic_category'].fillna('Unknown')
    gn_data['epistemic_category'] = gn_data['epistemic_category'].fillna('Unknown')
    
    # 1. Epistemic Category Comparison Bar Chart
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    # GS epistemic categories
    gs_counts = gs_data['epistemic_category'].value_counts()
    ax1.bar(gs_counts.index, gs_counts.values, color='skyblue', alpha=0.7)
    ax1.set_title('Global South - Epistemic Categories', fontsize=14, fontweight='bold')
    ax1.set_ylabel('Number of Publications')
    ax1.tick_params(axis='x', rotation=45)
    
    # GN epistemic categories  
    gn_counts = gn_data['epistemic_category'].value_counts()
    ax2.bar(gn_counts.index, gn_counts.values, color='lightcoral', alpha=0.7)
    ax2.set_title('Global North - Epistemic Categories', fontsize=14, fontweight='bold')
    ax2.set_ylabel('Number of Publications')
    ax2.tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.savefig('results/graphics/epistemic_comparison_bar.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✅ Created: epistemic_comparison_bar.png")
    
    # 2. Percentage Comparison
    categories = ['Library and Information Science (LIS)', 'Information Science (IS)', 'Library Science (LS)']
    gs_percentages = [gs_counts.get(cat, 0)/len(gs_data)*100 for cat in categories]
    gn_percentages = [gn_counts.get(cat, 0)/len(gn_data)*100 for cat in categories]
    
    x = np.arange(len(categories))
    width = 0.35
    
    plt.figure(figsize=(12, 6))
    plt.bar(x - width/2, gs_percentages, width, label='Global South', color='skyblue', alpha=0.7)
    plt.bar(x + width/2, gn_percentages, width, label='Global North', color='lightcoral', alpha=0.7)
    
    plt.xlabel('Epistemic Categories')
    plt.ylabel('Percentage of Publications (%)')
    plt.title('Epistemic Category Distribution: Global South vs Global North', fontsize=14, fontweight='bold')
    plt.xticks(x, categories, rotation=15)
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Add value labels
    for i, v in enumerate(gs_percentages):
        plt.text(i - width/2, v + 1, f'{v:.1f}%', ha='center', va='bottom')
    for i, v in enumerate(gn_percentages):
        plt.text(i + width/2, v + 1, f'{v:.1f}%', ha='center', va='bottom')
    
    plt.tight_layout()
    plt.savefig('results/graphics/epistemic_percentage_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✅ Created: epistemic_percentage_comparison.png")
    
    # 3. Coloniality Gap Visualization
    gap_data = pd.DataFrame({
        'Category': categories,
        'GS_Percentage': gs_percentages,
        'GN_Percentage': gn_percentages,
        'Gap': [gs_p - gn_p for gs_p, gn_p in zip(gs_percentages, gn_percentages)]
    })
    
    plt.figure(figsize=(10, 6))
    plt.barh(gap_data['Category'], gap_data['Gap'], color=['red' if x < 0 else 'green' for x in gap_data['Gap']], alpha=0.7)
    plt.xlabel('Percentage Gap (GS - GN)')
    plt.title('Epistemic Coloniality Gap: Global South vs Global North', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    
    # Add value labels
    for i, v in enumerate(gap_data['Gap']):
        plt.text(v, i, f'{v:+.1f}%', va='center', ha='left' if v > 0 else 'right')
    
    plt.tight_layout()
    plt.savefig('results/graphics/coloniality_gap.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✅ Created: coloniality_gap.png")

if __name__ == "__main__":
    create_coloniality_visualizations()
