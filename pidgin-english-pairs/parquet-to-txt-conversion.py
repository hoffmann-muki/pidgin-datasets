#!/usr/bin/env python3
"""
Parquet to Text File Converter
Extracts data from train-00000-of-00001.parquet and converts it to a readable .txt format
"""

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import os

def convert_parquet_to_txt():
    """Convert parquet file to text format"""
    
    # Input and output file paths
    parquet_file = "train-00000-of-00001.parquet"
    output_file = "pidgin-english-data.txt"
    
    if not os.path.exists(parquet_file):
        print(f"Error: {parquet_file} not found in current directory")
        return
    
    try:
        print(f"Reading parquet file: {parquet_file}")
        
        # Try reading with pyarrow first
        try:
            table = pq.read_table(parquet_file)
            df = table.to_pandas()
            print("Successfully read with PyArrow")
        except Exception as e:
            print(f"PyArrow failed: {e}")
            print("Trying with pandas...")
            # Fallback to pandas with different engines
            try:
                df = pd.read_parquet(parquet_file, engine='pyarrow')
            except:
                print("Trying with fastparquet engine...")
                df = pd.read_parquet(parquet_file, engine='fastparquet')
        
        print(f"Data shape: {df.shape}")
        print(f"Columns: {list(df.columns)}")
        print("\nFirst few rows:")
        print(df.head())
        
        # Display data types
        print(f"\nData types:")
        for col in df.columns:
            print(f"  {col}: {df[col].dtype}")
        
        # Write to text file
        print(f"\nConverting to text file: {output_file}")
        
        with open(output_file, 'w', encoding='utf-8') as f:
            # Write header information
            f.write("# Pidgin-English Pairs Dataset\n")
            f.write(f"# Total records: {len(df)}\n")
            f.write(f"# Columns: {', '.join(df.columns)}\n")
            f.write("# " + "="*50 + "\n\n")
            
            # Write data based on column structure
            for i, (idx, row) in enumerate(df.iterrows()):
                f.write(f"Record {i + 1}:\n")
                for col in df.columns:
                    # Handle potential encoding issues and null values
                    try:
                        cell_value = row[col]
                        # Convert to string and handle nulls
                        if cell_value is None or str(cell_value).lower() in ['nan', 'none', 'null']:
                            value = "[NULL]"
                        else:
                            value = str(cell_value).replace('\n', '\\n').replace('\r', '\\r')
                        f.write(f"  {col}: {value}\n")
                    except Exception as e:
                        f.write(f"  {col}: [ERROR: {str(e)}]\n")
                f.write("-" * 40 + "\n\n")
                
                # Progress indicator for large files
                if (i + 1) % 1000 == 0:
                    print(f"  Processed {i + 1} records...")
        
        print(f"Successfully converted {len(df)} records to {output_file}")
        
        # Display some statistics
        print(f"\nDataset Statistics:")
        print(f"- Total records: {len(df)}")
        print(f"- Columns: {len(df.columns)}")
        for col in df.columns:
            if df[col].dtype == 'object':
                avg_length = df[col].astype(str).str.len().mean()
                print(f"- Average {col} length: {avg_length:.1f} characters")
                
                # Show some example values
                print(f"- Sample {col} values:")
                sample_values = df[col].dropna().head(3).tolist()
                for j, val in enumerate(sample_values):
                    print(f"  {j+1}. {val}")
        
    except Exception as e:
        print(f"Error converting file: {str(e)}")
        print(f"Error type: {type(e).__name__}")
        
        # Try to get file info
        try:
            file_size = os.path.getsize(parquet_file)
            print(f"File size: {file_size} bytes ({file_size / (1024*1024):.2f} MB)")
        except:
            pass

if __name__ == "__main__":
    print("Parquet to Text Converter")
    print("=" * 30)
    convert_parquet_to_txt()
