# Molecular Dynamics Simulation for Protein-Ligand Stability

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/USERNAME/REPO/blob/main/gig1-drug-discovery-docking/project2-md-simulation-gromacs/notebook.ipynb)

Manual colab access: 


https://colab.research.google.com/drive/18YW8A7IH9F-k0epl9noOGYuSCOxmygh7#scrollTo=ToeCZ9OlDUOW

## Problem
Docking shows how strongly a ligand binds, but not whether it stays bound over time. Molecular Dynamics (MD) simulation tracks atom movement and checks if the complex is stable.

## Approach
1. Build protein and ligand input files with CHARMM-GUI (GROMACS output)
2. Equilibrate the system (solvation, ions, energy minimization)
3. Run the production MD simulation
4. Calculate RMSD and plot it to judge stability

## Tools
Python, GROMACS, CHARMM-GUI, MDAnalysis, Matplotlib

## Results
RMSD plot of the protein-ligand complex. A flat curve means a stable complex (add your real plot here).

## Notes
Write the simulation length (ns), the protein and ligand names, and the GPU you used.

## How to run
1. Click the "Open in Colab" badge.
2. Choose Runtime > Change runtime type > GPU (if needed).
3. Click Runtime > Run all.
