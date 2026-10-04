# AI-Powered BRCA1 Variant Search Engine Using RAG

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/USERNAME/REPO/blob/main/gig2-genomic-rag-biomedical-nlp/project1-brca1-variant-search-rag/notebook.ipynb)


https://colab.research.google.com/drive/1gxno-yhnrwcBcTvXTwqtXN8imxmH3nJF

## Problem
Information about BRCA1 variants and cancer risk is scattered across many sources, so finding the right answer fast is hard. This project builds a search system where a user asks in plain English (for example, 'Which BRCA1 variants cause ovarian cancer?') and gets the most relevant variants and risk information.

## Approach
1. Install packages and prepare the BRCA1 variant data (for example from ClinVar)
2. Split text into chunks and create embeddings
3. Store embeddings in a Chroma vector database
4. Build the RAG search function (top-k search, metadata filtering)
5. Test different queries
6. Serve the search with FastAPI and save the database so it can be reloaded

## Tools
Python, ChromaDB, Sentence-Transformers, FastAPI, Pandas

## Results
Example queries and the top matching variants returned (add your real outputs and screenshots here).

## Notes
Write the data source, the number of variants indexed, and the embedding model used. This is a research and learning tool, not for clinical use.

## How to run
1. Click the "Open in Colab" badge.
2. Choose Runtime > Change runtime type > GPU (if needed).
3. Click Runtime > Run all.
