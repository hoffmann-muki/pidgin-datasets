#!/usr/bin/env python3
"""
Clean Pidgin References and Religious Terms
Cleans the pidgin-english-data.txt file by:
1. Removing biblical references and parenthetical content from ANYWHERE in both eng and pcm lines
2. Removing "Jehovah" and "Witness" from all lines
3. Removing leading non-alphabetic characters from all lines
4. Cleaning up extra spaces
"""

import re
import os

def clean_biblical_references(text):
    """
    Remove parenthetical references from anywhere in the text.
    This includes biblical references, study notes, and other citations.
    
    Examples:
    - "text ( Ps . 23:1 ) more text" -> "text more text"
    - "beginning ( Phil . 4 : 7 , ftn . ) end" -> "beginning end"
    - "start ( Check paragraph 17 ) continue" -> "start continue"
    - "incomplete ( Ps . at end" -> "incomplete at end"
    """
    # Remove complete parenthetical content (with closing parenthesis) from anywhere
    pattern_complete = r'\s*\([^)]*\)\s*'
    cleaned = re.sub(pattern_complete, ' ', text)
    
    # Remove incomplete parenthetical content (without closing parenthesis, typically at end)
    pattern_incomplete = r'\s*\([^)]*$'
    cleaned = re.sub(pattern_incomplete, '', cleaned)
    
    # Clean up multiple spaces
    cleaned = re.sub(r'\s+', ' ', cleaned)
    return cleaned.strip()

def remove_religious_terms(text):
    """Remove 'Jehovah' and 'Witness' from text"""
    # Remove "Jehovah" (case insensitive)
    text = re.sub(r'\bJehovah\b', '', text, flags=re.IGNORECASE)
    
    # Remove "Witness" and "Witnesses" (case insensitive)
    text = re.sub(r'\bWitnesses?\b', '', text, flags=re.IGNORECASE)
    
    return text

def remove_leading_non_alphabetic(text):
    """Remove all non-alphabetic characters and enumeration patterns from the beginning of text"""
    # Remove everything up to and including enumeration patterns like ( a ), ( b ), a ), b ), etc.
    text = re.sub(r'^.*?\(\s*[a-zA-Z]\s*\)\s*', '', text)  # Remove everything up to ( a ), ( b ), etc.
    text = re.sub(r'^[a-zA-Z]\s*\)\s*', '', text)  # Still handle standalone a ), b ), etc.
    
    # Then remove any remaining non-alphabetic characters from start
    text = re.sub(r'^[^A-Za-z]*', '', text)
    return text

def clean_extra_spaces(text):
    """Clean up extra spaces, commas, and punctuation issues"""
    # Replace multiple spaces with single space
    text = re.sub(r'\s+', ' ', text)
    
    # Fix spacing around punctuation
    text = re.sub(r'\s+([,.!?;:])', r'\1', text)  # Remove space before punctuation
    text = re.sub(r'([,.!?;:])\s+', r'\1 ', text)  # Single space after punctuation
    
    # Fix multiple commas or periods
    text = re.sub(r',+', ',', text)
    text = re.sub(r'\.+', '.', text)
    
    # Remove leading/trailing spaces and punctuation
    text = text.strip()
    
    # Remove orphaned punctuation at the beginning
    text = re.sub(r'^[,.\s]+', '', text)
    
    return text

def clean_pidgin_data():
    """Clean the pidgin-english-data.txt file"""
    
    input_file = "pidgin-english-data.txt"
    output_file = "pidgin-english-data-cleaned.txt"
    
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found")
        return
    
    print("Cleaning Pidgin-English Dataset")
    print("=" * 35)
    print(f"Input file: {input_file}")
    print(f"Output file: {output_file}")
    
    processed_lines = 0
    cleaned_reference_lines = 0
    cleaned_leading_chars = 0
    
    try:
        with open(input_file, 'r', encoding='utf-8') as infile, \
             open(output_file, 'w', encoding='utf-8') as outfile:
            
            for line_num, line in enumerate(infile, 1):
                original_line = line.rstrip()
                
                # Skip header lines and separators
                if line.startswith('#') or line.startswith('-') or not line.strip():
                    outfile.write(line)
                    continue
                
                # Process data lines
                if line.strip().startswith('eng:') or line.strip().startswith('pcm:'):
                    processed_lines += 1
                    
                    # Extract the prefix and content
                    if ':' in line:
                        prefix, content = line.split(':', 1)
                        content = content.strip()
                        
                        # Remove parenthetical references from both eng and pcm lines
                        content = clean_biblical_references(content)
                        if prefix.strip() in ['eng', 'pcm']:
                            cleaned_reference_lines += 1
                        
                        # Remove religious terms from all lines
                        content = remove_religious_terms(content)
                        
                        # Remove leading non-alphabetic characters from all lines
                        original_content = content
                        content = remove_leading_non_alphabetic(content)
                        if original_content != content:
                            cleaned_leading_chars += 1
                        
                        # Clean up extra spaces
                        content = clean_extra_spaces(content)
                        
                        # Write cleaned line
                        if content:  # Only write if there's content left
                            outfile.write(f"  {prefix.strip()}: {content}\n")
                        else:
                            outfile.write(f"  {prefix.strip()}: [CONTENT_REMOVED]\n")
                    else:
                        # Write line as-is if no colon found
                        outfile.write(line)
                else:
                    # Write non-data lines as-is
                    outfile.write(line)
                
                # Progress indicator
                if line_num % 5000 == 0:
                    print(f"  Processed {line_num:,} lines...")
    
        print(f"\nCleaning completed!")
        print(f"- Total lines processed: {processed_lines:,}")
        print(f"- Lines with references removed: {cleaned_reference_lines:,}")
        print(f"- Lines with leading chars removed: {cleaned_leading_chars:,}")
        
        # Show file sizes
        original_size = os.path.getsize(input_file)
        cleaned_size = os.path.getsize(output_file)
        size_reduction = original_size - cleaned_size
        reduction_percent = (size_reduction / original_size) * 100
        
        print(f"- Original file size: {original_size:,} bytes ({original_size/(1024*1024):.2f} MB)")
        print(f"- Cleaned file size: {cleaned_size:,} bytes ({cleaned_size/(1024*1024):.2f} MB)")
        print(f"- Size reduction: {size_reduction:,} bytes ({reduction_percent:.1f}%)")
        
        # Show sample of cleaned data
        print(f"\nSample of cleaned data:")
        print("-" * 40)
        with open(output_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            # Find first few data records
            data_lines = [line for line in lines if line.strip().startswith(('eng:', 'pcm:'))]
            for i, line in enumerate(data_lines[:6]):  # Show first 3 pairs
                print(line.rstrip())
                if i % 2 == 1:  # After every pcm line
                    print()
        
    except Exception as e:
        print(f"Error processing file: {str(e)}")

if __name__ == "__main__":
    clean_pidgin_data()
