# PLNorm
This repository hosts a Python-based command-line tool designed to normalize single-cell Hi-C data efficiently. It is tailored to handle various genome types and accommodates a range of chromosome numbers and file naming conventions.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Adding New Genomes](#adding-new-genomes)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

The script requires the following to be installed:
- Python (3.x)
- NumPy

## Usage
Run the script from the command line by providing the genome type, input directory path, and output directory path. Optionally, a suffix for the output files can be specified.

### Command syntax
python normalize_scHiC.py --genome_type <GENOME_TYPE> --input_base_dir <INPUT_DIR> --output_base_dir <OUTPUT_DIR> [--output_suffix <SUFFIX>]

### Parameters
- --genome_type: Type of genome (e.g., hg19, mm9) which determines the chromosomes to process.
- --input_base_dir: Directory containing the input chromosome files.
- --output_base_dir: Directory where normalized chromosome files will be saved.
- --output_suffix: (Optional) Suffix to append to output filenames.
