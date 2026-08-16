#!/usr/bin/env python3
import os
import sys

def merge_chunks(chunks_dir, output_file):
    """
    Deterministically merges all chunk*.md files in a directory into a single output file.
    Assumes files are named alphabetically/numerically in correct order, e.g., chunk1.md, chunk2.md
    """
    if not os.path.exists(chunks_dir):
        print(f"Error: Directory {chunks_dir} does not exist.")
        sys.exit(1)
        
    chunks = sorted([f for f in os.listdir(chunks_dir) if f.startswith('chunk') and f.endswith('.md')])
    if not chunks:
        print(f"Error: No chunk files found in {chunks_dir}.")
        sys.exit(1)
        
    print(f"Found {len(chunks)} chunks to merge.")
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for chunk in chunks:
            chunk_path = os.path.join(chunks_dir, chunk)
            with open(chunk_path, 'r', encoding='utf-8') as infile:
                outfile.write(infile.read())
                outfile.write("\n\n")
                
    print(f"Successfully concatenated chunks into {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python merge_chunks.py <path_to_chunks_dir> <output_file.md>")
        sys.exit(1)
    
    merge_chunks(sys.argv[1], sys.argv[2])
