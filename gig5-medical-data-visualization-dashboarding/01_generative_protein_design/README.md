# Project 1: Generative Protein Design (Diffusion Models)

De novo design of enzymes using Diffusion Probabilistic Models + AlphaFold + RFdiffusion + ProteinMPNN.

## Features
- Target protein 3D structure prediction (AlphaFold)
- Backbone design via RFdiffusion
- Sequence optimization (ProteinMPNN)
- Structure validation (pLDDT score)
- 3D visualization (py3Dmol)

## Tech Stack
- ColabDesign (AlphaFold2, RFdiffusion, ProteinMPNN)
- py3Dmol, PyTorch

## How to Run
Open `generative_protein_design.py` in Google Colab (GPU recommended).

https://colab.research.google.com/drive/1x_OKw371wrz68JTfRbhHbz1oniYptOiy


## Output
- `target_structure.pdb`
- `complex_backbone.pdb`
- Designed sequences + pLDDT scores
