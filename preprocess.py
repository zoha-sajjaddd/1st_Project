import pandas as pd
import numpy as np
import os

def assign_grade(total):
    """Maps total marks to letter grades for rows missing a grade."""
    if pd.isna(total):
        return 'C' # Fallback default
    if total >= 450: return 'A'
    elif total >= 400: return 'B'
    elif total >= 350: return 'C'
    elif total >= 300: return 'D'
    else: return 'F'

def clean_data(df):
    """Cleans data, ensures a grade column exists, and merges additional_data.csv."""
    numeric_cols = [
        'stu_hours', 'attendance', 'eng', 'isl', 
        'maths', 'statistics', 'linear_algebra', 'total_marks'
    ]
    
    for col in numeric_cols:
        if col in df.columns:
            numeric_series = pd.to_numeric(df[col], errors='coerce')
            median_val = numeric_series.median()
            df[col] = numeric_series.fillna(median_val)
            
    df = df.drop_duplicates()
    
    # CRITICAL FIX: Ensure ALL rows have a grade (fills NaN grades using total_marks)
    if 'grade' not in df.columns:
        df['grade'] = df['total_marks'].apply(assign_grade)
    else:
        df['grade'] = df['grade'].fillna(df['total_marks'].apply(assign_grade))

    # Merge the separate CSV file containing the high-grade ('A') examples
    if os.path.exists('additional_data.csv'):
        additional_df = pd.read_csv('additional_data.csv')
        df = pd.concat([df, additional_df], ignore_index=True)
        print("  ✔ Successfully merged 'additional_data.csv'")
    else:
        print("  ⚠ Warning: 'additional_data.csv' not found!")
        
    return df