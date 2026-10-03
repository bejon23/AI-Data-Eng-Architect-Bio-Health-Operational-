# ADMET Prediction Pipeline for FDA-Approved Drugs with DeepChem

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/USERNAME/REPO/blob/main/gig1-drug-discovery-docking/project4-admet-deepchem/notebook.ipynb)

## Problem
A drug must bind well and also be safe in the body. This project joins docking scores with AI-predicted toxicity so we can find drugs that bind strongly and have low toxicity risk.

## Approach
1. Install DeepChem and RDKit and load a toxicity dataset (Tox21)
2. Train a Graph Convolutional Network on molecular graphs
3. Merge docking scores with predicted toxicity for each drug
4. Plot a safety map (binding score vs toxicity score)

## Tools
Python, DeepChem, RDKit, Pandas, Seaborn

## Results
A table and scatter plot showing drugs with good binding and low toxicity (add your real outputs here).

## Notes
Write which dataset was used for training and which drugs have real docking scores.

## How to run
1. Click the "Open in Colab" badge.
2. Choose Runtime > Change runtime type > GPU (if needed).
3. Click Runtime > Run all.
