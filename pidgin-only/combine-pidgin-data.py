#!/usr/bin/env python3
"""
Combine Pidgin Train and Eval Data
Combines train.txt and eval.txt into a single pidgin-sentences.txt file.
Each line in the output file will be a single pidgin sentence.
"""

import os

def combine_pidgin_files():
    """Combine train.txt and eval.txt into pidgin-sentences.txt"""
    
    train_file = "train.txt"
    eval_file = "eval.txt"
    output_file = "pidgin-sentences.txt"
    
    # Check if input files exist
    if not os.path.exists(train_file):
        print(f"Error: {train_file} not found")
        return
    
    if not os.path.exists(eval_file):
        print(f"Error: {eval_file} not found")
        return
    
    print("Combining Pidgin Dataset Files")
    print("=" * 35)
    print(f"Input files: {train_file}, {eval_file}")
    print(f"Output file: {output_file}")
    
    total_lines = 0
    
    try:
        with open(output_file, 'w', encoding='utf-8') as outfile:
            # Process train.txt
            print(f"\nProcessing {train_file}...")
            with open(train_file, 'r', encoding='utf-8') as infile:
                lines_from_train = 0
                for line in infile:
                    line = line.strip()
                    if line:  # Skip empty lines
                        outfile.write(line + '\n')
                        lines_from_train += 1
                        total_lines += 1
                
                print(f"  Added {lines_from_train:,} lines from {train_file}")
            
            # Process eval.txt
            print(f"\nProcessing {eval_file}...")
            with open(eval_file, 'r', encoding='utf-8') as infile:
                lines_from_eval = 0
                for line in infile:
                    line = line.strip()
                    if line:  # Skip empty lines
                        outfile.write(line + '\n')
                        lines_from_eval += 1
                        total_lines += 1
                
                print(f"  Added {lines_from_eval:,} lines from {eval_file}")
        
        print(f"\nCombination completed!")
        print(f"- Total lines written: {total_lines:,}")
        
        # Show file size
        output_size = os.path.getsize(output_file)
        print(f"- Output file size: {output_size:,} bytes ({output_size/(1024*1024):.2f} MB)")
        
        # Show sample of combined data
        print(f"\nSample from combined file:")
        print("-" * 40)
        with open(output_file, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f):
                if i >= 5:  # Show first 5 lines
                    break
                print(f"{i+1}: {line.rstrip()}")
        
    except Exception as e:
        print(f"Error processing files: {str(e)}")

if __name__ == "__main__":
    combine_pidgin_files()
