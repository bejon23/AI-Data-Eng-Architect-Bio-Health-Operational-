# Clinical Decision Support RAG with PubMedBERT and SNOMED-CT

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/USERNAME/REPO/blob/main/gig2-genomic-rag-biomedical-nlp/project3-clinical-decision-support-rag/notebook.ipynb)


https://colab.research.google.com/drive/1iSKak6uSr81yvC1gzq8govY7iHZKsAvJ


## Problem
Doctors cannot easily search thousands of medical papers for the right evidence. This project builds an API that takes patient symptoms, maps them to standard medical concepts, retrieves related evidence, and returns an evidence-based suggestion.

## Approach
1. Map symptoms to standard medical concepts (SNOMED CT or a free alternative)
2. Create embeddings with a biomedical model (PubMedBERT)
3. Retrieve relevant evidence from a vector database
4. Generate a short answer from the evidence with an LLM
5. Serve the pipeline with FastAPI
6. Validate the output against guidelines

## Tools
Python, Transformers (PubMedBERT), FastAPI, ChromaDB

## Results
Example symptom inputs and the returned evidence-based suggestions (add your real outputs here).

## Notes
This is an educational demo and NOT medical advice. SNOMED CT needs a licence for full use, so write which concept source you really used. Replace any placeholder functions with working code and report a real validation score.

## How to run
1. Click the "Open in Colab" badge.
2. Choose Runtime > Change runtime type > GPU (if needed).
3. Click Runtime > Run all.
