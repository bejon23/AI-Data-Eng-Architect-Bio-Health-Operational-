# Federated Learning for Rare Disease Genomics Across 5 Hospitals

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/USERNAME/REPO/blob/main/gig3-ai-ml-genomics-precision-medicine/project5-federated-learning-rare-disease/notebook.ipynb)

## Problem
Rare disease data is small and spread across hospitals, and privacy rules stop it from being moved to one server. This project simulates 5 hospitals that train a model locally and share only model weights, which a central server averages (FedAvg).

## Approach
1. Set up the federated environment with TensorFlow Federated
2. Split the data into 5 simulated hospital datasets
3. Train locally at each hospital
4. Combine the updates with Federated Averaging into a global model
5. Evaluate on a test set and compare with a centralized model

## Tools
Python, TensorFlow Federated, TensorFlow, Pandas

## Results
Global model accuracy per round and comparison with centralized training (add your real outputs here).

## Notes
Say clearly that the 5 hospitals are simulated from a public or synthetic dataset. Federated learning keeps raw data local but does not by itself guarantee privacy, so do not claim full privacy unless you add methods such as differential privacy.

## How to run
1. Click the "Open in Colab" badge.
2. Choose Runtime > Change runtime type > GPU (if needed).
3. Click Runtime > Run all.
