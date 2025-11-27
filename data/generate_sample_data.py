"""
Generate sample data for Coloniality Analysis Project
"""
import pandas as pd
import numpy as np
import os

def create_sample_gs_data():
    """Create sample Google Scholar research data"""
    np.random.seed(42)
    
    sample_data = {
        'author': ['Smith, J', 'Johnson, M', 'Garcia, L', 'Lee, K', 'Wang, Y'] * 20,
        'title': [f'Research on Coloniality Study {i}' for i in range(100)],
        'year': np.random.randint(2010, 2023, 100),
        'citations': np.random.randint(0, 150, 100),
        'country': ['USA', 'UK', 'Indonesia', 'Netherlands', 'Brazil'] * 20,
        'field': ['Social Sciences', 'Humanities', 'Education', 'Political Science'] * 25,
        'publication': [f'Journal of {field} {i%5}' for i, field in enumerate(['Social Sciences', 'Humanities', 'Education', 'Political Science'] * 25)]
    }
    
    df = pd.DataFrame(sample_data)
    df.to_csv('data/sample_gs_research.csv', index=False)
    print("✅ Created sample_gs_research.csv with 100 records")
    return df

def create_sample_gn_data():
    """Create sample Global North WoS/Scopus data"""
    np.random.seed(42)
    
    sample_data = {
        'document_id': [f'DOC_{i:04d}' for i in range(100)],
        'title': [f'Global North Research {i}' for i in range(100)],
        'year': np.random.randint(2010, 2023, 100),
        'citations': np.random.randint(0, 100, 100),
        'field': ['Social Sciences', 'Humanities', 'STEM', 'Medical'] * 25,
        'region': ['North America', 'Europe', 'East Asia', 'Oceania'] * 25,
        'journal_quartile': ['Q1', 'Q2', 'Q3', 'Q4'] * 25
    }
    
    df = pd.DataFrame(sample_data)
    df.to_csv('data/sample_gn_wos_scopus.csv', index=False)
    print("✅ Created sample_gn_wos_scopus.csv with 100 records")
    return df

if __name__ == "__main__":
    print("🚀 Generating sample data for Coloniality Analysis...")
    create_sample_gs_data()
    create_sample_gn_data()
    print("🎉 Sample data generation completed!")
    print("📁 Files created in 'data/' folder:")
    print("   - sample_gs_research.csv")
    print("   - sample_gn_wos_scopus.csv")
