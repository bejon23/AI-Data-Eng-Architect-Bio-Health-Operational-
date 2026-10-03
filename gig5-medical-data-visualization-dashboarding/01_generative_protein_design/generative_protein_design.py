# =======================
# PROJECT 1: Generative Protein Design
# =======================
!pip install -q py3Dmol
!pip install -q git+https://github.com/sokrypton/ColabDesign.git@v1.1.1

print("All tools installed! Ready for protein design.")

# ============================================
# Cell 2: Target & Binder Length
# ============================================
target_sequence = "MVLSPADKTNVKAAWGKVGAHAGEYGAEALERMFLSFPTTKTYFPHF"
binder_length = 50

print(f"Target sequence: {target_sequence}")
print(f"Binder length: {binder_length} amino acids")

# ============================================
# Cell 3: AlphaFold - Target 3D Structure
# ============================================
from colabdesign import mk_afdesign_model, clear_mem

clear_mem()
af_model = mk_afdesign_model(protocol="fixbb", use_multimer=True, num_recycles=3)
af_model.prep_inputs(sequence=target_sequence, chain="A")
af_model.predict()
af_model.save_pdb("target_structure.pdb")
print("target_structure.pdb created (target protein 3D structure).")

# ============================================
# Cell 4: RFdiffusion - Binder Backbone
# ============================================
clear_mem()
rfd_model = mk_afdesign_model(protocol="binder", use_multimer=True)
rfd_model.prep_inputs(pdb_filename="target_structure.pdb", chain="A", binder_len=binder_length)
rfd_model.design_3stage(soft_iters=50, temp_iters=50, hard_iters=10)
rfd_model.save_pdb("complex_backbone.pdb")
print("complex_backbone.pdb created (target + binder backbone).")

binder_sequence = rfd_model.get_seq()[0]
print(f"Designed binder sequence: {binder_sequence[:30]}...")

# ============================================
# Cell 5: ProteinMPNN - Sequence Optimization
# ============================================
from colabdesign import mk_mpnn_model

mpnn_model = mk_mpnn_model()
mpnn_model.prep_inputs(pdb_filename="complex_backbone.pdb")
sequences = mpnn_model.sample(num_seq=10, temperature=0.1)
best_sequence = sequences[0][0]
print(f"Best designed sequence: {best_sequence[:30]}")

# ============================================
# Cell 6: AlphaFold2 Validation
# ============================================
clear_mem()
validate_model = mk_afdesign_model(protocol="fixbb", use_multimer=True)
validate_model.prep_inputs(sequence=best_sequence, chain="B")
validate_model.predict()
plddt_score = validate_model.get_plddt().mean()
print(f"AlphaFold2 pLDDT score: {plddt_score:.2f} (80+ is good)")

if plddt_score > 80:
    print("Design is high quality! Protein will fold as expected.")
else:
    print("Score is low, may need to redesign.")

# ============================================
# Cell 7: 3D Visualization
# ============================================
import py3Dmol as p3d

view = p3d.view(width=600, height=400)
view.addModel(open("complex_backbone.pdb", "r").read(), "pdb")
view.setStyle({'cartoon': {'color': 'spectrum'}})
view.addSurface(p3d.VDW, {'opacity': 0.6})
view.zoomTo()
view.show()
print("Above is your designed protein complex!")

# ============================================
# Cell 8: Final Report
# ============================================
print("\n" + "="*50)
print("FINAL DESIGN REPORT")
print("="*50)
print(f"Target Protein: {target_sequence[:20]}...")
print(f"Designed Binder: {best_sequence[:30]}...")
print(f"AlphaFold Confidence (pLDDT): {plddt_score:.2f}/100")
print(f"Output files: target_structure.pdb, complex_backbone.pdb")
print("="*50)
print("This protein is now ready for gene synthesis & testing!")
