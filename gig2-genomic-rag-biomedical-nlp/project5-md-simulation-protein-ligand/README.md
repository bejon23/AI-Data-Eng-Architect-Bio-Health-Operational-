# Molecular Dynamics Simulation for Protein-Ligand Structural Stability

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/USERNAME/REPO/blob/main/gig2-genomic-rag-biomedical-nlp/project5-md-simulation-protein-ligand/notebook.ipynb)


https://colab.research.google.com/drive/1ZayDWyFhdT_ov0JWXuI40gIdqnhQZ2HQ

## Problem
Docking shows how strongly a ligand binds, but not whether it stays bound over time. MD simulation tracks atom movement to check if the best docked compounds are really stable, so lab time is not wasted on weak candidates.

## Approach
1. Generate topology and a simulation box with GROMACS
2. Add water and ions (solvation and ionization)
3. Run energy minimization
4. Run the production MD simulation
5. Calculate RMSD and plot it to check stability

## Tools
Python, GROMACS, Matplotlib, MDAnalysis

## Results
RMSD plot of the complex. A flat curve means a stable complex (add your real plot here).

## Notes
Write the simulation length (ns), the protein and ligand names, and the GPU used. This project is related to Gig 1 Project 2, so link to it or use a different protein-ligand pair.

## How to run
1. Click the "Open in Colab" badge.
2. Choose Runtime > Change runtime type > GPU (if needed).
3. Click Runtime > Run all.
