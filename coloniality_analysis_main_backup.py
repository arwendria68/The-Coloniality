#!/usr/bin/env python3
"""
Main analysis script for Coloniality Analysis Project
Analysis of research publication patterns between Global South and Global North
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

def load_data(use_sample_data=True):
    """
    Load research data from appropriate source
    """
    if use_sample_data:
        # Use sample data from repository
        data_path = Path("data")
        gs_file = data_path / "sample_gs_research.csv"
        gn_file = data_path / "sample_gn_wos_scopus.csv"
        data_source = "SAMPLE"
    else:
        # Use original data from local path
        data_path = "/Users/arwendriadahlan/Documents/EFFECTS/scrap/POP/DATA GS/"
        gs_file = os.path.join(data_path, "GS_research.csv")
        gn_file = os.path.join(data_path, "GN_wos_scopus_data.csv")
        data_source = "ORIGINAL"
    
    print(f"📂 Using {data_source} data")
    print(f"   GS file: {gs_file}")
    print(f"   GN file: {gn_file}")
    
    try:
        gs_data = pd.read_csv(gs_file)
        gn_data = pd.read_csv(gn_file)
        
        print(f"✅ Loaded GS data: {gs_data.shape[0]} records, {gs_data.shape[1]} columns")
        print(f"✅ Loaded GN data: {gn_data.shape[0]} records, {gn_data.shape[1]} columns")
        
        return gs_data, gn_data, data_source
        
    except FileNotFoundError as e:
        print(f"❌ File not found: {e}")
        if use_sample_data:
            print("💡 Tip: Run 'python data/generate_sample_data.py' to create sample data")
        return None, None, data_source

def basic_descriptive_analysis(gs_data, gn_data, data_source):
    """Perform basic descriptive analysis"""
    print("\n📊 BASIC DESCRIPTIVE ANALYSIS")
    print("=" * 50)
    
    # GS Data Analysis
    print("\n🌍 GLOBAL SOUTH RESEARCH DATA:")
    print(f"Total publications: {len(gs_data)}")
    
    if 'citations' in gs_data.columns:
        print(f"Average citations: {gs_data['citations'].mean():.2f}")
        print(f"Max citations: {gs_data['citations'].max()}")
    
    if 'year' in gs_data.columns:
        year_range = f"{gs_data['year'].min()}-{gs_data['year'].max()}"
        print(f"Year range: {year_range}")
    
    if 'country' in gs_data.columns:
        top_countries = gs_data['country'].value_counts().head(5)
        print("\nTop 5 countries:")
        for country, count in top_countries.items():
            print(f"  {country}: {count} publications")
    
    # GN Data Analysis  
    print("\n🌐 GLOBAL NORTH RESEARCH DATA:")
    print(f"Total publications: {len(gn_data)}")
    
    if 'citations' in gn_data.columns:
        print(f"Average citations: {gn_data['citations'].mean():.2f}")
        print(f"Max citations: {gn_data['citations'].max()}")
    
    if 'region' in gn_data.columns:
        region_dist = gn_data['region'].value_counts()
        print("\nRegional distribution:")
        for region, count in region_dist.items():
            print(f"  {region}: {count} publications")

def create_visualizations(gs_data, gn_data, data_source):
    """Create comparative visualizations"""
    print("\n📈 CREATING VISUALIZATIONS")
    print("=" * 50)
    
    # 1. Citation comparison
    if 'citations' in gs_data.columns and 'citations' in gn_data.columns:
        plt.figure(figsize=(10, 6))
        
        citation_data = pd.DataFrame({
            'Region': ['Global South'] * len(gs_data) + ['Global North'] * len(gn_data),
            'Citations': list(gs_data['citations']) + list(gn_data['citations'])
        })
        
        sns.boxplot(x='Region', y='Citations', data=citation_data)
        plt.title('Citation Distribution: Global South vs Global North')
        plt.tight_layout()
        plt.savefig('results/graphics/citation_comparison.png', dpi=300, bbox_inches='tight')
        plt.close()
        print("✅ Created: citation_comparison.png")
    
    # 2. Publication trends over time
    if 'year' in gs_data.columns and 'year' in gn_data.columns:
        plt.figure(figsize=(12, 6))
        
        gs_year_counts = gs_data['year'].value_counts().sort_index()
        gn_year_counts = gn_data['year'].value_counts().sort_index()
        
        plt.plot(gs_year_counts.index, gs_year_counts.values, marker='o', label='Global South', linewidth=2)
        plt.plot(gn_year_counts.index, gn_year_counts.values, marker='s', label='Global North', linewidth=2)
        
        plt.xlabel('Year')
        plt.ylabel('Number of Publications')
        plt.title('Publication Trends Over Time')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig('results/graphics/publication_trends.png', dpi=300, bbox_inches='tight')
        plt.close()
        print("✅ Created: publication_trends.png")
    
    # 3. Research field distribution
    if 'field' in gs_data.columns:
        plt.figure(figsize=(10, 8))
        field_counts = gs_data['field'].value_counts()
        
        plt.pie(field_counts.values, labels=field_counts.index, autopct='%1.1f%%', startangle=90)
        plt.title('Research Field Distribution - Global South')
        plt.tight_layout()
        plt.savefig('results/graphics/gs_field_distribution.png', dpi=300, bbox_inches='tight')
        plt.close()
        print("✅ Created: gs_field_distribution.png")

def save_analysis_results(gs_data, gn_data, data_source):
    """Save analysis results and tables"""
    print("\n💾 SAVING ANALYSIS RESULTS")
    print("=" * 50)
    
    # Save summary statistics
    summary_stats = {
        'Metric': ['Total Publications', 'Average Citations', 'Year Range'],
        'Global_South': [
            len(gs_data),
            gs_data['citations'].mean() if 'citations' in gs_data.columns else 'N/A',
            f"{gs_data['year'].min()}-{gs_data['year'].max()}" if 'year' in gs_data.columns else 'N/A'
        ],
        'Global_North': [
            len(gn_data),
            gn_data['citations'].mean() if 'citations' in gn_data.columns else 'N/A',
            f"{gn_data['year'].min()}-{gn_data['year'].max()}" if 'year' in gn_data.columns else 'N/A'
        ]
    }
    
    summary_df = pd.DataFrame(summary_stats)
    summary_df.to_csv('results/tables/summary_statistics.csv', index=False)
    print("✅ Saved: summary_statistics.csv")
    
    # Save sample of processed data
    gs_data.head(20).to_csv('results/tables/gs_data_sample.csv', index=False)
    gn_data.head(20).to_csv('results/tables/gn_data_sample.csv', index=False)
    print("✅ Saved sample data tables")

def generate_report(gs_data, gn_data, data_source):
    """Generate a simple text report"""
    print("\n📝 GENERATING ANALYSIS REPORT")
    print("=" * 50)
    
    report_content = f"""
