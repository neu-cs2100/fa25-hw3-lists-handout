"""
data_loader.py
Module responsible for loading and basic exploration of 311 cases dataset.
Follows single responsibility principle: handles data input and initial exploration.
"""

import pandas as pd
import numpy as np

def load_and_explore_data(filepath):
    """
    Load the 311 cases dataset and display basic information.
    
    Args:
        filepath (str): Path to the CSV file
        
    Returns:
        pd.DataFrame: Loaded dataset
        
    try:
        # Load the data
        df = pd.read_csv(filepath)
        
        # Validate that required columns exist
        required_columns = ['category', 'neighborhood', 'days_open', 'latitude', 'longitude']
        missing_columns = [col for col in required_columns if col not in df.columns]
        
        if missing_columns:
            print(f"Warning: Missing expected columns: {missing_columns}")
            print(f"Available columns: {list(df.columns)}")
        
        # Display basic information
        print("Dataset Overview:")
        print(f"Shape: {df.shape}")
        print(f"Columns: {list(df.columns)}")
        print("\nFirst few rows:")
        print(df.head())
        print("\nData types:")
        print(df.dtypes)
        print("\nMissing values:")
        print(df.isnull().sum())
        
        # Basic statistics for numeric columns
        print("\nBasic statistics:")
        print(df.describe())
        
        return df
        
    except FileNotFoundError as e:
        print(f"Error: Could not find file '{filepath}'")
        raise e
    except pd.errors.EmptyDataError as e:
        print("Error: The file appears to be empty")
        raise e
    except pd.errors.ParserError as e:
        print("Error: Could not parse the file. Check if it's a valid CSV.")
        raise e
    """
    pass
    
    # Add category-specific summaries if columns exist (Keeping this as starter code for now, let me know if it should be removed)
    
    summary = []
    
    if 'category' in df.columns: #df not defined error, will be fixed when students load data
        summary['category_counts'] = df['category'].value_counts().to_dict()
    
    if 'neighborhood' in df.columns:
        summary['neighborhood_counts'] = df['neighborhood'].value_counts().to_dict()
    
    if 'days_open' in df.columns:
        summary['days_open_stats'] = {
            'mean': df['days_open'].mean(),
            'median': df['days_open'].median(),
            'std': df['days_open'].std(),
            'min': df['days_open'].min(),
            'max': df['days_open'].max()
        }
    
    return summary