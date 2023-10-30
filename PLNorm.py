import numpy as np
import os
import sys
import glob
import argparse

# Predefined chromosome lists for different genome types
genome_chromosomes = {
    'hg19': ["chr1", "chr2", "chr3", "chr4", "chr5", "chr6", "chr7", "chr8", "chr9", "chr10",
             "chr11", "chr12", "chr13", "chr14", "chr15", "chr16", "chr17", "chr18", "chr19", 
             "chr20", "chr21", "chr22", "chrX"],
    'mm9': ["chr1", "chr2", "chr3", "chr4", "chr5", "chr6", "chr7", "chr8", "chr9", "chr10",
            "chr11", "chr12", "chr13", "chr14", "chr15", "chr16", "chr17", "chr18", "chr19", "chrX"],
    # Add more genome types with corresponding chromosomes here...
}

def normalize_chromosome(file_path, output_folder, output_suffix):
    mt = np.loadtxt(file_path)
    mt_new = np.triu(mt, k=1) + np.diag(np.diag(mt) / 2)
    sum_per_column = np.sum(mt_new, axis=0)
    log_sum = np.log2(sum_per_column + 1)
    total_sum = np.sum(log_sum)
    
    mt_norm = mt_new if total_sum == 0 else mt_new * (mt_new.shape[0] / total_sum)
    mt_norm = mt_norm + np.transpose(np.triu(mt_norm, k=1))

    base_name = os.path.basename(file_path)
    name_part, ext_part = os.path.splitext(base_name)
    output_file_name = f"{name_part}{output_suffix}{ext_part}"
    output_file = os.path.join(output_folder, output_file_name)
    np.savetxt(output_file, mt_norm)

def process_chromosomes(input_base_dir, output_base_dir, chromosomes, output_suffix):
    for chrom in chromosomes:
        input_dir = os.path.join(input_base_dir, chrom)
        output_dir = os.path.join(output_base_dir, chrom)
        os.makedirs(output_dir, exist_ok=True)
        
        for file_path in glob.glob(os.path.join(input_dir, '*')):
            print(f"Normalizing file: {file_path}")
            normalize_chromosome(file_path, output_dir, output_suffix)

def main(genome_type, input_base_dir, output_base_dir, output_suffix):
    chromosomes = genome_chromosomes.get(genome_type)
    if not chromosomes:
        raise ValueError(f"Genome type '{genome_type}' is not recognized. Please add it to the 'genome_chromosomes' dictionary.")
    
    process_chromosomes(input_base_dir, output_base_dir, chromosomes, output_suffix)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Normalize single-cell Hi-C data for specified genome type.')
    parser.add_argument('-g', '--genome_type', required=True, choices=genome_chromosomes.keys(), help='Genome type (e.g., "hg19", "mm9").')
    parser.add_argument('-i', '--input_base_dir', required=True, help='Base input directory containing chromosome folders with files to be normalized.')
    parser.add_argument('-o', '--output_base_dir', required=True, help='Base output directory for the normalized chromosome folders and files.')
    parser.add_argument('-s', '--output_suffix', default='_PLNorm', help='Optional suffix to append to output filenames (default is "_PLNorm").')
    
    args = parser.parse_args()
    main(args.genome_type, args.input_base_dir, args.output_base_dir, args.output_suffix)
