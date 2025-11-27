#!/usr/bin/env python3
"""
Main analysis script for Coloniality Analysis Project
Analysis of research publication patterns between Global South and Global North
Using ACTUAL research data structure
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import os
import sys

# Set style for better visualizations
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

def setup_directories():
    """Ensure all necessary directories exist"""
    directories = [
        'results/graphics',
        'results/tables', 
        'results/reports',
        'results/models'
    ]
    
    for dir_path in directories:
        Path(dir_path).mkdir(parents=True, exist_ok=True)
    print("✅ Directories setup completed")

def load_actual_data():
    """
    Load actual research data from local path
    """
    data_path = "/Users/arwendriadahlan/Documents/EFFECTS/scrap/POP/DATA GS/"
    gs_file = os.path.join(data_path, "GS_research.csv")
    gn_file = os.path.join(data_path, "GN_wos_scopus_data.csv")
    
    print("📂 Loading ACTUAL research data...")
    print(f"   GS file: {gs_file}")
    print(f"   GN file: {gn_file}")
    
    try:
        gs_data = pd.read_csv(gs_file)
        gn_data = pd.read_csv(gn_file)
        
        print(f"✅ Loaded GS data: {gs_data.shape[0]} publications, {gs_data.shape[1]} columns")
        print(f"✅ Loaded GN data: {gn_data.shape[0]} publications, {gn_data.shape[1]} columns")
        
        return gs_data, gn_data
        
    except FileNotFoundError as e:
        print(f"❌ File not found: {e}")
        return None, None

def basic_comparative_analysis(gs_data, gn_data):
    """Perform basic comparative analysis between GS and GN"""
    print("\n📊 BASIC COMPARATIVE ANALYSIS")
    print("=" * 60)
    
    # Publication counts
    print(f"🌍 GLOBAL SOUTH: {len(gs_data)} publications")
    print(f"🌐 GLOBAL NORTH: {len(gn_data)} publications")
    print(f"📈 GS/GN Ratio: {len(gs_data)/len(gn_data):.2%}")
    
    # Year analysis
    print(f"\n📅 YEAR RANGE:")
    print(f"   GS: {gs_data['year'].min():.0f} - {gs_data['year'].max():.0f}")
    print(f"   GN: {gn_data['year'].min()} - {gn_data['year'].max()}")
    
    # Database sources
    print(f"\n🗃️ DATABASE DISTRIBUTION:")
    if 'database' in gs_data.columns:
        gs_db = gs_data['database'].value_counts()
        print("   Global South:")
        for db, count in gs_db.items():
            print(f"     {db}: {count} publications")
    
    if 'database' in gn_data.columns:
        gn_db = gn_data['database'].value_counts()
        print("   Global North:")
        for db, count in gn_db.items():
            print(f"     {db}: {count} publications")

def analyze_epistemic_categories(gs_data, gn_data):
    """Analyze epistemic categories distribution"""
    print(f"\n🎯 EPISTEMIC CATEGORY ANALYSIS")
    print("=" * 50)
    
    if 'epistemic_category' in gs_data.columns:
        gs_epistemic = gs_data['epistemic_category'].value_counts()
        print("Global South Epistemic Categories:")
        for category, count in gs_epistemic.head(10).items():
            print(f"  {category}: {count} publications")
    
    if 'epistemic_category' in gn_data.columns:
        gn_epistemic = gn_data['epistemic_category'].value_counts()
        print("\nGlobal North Epistemic Categories:")
        for category, count in gn_epistemic.head(10).items():
            print(f"  {category}: {count} publications")

def analyze_research_domains(gs_data, gn_data):
    """Analyze research domains distribution"""
    print(f"\n🔬 RESEARCH DOMAIN ANALYSIS")
    print("=" * 50)
    
    if 'research_domain' in gs_data.columns:
        gs_domains = gs_data['research_domain'].value_counts()
        print("Global South Research Domains:")
        for domain, count in gs_domains.head(8).items():
            print(f"  {domain}: {count} publications")
    
    if 'research_domain' in gn_data.columns:
        gn_domains = gn_data['research_domain'].value_counts()
        print("\nGlobal North Research Domains:")
        for domain, count in gn_domains.head(8).items():
            print(f"  {domain}: {count} publications")

def create_comparative_visualizations(gs_data, gn_data):
    """Create comparative visualizations based on actual data"""
    print(f"\n📈 CREATING COMPARATIVE VISUALIZATIONS")
    print("=" * 50)
    
    # 1. Publication trends over time
    plt.figure(figsize=(12, 6))
    
    # GS yearly trend
    gs_yearly = gs_data.groupby('year').size()
    # GN yearly trend
    gn_yearly = gn_data.groupby('year').size()
    
    plt.plot(gs_yearly.index, gs_yearly.values, marker='o', linewidth=2, label='Global South')
    plt.plot(gn_yearly.index, gn_yearly.values, marker='s', linewidth=2, label='Global North')
    
    plt.xlabel('Year')
    plt.ylabel('Number of Publications')
    plt.title('Publication Trends: Global South vs Global North')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('results/graphics/publication_trends_actual.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✅ Created: publication_trends_actual.png")
    
    # 2. Epistemic categories comparison
    if 'epistemic_category' in gs_data.columns and 'epistemic_category' in gn_data.columns:
        plt.figure(figsize=(14, 8))
        
        # Get top categories
        gs_top_cats = gs_data['epistemic_category'].value_counts().head(8)
        gn_top_cats = gn_data['epistemic_category'].value_counts().head(8)
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
        
        ax1.pie(gs_top_cats.values, labels=gs_top_cats.index, autopct='%1.1f%%', startangle=90)
        ax1.set_title('Global South - Epistemic Categories')
        
        ax2.pie(gn_top_cats.values, labels=gn_top_cats.index, autopct='%1.1f%%', startangle=90)
        ax2.set_title('Global North - Epistemic Categories')
        
        plt.tight_layout()
        plt.savefig('results/graphics/epistemic_categories_comparison.png', dpi=300, bbox_inches='tight')
        plt.close()
        print("✅ Created: epistemic_categories_comparison.png")

def analyze_engagement_metrics(gs_data, gn_data):
    """Analyze views and downloads engagement metrics"""
    print(f"\n👀 ENGAGEMENT METRICS ANALYSIS")
    print("=" * 50)
    
    if 'views' in gs_data.columns and 'downloads' in gs_data.columns:
        print("Global South Engagement:")
        print(f"  Average views: {gs_data['views'].mean():.1f}")
        print(f"  Average downloads: {gs_data['downloads'].mean():.1f}")
        print(f"  Views/Downloads ratio: {gs_data['views'].mean()/gs_data['downloads'].mean():.2f}")
    
    if 'views' in gn_data.columns and 'downloads' in gn_data.columns:
        print("\nGlobal North Engagement:")
        print(f"  Average views: {gn_data['views'].mean():.1f}")
        print(f"  Average downloads: {gn_data['downloads'].mean():.1f}")
        print(f"  Views/Downloads ratio: {gn_data['views'].mean()/gn_data['downloads'].mean():.2f}")

def save_detailed_analysis(gs_data, gn_data):
    """Save detailed analysis results"""
    print(f"\n💾 SAVING DETAILED ANALYSIS RESULTS")
    print("=" * 50)
    
    # Save summary statistics
    summary_data = {
        'Metric': ['Total Publications', 'Year Range', 'Average Views', 'Average Downloads'],
        'Global_South': [
            len(gs_data),
            f"{gs_data['year'].min():.0f}-{gs_data['year'].max():.0f}",
            f"{gs_data['views'].mean():.1f}" if 'views' in gs_data.columns else 'N/A',
            f"{gs_data['downloads'].mean():.1f}" if 'downloads' in gs_data.columns else 'N/A'
        ],
        'Global_North': [
            len(gn_data),
            f"{gn_data['year'].min()}-{gn_data['year'].max()}",
            f"{gn_data['views'].mean():.1f}" if 'views' in gn_data.columns else 'N/A',
            f"{gn_data['downloads'].mean():.1f}" if 'downloads' in gn_data.columns else 'N/A'
        ]
    }
    
    summary_df = pd.DataFrame(summary_data)
    summary_df.to_csv('results/tables/detailed_summary_statistics.csv', index=False)
    print("✅ Saved: detailed_summary_statistics.csv")
    
    # Save country distribution
    if 'country_final' in gs_data.columns:
        country_dist = gs_data['country_final'].value_counts().head(15)
        country_dist.to_csv('results/tables/gs_country_distribution.csv')
        print("✅ Saved: gs_country_distribution.csv")

def generate_comprehensive_report(gs_data, gn_data):
    """Generate comprehensive analysis report"""
    print(f"\n📝 GENERATING COMPREHENSIVE REPORT")
    print("=" * 50)
    
    report_content = f"""
