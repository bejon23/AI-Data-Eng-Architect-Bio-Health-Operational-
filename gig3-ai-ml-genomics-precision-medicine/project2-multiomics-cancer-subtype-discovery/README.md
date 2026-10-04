# Multi-Omics Integration with Transformers for Cancer Subtype Discovery

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/USERNAME/REPO/blob/main/gig3-ai-ml-genomics-precision-medicine/project2-multiomics-cancer-subtype-discovery/notebook.ipynb)


https://colab.research.google.com/drive/1z0djRh2jSKd5gOJDaObkqxNBoeQhyh-d


## Problem
Looking at only DNA or only RNA gives an incomplete picture of a cancer. This project combines genomic and single-cell transcriptomic data with transformer-based embeddings (DNABERT, scGPT) to find cancer subtypes.

## Approach
1. Load and normalize multi-omics data with Scanpy / AnnData
2. Create DNA embeddings (DNABERT) and RNA embeddings (scGPT)
3. Combine them in a transformer model with attention across omics
4. Cluster the combined embeddings (Leiden) and visualize with UMAP
5. Find marker genes for each subtype

## Tools
Python, Scanpy, AnnData, DNABERT, scGPT, PyTorch

## Results
UMAP of discovered subtypes and marker gene tables (add your real plots here).

## Notes
Write the exact dataset used and its size. If you use a small public dataset for the demo, say so clearly. Replace placeholder model classes with working code.

## How to run
1. Click the "Open in Colab" badge.
2. Choose Runtime > Change runtime type > GPU (if needed).
3. Click Runtime > Run all.
