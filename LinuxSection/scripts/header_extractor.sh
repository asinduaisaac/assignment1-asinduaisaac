#!/bin/bash

# folder where the fasta files live
dir="../data/processed/genomic_data"

# where the combined header output will be saved
output_file="../results/all_sequence_headers.txt"

# start with a clean output file, so old runs don't leave duplicate headers behind
> "$output_file"

# loop through every .fa file in that folder
for file in "$dir"/*.fa; do

    # extract lines starting with '>' (the headers) and append them to the output file
    grep "^>" "$file" >> "$output_file"

done