COLONIALITY ANALYSIS PROJECT - REPORT
Generated on: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}
Data Source: {data_source}

DATASET OVERVIEW:
- Global South publications: {len(gs_data)}
- Global North publications: {len(gn_data)}
- Total publications analyzed: {len(gs_data) + len(gn_data)}

KEY FINDINGS:
1. Dataset successfully loaded and analyzed
2. Basic comparative analysis completed
3. Visualizations generated in results/graphics/
4. Summary tables saved in results/tables/

NEXT STEPS:
- Conduct advanced statistical analysis
- Perform topic modeling on publication titles
- Analyze collaboration patterns
- Examine citation networks

---
This is an automated report from the Coloniality Analysis Project.
    """
    
    with open('results/reports/analysis_report.txt', 'w') as f:
        f.write(report_content)
    
    print("✅ Generated: analysis_report.txt")

def main():
    """Main analysis function"""
    print("=" * 60)
    print("🎯 COLONIALITY ANALYSIS PROJECT - MAIN ANALYSIS")
    print("=" * 60)
    
    # Setup directories
    setup_directories()
    
    # Data source selection
    print("\nChoose data source:")
    print("1. Sample data (from repository - for testing)")
    print("2. Original data (local path - for real analysis)")
    
    try:
        choice = input("Enter choice (1 or 2): ").strip()
        use_sample_data = (choice == "1")
    except:
        use_sample_data = True  # Default to sample data
        print("Using sample data by default")
    
    # Load data
    gs_data, gn_data, data_source = load_data(use_sample_data)
    
    if gs_data is None or gn_data is None:
        print("❌ Failed to load data. Exiting.")
        return
    
    # Perform analyses
    basic_descriptive_analysis(gs_data, gn_data, data_source)
    create_visualizations(gs_data, gn_data, data_source)
    save_analysis_results(gs_data, gn_data, data_source)
    generate_report(gs_data, gn_data, data_source)
    
    # Final summary
    print("\n" + "=" * 60)
    print("🎉 ANALYSIS COMPLETED SUCCESSFULLY!")
    print("=" * 60)
    print("\n📁 Output files created:")
    print("   📊 Graphics: results/graphics/")
    print("   📋 Tables: results/tables/") 
    print("   📝 Reports: results/reports/")
    print(f"\n💡 Data used: {data_source} dataset")
    print("\nNext: Check the generated files and modify the analysis as needed!")

if __name__ == "__main__":
    main()
