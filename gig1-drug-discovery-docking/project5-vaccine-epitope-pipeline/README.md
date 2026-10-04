# Epitope-Based Vaccine Candidate Selection Pipeline

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/USERNAME/REPO/blob/main/gig1-drug-discovery-docking/project5-vaccine-epitope-pipeline/notebook.ipynb)


https://colab.research.google.com/drive/1be6dZed4osewZGFb9yuFJUCouYKHFSm5

## Problem
A good vaccine needs peptides (epitopes) that bind HLA strongly, are not allergenic, and are not toxic. Checking this in the lab is slow and costly. This project builds a computer pipeline to shortlist safe and effective epitopes.

## Approach
1. Load the protein sequence (UniProt)
2. Split the sequence into peptide windows
3. Filter candidates by binding, allergenicity and toxicity
4. Join the best epitopes with linkers into a vaccine construct
5. Predict the 3D structure with ColabFold and check receptor docking

## Tools
Python, Biopython, Pandas, ColabFold, Seaborn

## Results
A ranked list of vaccine epitope candidates and a predicted 3D structure (add your real outputs here).

## Notes
Say clearly which steps use real tools and which steps are demo or simulated. Replace dummy filters and random docking scores with real tools (for example IEDB, AllerTOP, ToxinPred, HDOCK) before presenting results as real.

## How to run
1. Click the "Open in Colab" badge.
2. Choose Runtime > Change runtime type > GPU (if needed).
3. Click Runtime > Run all.
