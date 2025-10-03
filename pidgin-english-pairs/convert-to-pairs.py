#!/usr/bin/env python3
"""
Convert Cleaned Pidgin-English Data to Simple Pairs Format
Converts pidgin-english-data-cleaned.txt to simple line-by-line pairs:
Each line: "pidgin-text [TAB][TAB] english-text"
No metadata, headers, or separators.
"""

import os

def convert_to_pairs():
    """Convert cleaned pidgin-english data to simple pairs format"""
    
    input_file = "pidgin-english-data-cleaned.txt"
    output_file = "pidgin-english-pairs.txt"
    
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found")
        return
    
    print("Converting to Simple Pairs Format")
    print("=" * 35)
    print(f"Input file: {input_file}")
    print(f"Output file: {output_file}")
    
    pairs_written = 0
    current_eng = None
    current_pcm = None
    
    try:
        with open(input_file, 'r', encoding='utf-8') as infile, \
             open(output_file, 'w', encoding='utf-8') as outfile:
            
            for line_num, line in enumerate(infile, 1):
                line = line.strip()
                
                # Skip empty lines, headers, and separators
                if not line or line.startswith('#') or line.startswith('-') or line.startswith('Record'):
                    continue
                
                # Process eng: and pcm: lines
                if line.startswith('eng:'):
                    current_eng = line[4:].strip()  # Remove 'eng:' prefix
                elif line.startswith('pcm:'):
                    current_pcm = line[4:].strip()  # Remove 'pcm:' prefix
                    
                    # When we have both eng and pcm, write the pair
                    if current_eng and current_pcm:
                        # Format: pidgin-text [TAB][TAB] english-text
                        outfile.write(f"{current_pcm}\t\t{current_eng}\n")
                        pairs_written += 1
                        
                        # Reset for next pair
                        current_eng = None
                        current_pcm = None
                
                # Progress indicator
                if line_num % 5000 == 0:
                    print(f"  Processed {line_num:,} lines...")
        
        print(f"\nConversion completed!")
        print(f"- Translation pairs written: {pairs_written:,}")
        
        # Show file sizes
        original_size = os.path.getsize(input_file)
        pairs_size = os.path.getsize(output_file)
        size_reduction = original_size - pairs_size
        reduction_percent = (size_reduction / original_size) * 100
        
        print(f"- Original file size: {original_size:,} bytes ({original_size/(1024*1024):.2f} MB)")
        print(f"- Pairs file size: {pairs_size:,} bytes ({pairs_size/(1024*1024):.2f} MB)")
        print(f"- Size reduction: {size_reduction:,} bytes ({reduction_percent:.1f}%)")
        
        # Show sample of pairs
        print(f"\nSample pairs (pidgin [TAB][TAB] english):")
        print("-" * 50)
        with open(output_file, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f):
                if i >= 5:  # Show first 5 pairs
                    break
                print(f"{i+1}: {line.rstrip()}")
        
    except Exception as e:
        print(f"Error processing file: {str(e)}")

if __name__ == "__main__":
    convert_to_pairs()
