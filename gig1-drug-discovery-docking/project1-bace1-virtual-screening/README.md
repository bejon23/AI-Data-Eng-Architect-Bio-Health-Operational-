# Virtual Screening of Natural Products Against Alzheimer's BACE1

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/USERNAME/REPO/blob/main/gig1-drug-discovery-docking/project1-bace1-virtual-screening/notebook.ipynb)

## Problem
Alzheimer's disease is linked to the enzyme BACE1. Testing thousands of natural compounds in a lab takes years. This project builds a computer filter that docks a compound library against BACE1 and ranks the best candidates.

## Approach
1. Prepare the BACE1 receptor and ligand library (SDF to PDBQT)
2. Dock every ligand with AutoDock Vina / AutoDock-GPU
3. Collect all binding energies into one table with Pandas
4. Plot the binding affinity distribution and pick top lead compounds

## Tools
Python, AutoDock Vina, Meeko, Open Babel, Pandas, Matplotlib

## Results
Top lead compounds with the lowest binding energy (add your real table and chart here).

## Notes
State the real number of ligands you docked (for example 50 or 100, not 10,000, unless you really ran 10,000).

## How to run
1. Click the "Open in Colab" badge.
2. Choose Runtime > Change runtime type > GPU (if needed).
3. Click Runtime > Run all.
