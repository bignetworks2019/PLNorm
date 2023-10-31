# PLNorm
This repository hosts a Python-based tool designed to normalize single-cell Hi-C data efficiently. It is tailored to handle various genome types and utilize the power law behavior existing in scHi-C data.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Adding New Genomes](#adding-new-genomes)

## Prerequisites

The script requires the following to be installed:
- Python (3.x)
- NumPy

## Installation
To use this tool, clone the repository to your local machine using the following command:

## Usage
Run the script from the command line by providing the genome type, input directory path, and output directory path. Optionally, a suffix for the output files can be specified.

### Input format
Note that we should have a bunch of cell contact matrix files as the input for this algorithm, and they should be squared matrices in text format.

### Command syntax
python PLNorm.py --genome_type <GENOME_TYPE> --input_base_dir <INPUT_DIR> --output_base_dir <OUTPUT_DIR> [--output_suffix <SUFFIX>]

### Parameters
- --genome_type: Type of genome (e.g., hg19, mm9) which determines the chromosomes to process.
- --input_base_dir: Directory containing the input chromosome files.
- --output_base_dir: Directory where normalized chromosome files will be saved.
- --output_suffix: (Optional) Suffix to append to output filenames.

## Examples
To normalize single-cell Hi-C data for the hg19 human genome without a custom suffix:
python PLNorm.py --genome_type hg19 --input_base_dir /path/to/input --output_base_dir /path/to/output

To add a custom suffix _norm to the output filenames:
python PLNorm.py --genome_type hg19 --input_base_dir /path/to/input --output_base_dir /path/to/output --output_suffix _norm

### Example data
To run PLNorm on the example data provided in the "/data" folder, we can start with:
python PLNorm.py --genome_type hg19 --input_base_dir /data --output_base_dir /example_output

## Adding New Genomes
To add support for a new genome, edit the genome_chromosomes dictionary within the script to include a new key for the genome type and its list of chromosomes as the value.

