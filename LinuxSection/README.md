# LinuxSection

This directory contains my work for Question 2 (the Linux/Bash section) of Assignment 1.

## Folder structure

- `data/raw/` — the original downloaded genomic_data.zip file, kept untouched
- `data/processed/genomic_data/` — files extracted from the zip (fasta, bed, fastq files)
- `results/` — final outputs from my scripts (e.g. all_sequence_headers.txt)
- `scripts/` — the bash scripts I wrote to process the data
- `README.md` — this file

## Commands used to set up the folder structure

\```bash
mkdir -p LinuxSection/data/raw
mkdir -p LinuxSection/data/processed
mkdir -p LinuxSection/results
mkdir -p LinuxSection/scripts
touch LinuxSection/README.md
touch LinuxSection/scripts/genomic_data.sh
touch LinuxSection/scripts/sequence_count.sh
touch LinuxSection/scripts/header_extractor.sh
\```

## Dependencies

- `unzip` must be installed on the system before running genomic_data.sh:
\```bash
sudo apt install unzip -y
\```
This is a one-time system setup step, not something any script installs automatically.

## Scripts

- **`scripts/genomic_data.sh`** — downloads `genomic_data.zip` from GitHub into `data/raw/`, extracts its contents into `data/processed/genomic_data/`, then prints the total number of files and the number of fasta files in that folder.
- **`scripts/sequence_count.sh`** — loops through every fasta file in `data/processed/genomic_data/` and counts how many sequences (lines starting with `>`) each one contains, printing the filename and count separated by a tab.
- **`scripts/header_extractor.sh`** — loops through every fasta file and extracts all sequence header lines (lines starting with `>`), saving the combined output into `results/all_sequence_headers.txt`.

## How to run everything

All scripts are run from inside the `scripts/` folder, in this order:

\```bash
cd LinuxSection/scripts
bash genomic_data.sh
bash sequence_count.sh
bash header_extractor.sh
\```

## Results summary

- Number of files in genomic_data: 6
- Number of fasta files in genomic_data: 4
- Sequence counts: gch1s-metazoan.fa (9), nrf1_seq.fa (100), Pfb_seq.fa (114), sample.fa (4)
- Total headers extracted to all_sequence_headers.txt: 227
