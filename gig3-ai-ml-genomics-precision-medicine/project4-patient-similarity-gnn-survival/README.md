# Patient Similarity Network and Survival Prediction with Graph Neural Networks

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/USERNAME/REPO/blob/main/gig3-ai-ml-genomics-precision-medicine/project4-patient-similarity-gnn-survival/notebook.ipynb)

## Problem
Every cancer patient is biologically different, so predicting survival is hard. This project connects similar TCGA patients in a network and uses a Graph Neural Network to learn from neighbours and predict personalized survival.

## Approach
1. Load TCGA clinical and expression features
2. Build a patient similarity graph (for example k-nearest neighbours)
3. Design a GCN with PyTorch Geometric
4. Train with a survival-aware loss (for example Cox loss) or a risk classification target
5. Evaluate with concordance index and visualize the patient network

## Tools
Python, PyTorch Geometric, NetworkX, lifelines, scikit-learn

## Results
Concordance index, training curves and a patient network map (add your real outputs here).

## Notes
Write the TCGA cancer type and number of patients. Use a real survival loss and metric. A single GCN layer alone is not enough for survival prediction. Make sure no test patients leak into training.

## How to run
1. Click the "Open in Colab" badge.
2. Choose Runtime > Change runtime type > GPU (if needed).
3. Click Runtime > Run all.
