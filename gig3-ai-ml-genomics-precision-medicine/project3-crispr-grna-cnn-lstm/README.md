# CRISPR Guide RNA On-Target vs Off-Target Prediction with CNN + LSTM

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/USERNAME/REPO/blob/main/gig3-ai-ml-genomics-precision-medicine/project3-crispr-grna-cnn-lstm/notebook.ipynb)



## Problem
Wrong-site edits (off-target effects) are a safety risk in CRISPR-Cas9 genome editing. This project trains a CNN + LSTM model on guide RNA sequences to predict on-target efficiency and off-target risk.

## Approach
1. Load and clean guide RNA data and one-hot encode the sequences
2. Build a hybrid CNN + LSTM model (CNN finds local motifs, LSTM captures long-range patterns)
3. Train and validate the model with a proper train/validation/test split
4. Predict the risk score for new guide sequences
5. Plot score distributions and model performance

## Tools
Python, TensorFlow / Keras, Pandas, Matplotlib

## Results
Training curves, test metrics and example gRNA risk scores (add your real outputs here).

## Notes
Write the real dataset name and size (only write 50,000 gRNAs if the data really has that many). Off-target datasets are often small and imbalanced, so report AUC and precision-recall, not only accuracy.

## How to run
1. Click the "Open in Colab" badge.
2. Choose Runtime > Change runtime type > GPU (if needed).
3. Click Runtime > Run all.
