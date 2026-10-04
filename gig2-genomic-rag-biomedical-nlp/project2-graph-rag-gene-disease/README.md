# Graph-RAG Pipeline for Gene-Disease Association Discovery

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/USERNAME/REPO/blob/main/gig2-genomic-rag-biomedical-nlp/project2-graph-rag-gene-disease/notebook.ipynb)

https://colab.research.google.com/drive/1gsfyG4zahL9ZneZYkDyudA3OhCosL1dQ



## Problem
Genes and diseases are connected like a network, but normal text search only matches words and misses these links. This project combines a graph database (Neo4j) for gene-disease relationships with a vector database (ChromaDB) for gene descriptions, and an LLM to write the final answer.

## Approach
1. Build a gene-disease graph in Neo4j
2. Store gene description embeddings in ChromaDB
3. For each question, find relationships in the graph
4. Retrieve matching descriptions from the vector database
5. Give both to an LLM to write a clear answer

## Tools
Python, Neo4j, ChromaDB, Sentence-Transformers, LLM API

## Results
Example questions with graph relationships and generated answers (add your real outputs and a graph screenshot here).

## Notes
Write where the gene-disease data came from, and how Neo4j was run (Neo4j Aura free instance or local). Never upload database passwords or API keys.

## How to run
1. Click the "Open in Colab" badge.
2. Choose Runtime > Change runtime type > GPU (if needed).
3. Click Runtime > Run all.
