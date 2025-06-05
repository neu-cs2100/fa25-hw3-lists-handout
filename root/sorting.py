"""
sorting.py
Module responsible for sorting 311 cases and managing urgency rankings.
Combines sorting and urgency functions as they work together conceptually.
"""

import pandas as pd
import numpy as np

def sort_by_days_open(df, ascending=False):
    """
    Sort the 311 cases by how long they were open.
    
    Args:
        df (pd.DataFrame): The 311 cases dataset
        ascending (bool): If True, sort from shortest to longest duration
        
    Returns:
        pd.DataFrame: Sorted dataset
        
    Raises:
        KeyError: If 'days_open' column doesn't exist
        ValueError: If days_open contains non-numeric values
    """
    
    # TODO: Sort the data
    
    pass

def create_urgency_ranking(df):
    """
    Create an urgency ranking system for 311 case categories.
    
    ETHICS QUESTION FOR STUDENTS: (Will add these in the summary file)
    How do you decide which issues are most "urgent"? 
    Consider factors like:
    - Public safety and health impacts
    - Economic consequences
    - Equity and access issues
    - Community impact and quality of life
    - Infrastructure and long-term effects
    
    Args:
        df (pd.DataFrame): The 311 cases dataset
        
    Returns:
        dict: Dictionary mapping categories to urgency scores (1 = most urgent, higher = less urgent)
    """
    if 'category' not in df.columns:
        print("Warning: 'category' column not found in dataset")
        return {}
    
    # Get all unique categories (Keeping this as starter code for now as well)
    categories = df['category'].unique()
    print("Available categories in your dataset:")
    print("-" * 40)
    for i, cat in enumerate(sorted(categories), 1):
        print(f"{i:2d}. {cat}")
    
    print(f"\nTotal categories: {len(categories)}")
    
    # TODO: Students should create their urgency ranking here
    # This is a placeholder - students should modify this based on their reasoning
    # Lower numbers = more urgent (1 is most urgent)
    # There are over 100 categories in this dataset, include at least 10 and rank them (giving your reasoning in the summary file)
    urgency_ranking = {
        # EXAMPLE (students should replace with their own reasoning):
        # 'Traffic Signal Repair': 1,           # Immediate safety risk
        # 'Street Defects': 2,                 # Safety and accessibility 
        # 'Blocked Bike Lane': 3,              # Safety and transportation
        # 'Street and Sidewalk Cleaning': 4,   # Quality of life
        #  And so on
        
        # TODO: Add rankings for stleast 10 categories found in your dataset
        # Use the list above to assign urgency scores (1-10 scale recommended), lower number = more urgent
    }
    
    return urgency_ranking

def filter_data(df, urgency_ranking):
    
    #TODO: Filter the dataset to include only the categories you have ranked.


def sort_by_urgency(df, urgency_ranking):
    """
    Sort 311 cases by urgency ranking.
    
    Args:
        df (pd.DataFrame): The 311 cases dataset
        urgency_ranking (dict): Dictionary mapping categories to urgency scores
        
    Returns:
        pd.DataFrame: Dataset sorted by urgency (most urgent first)
        
    Raises:
        ValueError: If urgency_ranking is empty
        KeyError: If 'category' column doesn't exist
    """
    if not urgency_ranking:
        raise ValueError("Urgency ranking dictionary is empty. Please complete create_urgency_ranking() first.")
        
    if 'category' not in df.columns:
        raise KeyError("Column 'category' not found in dataset")
    
    # TODO: Create a copy of the filtered dataset to avoid modifying original data
    
    # TODO: Add urgency score column based on your rankings
    
    # TODO: Sort by urgency (lower scores = more urgent), then by days open (longer first)
    
    pass