COLONIALITY ANALYSIS PROJECT - COMPREHENSIVE REPORT
Generated on: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}

DATASET OVERVIEW:
- Global South publications: {len(gs_data)}
- Global North publications: {len(gn_data)}
- Total publications analyzed: {len(gs_data) + len(gn_data)}

KEY COMPARATIVE FINDINGS:

1. PUBLICATION VOLUME:
   - GS/GN Ratio: {len(gs_data)/len(gn_data):.2%}
   - Year Range - GS: {gs_data['year'].min():.0f}-{gs_data['year'].max():.0f}
   - Year Range - GN: {gn_data['year'].min()}-{gn_data['year'].max()}

2. ENGAGEMENT METRICS:
   - GS Average Views: {gs_data['views'].mean():.1f} | Downloads: {gs_data['downloads'].mean():.1f}
   - GN Average Views: {gn_data['views'].mean():.1f} | Downloads: {gn_data['downloads'].mean():.1f}

3. RESEARCH FOCUS:
   - Analysis of epistemic categories and research domains completed
   - Country distribution analysis completed

NEXT RESEARCH QUESTIONS TO EXPLORE:
- Deep dive into epistemic category differences
- Keyword analysis for topic modeling
- Citation analysis (if citation data available)
- Collaboration patterns between regions

