# AlphaFold2 + ESM-2 for BRCA1/BRCA2 Variant Effect Prediction

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/USERNAME/REPO/blob/main/gig3-ai-ml-genomics-precision-medicine/project1-alphafold2-esm2-brca-variant-effect/notebook.ipynb)

## Problem
Mutations in BRCA1 and BRCA2 raise breast cancer risk, but among thousands of variants it is hard to know which ones damage protein structure and cause disease. This project combines 3D structure (AlphaFold2), sequence embeddings (ESM-2) and a stability score to predict if a variant is pathogenic or benign.

## Approach
1. Predict the 3D structure of the wild-type and mutant protein (AlphaFold2 / ColabFold) and read pLDDT confidence
2. Create sequence embeddings with ESM-2 at the mutation position
3. Estimate the stability change (ddG) with a tool such as FoldX or Rosetta
4. Combine structure, sequence and stability features and train a classifier (Random Forest or MLP) on labeled variants (for example ClinVar)
5. Highlight the mutation site in 3D (NGLView) and print a short report

## Tools
Python, ColabFold / AlphaFold2, ESM-2 (fair-esm), scikit-learn, NGLView, Matplotlib

## Results
Pathogenic or benign prediction for example variants, a pLDDT plot with the mutation site, and a 3D view (add your real outputs here).

## Notes
Use real labeled variants for training and report real metrics (accuracy, AUC) on a held-out test set. Do not use hard-coded example values for pLDDT or ddG in the final notebook.

## How to run
1. Click the "Open in Colab" badge.
2. Choose Runtime > Change runtime type > GPU (if needed).
3. Click Runtime > Run all.
