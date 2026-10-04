# Virtual Screening of Natural Products Against Alzheimer's BACE1

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/USERNAME/REPO/blob/main/gig1-drug-discovery-docking/project1-bace1-virtual-screening/notebook.ipynb)

Manually Colab access: 

https://colab.research.google.com/drive/1o-Lk__t9IGTlfoQDvYIq8E3oGKkwcwW-



## Problem
**Problem Statement**

Manual molecular docking remains one of the biggest bottlenecks in modern drug discovery and computational chemistry. Researchers and pharmaceutical teams still spend hours (or days) converting receptor and ligand files one by one, fixing format errors, cleaning PDBQT files, and running AutoDock Vina separately for every pair. This process is slow, error-prone, and nearly impossible to scale for larger virtual screening campaigns.

This project solves that problem completely. With a single Google Colab notebook, multiple receptors and ligands are automatically converted to clean PDBQT format, prepared for AutoDock Vina, docked in batch, and summarized with professional tables and visualizations — turning days of tedious work into minutes of automated results.

---

**Key Benefits**

- **Dramatically faster** — Run 3 receptors × 5 ligands (15 docking jobs) in one go instead of handling each pair manually.
- **Near-zero human error** — Automatic conversion, cleaning of problematic tags (MODEL, ROOT, BRANCH, etc.), and Vina-ready preparation eliminate common failures.
- **Beginner-friendly** — Fully runs in Google Colab. No local software installation or complex setup required.
- **Publication-ready outputs** — Generates clean affinity summary tables, heatmaps, ranking charts, and downloadable CSV/PNG files ready for reports or presentations.
- **Highly scalable** — Easily extend from a few molecules to dozens of receptors and hundreds of ligands with the same workflow.
- **Completely free & accessible** — No expensive software licenses. Ideal for students, academic labs, startups, and independent researchers.
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
