# =======================
# PROJECT 4: Interactive Literature Map
# =======================
!pip install bertopic networkx pyvis plotly -q

import networkx as nx
import numpy as np
import pandas as pd
from pyvis.network import Network

# ============================================
# Cell 1: Build Citation Network
# ============================================
print("=== Cell 1: Citation Network ===")

# Mock citation data
citations_data = {
    'source': ['Paper_1', 'Paper_1', 'Paper_2', 'Paper_3', 'Paper_4', 'Paper_5'],
    'target': ['Paper_2', 'Paper_3', 'Paper_4', 'Paper_5', 'Paper_6', 'Paper_1'],
    'topic': ['CRISPR', 'Gene Therapy', 'Genomics', 'Proteomics', 'CRISPR', 'Genomics']
}
citations_df = pd.DataFrame(citations_data)

G = nx.from_pandas_edgelist(citations_df, 'source', 'target')
print(f"Citation network: {G.number_of_nodes()} papers, {G.number_of_edges()} citations")

# ============================================
# Cell 2: Topic Modeling (BERTopic)
# ============================================
print("\n=== Cell 2: Topic Modeling ===")

# Mock abstracts
abstracts = [
    "CRISPR-Cas9 gene editing for treating genetic disorders",
    "Gene therapy approaches for rare diseases",
    "Genomic sequencing technologies and applications",
    "Proteomics analysis in cancer research",
    "CRISPR applications in agriculture",
    "Genomics of complex diseases"
]

# Note: BERTopic needs more data; here we show the workflow
print(f"Processing {len(abstracts)} abstracts for topic modeling")
topics = [0, 1, 2, 3, 0, 2]  # Mock topic assignments
print(f"Topics identified: {set(topics)}")

# ============================================
# Cell 3: Gene-Phenotype Network
# ============================================
print("\n=== Cell 3: Gene-Phenotype Network ===")

gene_phenotype = {
    'gene': ['BRCA1', 'BRCA2', 'TP53', 'EGFR', 'KRAS', 'BRCA1'],
    'phenotype': ['Breast Cancer', 'Breast Cancer', 'Multiple Cancers',
                  'Lung Cancer', 'Colorectal Cancer', 'Ovarian Cancer']
}
gp_df = pd.DataFrame(gene_phenotype)

G_gp = nx.from_pandas_edgelist(gp_df, 'gene', 'phenotype')
print(f"Gene-Phenotype network: {G_gp.number_of_nodes()} nodes, {G_gp.number_of_edges()} edges")

# ============================================
# Cell 4: Interactive Visualization
# ============================================
print("\n=== Cell 4: Interactive Visualization ===")

net = Network(height="600px", width="100%", bgcolor="#222222", font_color="white")

# Add nodes
for node in G_gp.nodes():
    color = '#FF6B6B' if node.startswith(('BRCA', 'TP53', 'EGFR', 'KRAS')) else '#4ECDC4'
    net.add_node(node, label=node, color=color, size=25)

# Add edges
for edge in G_gp.edges():
    net.add_edge(edge[0], edge[1])

net.save_graph("literature_map.html")
print("Interactive map saved: literature_map.html")

# ============================================
# Cell 5: Analysis
# ============================================
print("\n=== Cell 5: Network Analysis ===")

# Find most connected genes
degree_dict = dict(G_gp.degree())
top_genes = sorted(degree_dict.items(), key=lambda x: x[1], reverse=True)[:5]
print("Top connected genes/phenotypes:")
for node, degree in top_genes:
    print(f"  {node}: {degree} connections")

print("\nLiterature map complete!")