---
This report generated from actual research data for coloniality analysis.
    """
    
    with open('results/reports/comprehensive_analysis_report.txt', 'w') as f:
        f.write(report_content)
    
    print("✅ Generated: comprehensive_analysis_report.txt")

def main():
    """Main analysis function"""
    print("=" * 70)
    print("🎯 COLONIALITY ANALYSIS PROJECT - ACTUAL DATA ANALYSIS")
    print("=" * 70)
    
    # Setup directories
    setup_directories()
    
    # Load actual data
    gs_data, gn_data = load_actual_data()
    
    if gs_data is None or gn_data is None:
        print("❌ Failed to load data. Exiting.")
        return
    
    # Perform analyses
    basic_comparative_analysis(gs_data, gn_data)
    analyze_epistemic_categories(gs_data, gn_data)
    analyze_research_domains(gs_data, gn_data)
    analyze_engagement_metrics(gs_data, gn_data)
    create_comparative_visualizations(gs_data, gn_data)
    save_detailed_analysis(gs_data, gn_data)
    generate_comprehensive_report(gs_data, gn_data)
    
    # Final summary
    print("\n" + "=" * 70)
    print("🎉 ACTUAL DATA ANALYSIS COMPLETED SUCCESSFULLY!")
    print("=" * 70)
    print(f"\n📁 Output files created in results/ folder")
    print(f"📊 Analysis based on {len(gs_data) + len(gn_data)} total publications")
    print(f"\n🔍 Next: Examine the generated visualizations and tables for insights!")

if __name__ == "__main__":
    main()
