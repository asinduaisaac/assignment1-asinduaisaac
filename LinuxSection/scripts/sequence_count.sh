#!/bin/bash

# folder where the fasta files live
dir="../data/processed/genomic_data"

# loop through every .fa file in that folder
for file in "$dir"/*.fa; do

    # count how many lines start with '>' — each one marks a new sequence
    count=$(grep -c "^>" "$file")

    # print the filename (without its folder path) and the count, separated by a tab
    printf "%s\t%s\n" "$(basename "$file")" "$count"

done