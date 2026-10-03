# Drug-Resistance Mutation Analysis in HIV-1 Protease (Wild vs Mutant)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/USERNAME/REPO/blob/main/gig1-drug-discovery-docking/project3-fep-hiv-protease-resistance/notebook.ipynb)

## Problem
HIV-1 protease mutates quickly, and drugs stop working (drug resistance). This project compares drug binding to the wild-type protein and a mutant protein to see how much binding weakens.

## Approach
1. Pick the best protein-ligand pair from multi-docking (for example 1EVE with Warfarin)
2. Create a mutant protein in silico
3. Run the binding free energy workflow for the wild-type complex
4. Run the same workflow for the mutant complex and compare the difference

## Tools
Python, GROMACS, AutoDock Vina, Pandas, Matplotlib

## Results
Binding energy of wild type vs mutant and the difference between them (add your real values here).

## Notes
Write exactly which method you ran (full FEP, MM/PBSA, or docking plus MD). Do not call it FEP if you did not run FEP.

## How to run
1. Click the "Open in Colab" badge.
2. Choose Runtime > Change runtime type > GPU (if needed).
3. Click Runtime > Run all.
