# Cross-Lingual Genomic RAG: English to Bengali Search and Translation

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/USERNAME/REPO/blob/main/gig2-genomic-rag-biomedical-nlp/project4-cross-lingual-genomic-rag/notebook.ipynb)

## Problem
Most genetics data is in English, but many people and doctors in South Asia need it in Bengali. This project lets a user search in Bengali or English, finds matching genetic variants with semantic search, and explains the result in simple Bengali.

## Approach
1. Load a multilingual embedding model (LaBSE)
2. Index the variant database with embeddings and Bengali translations
3. Search by meaning: Bengali query to English variant data
4. Translate and summarize the results into Bengali with an LLM
5. Check translation quality of genetic terms

## Tools
Python, LaBSE (Sentence-Transformers), ChromaDB or FAISS, LLM API

## Results
Example Bengali queries with matching variants and Bengali explanations (add your real outputs here).

## Notes
Write the real number of variants indexed (write 50,000+ only if you really did) and how translation quality was checked (for example a manual review of a sample).

## How to run
1. Click the "Open in Colab" badge.
2. Choose Runtime > Change runtime type > GPU (if needed).
3. Click Runtime > Run all.
