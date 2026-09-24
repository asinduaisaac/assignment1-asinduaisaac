#!/bin/bash

# download the zip file
wget -O ../data/raw/genomic_data.zip https://github.com/kipkurui/Intro2Linux2019/raw/master/Data/genomic_data.zip

# extract contents into processed/
unzip -o ../data/raw/genomic_data.zip -d ../data/processed

# count all files in genomic_data
echo "Number of files in genomic_data:"
find ../data/processed/genomic_data -maxdepth 1 -type f | wc -l

# count fasta files in genomic_data
echo "Number of fasta files in genomic_data:"
find ../data/processed/genomic_data -maxdepth 1 -type f -iname "*.fa" | wc -l