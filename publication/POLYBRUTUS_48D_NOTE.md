# Polybrutus 48D: Exact 53-point Euclidean metric and a forty-twofold ideal graph mode

**Gabriel St-Pierre** — Independent researcher
**21 November 2026**
**Exact mathematical case study / scientific preprint**
**AI assistance:** OpenAI ChatGPT (Astra) materially assisted rational calculations, two separate verifier programs, scientific writing, bibliographic verification and controlled publication; AI is not a scientific author.

## Abstract

We construct one exact labelled squared-distance Euclidean metric for 53 norm-one points by appending a perpendicular unit vector to the immutable Polybrutus 47D metric [1]. All 1326 old labelled squared distances are conserved; 52 new distances squared equal 2 at unit radius, producing 1378 unordered labelled pairs. The exact rational Euclidean centered Gram matrix is positive semidefinite rank 48, establishing minimum affine realization dimension 48 for this synthetic metric. A separately stipulated ideal complete weighted graph with scalar unit masses and weights w_ij=1/d_ij² has exact Laplacian eigenvalue 53/2 of multiplicity 42 and 26 of multiplicity 4. Two independently implemented exact rational programs check every label, inherited ancestry, Gram ranks and graph eigenmode nullities. No physical frequency or extra spacetime dimension is measured.

## 1. Scientific lineage and conservation

Only direct scientific predecessor is St-Pierre, Polybrutus 47D [1], DOI 10.5281/zenodo.24425675, Git tag v0.1.0, actual frozen commit c7cdcbebeb0538b234d73015d4d236a33f44c054. The entire unmodified 47D source ZIP, including all older nested source archives, is preserved at prior/d47/frozen_scientific_tag_v0.1.0.zip (2466751 bytes, 31 entries, CRC PASS, SHA-256 fa0e823ec641192d43fca92e53808c39a41eaebb3d9edd79230920bf55196322). The original parent certificate is stored byte-identically, SHA-256 8dd08d1a449c08d77170ab9f23fde174d24b8fba340fc1b1f69f1f7c1f3685b0. Both checking programs verify these hashes and original source bytes.

Zero-embed predecessor vectors p_i as q_i=(p_i,0), i=1,...,52, and adjoin the perpendicular unit vector q_53=e_49. All 1326 old labelled squared distances remain identical. Each new squared distance ||q_53-q_i||²=2, hence C(53,2)=1378=1326+52. This is a conservative extension of one specified Euclidean metric, not a physically observed extra dimension.

## 2. Exact Gram rank and exhaustive labelled distances

The rational Gram G consists of seven canonical norm-one vertices (rank three), a separate centered five-point unit regular simplex (rank four) and 41 independent perpendicular unit axes, for total exact rank 3+4+41=48. It is PSD by explicit Gram factorization and has unit diagonal. Let D_ii=0, D_ij=2-2G_ij and H=I-11ᵀ/53. Then B=-(1/2)HDH=HGH is PSD and rank 48. The inherited antipodal canonical vertices place the origin in the affine hull.

Every one of 1378 exact unordered labelled pairs is reconstructed and every one of 1326 old labels is checked against the authenticated original 47D certificate. For R=1, normalized distance class k=4d²/R² occurs with counts 4:6, 7:2, 8:1347, 9:3, 10:10, 12:6, 13:2, 16:2. Their sum is 1378 and exact sum of squared distances is 11071/4. Class histogram equality alone cannot establish label identity.

## 3. Separately stipulated ideal graph

Let each edge of the ideal weighted complete graph carry w_ij=1/d_ij² and each vertex a scalar unit mass. Adding q_53 yields 52 new edges of weight 1/2; the Laplacian is L48=[[L47+I52/2,-1_52/2],[-1_52ᵀ/2,26]]. The characteristic polynomial obeys chi53(z)=z(z-53/2)chi52(z-1/2)/(z-1/2), with chosen-model closed form chi53(z)=z(z-53/2)^42(z-26)^4*f6(z-23), where f6=chiP7(z)/z is inherited from the seven-point model.

Independent exact nullities confirm eigenvalue 53/2 of multiplicity 42 and 26 of multiplicity 4. These graph modes are dimensionless and cannot by themselves be interpreted as hertz, particle masses or observed spacetime dimensions.

## 4. Reproducibility, adversarial controls and provenance caveat

Primary src/verify_d48.py builds an exact rational Gram and all labelled distances, checks source ZIP, CRC, certificate, all parent labels, exact centered rank and weighted graph nullities. Four negative controls reject a corrupted pair, duplicate vertex, tilted nonorthogonal new point and histogram-preserving pair-label permutation. Independently, tests/independent_d48.py uses Python fractions.Fraction distance rules without importing the primary constructor, recomputing all pairs, centered Gram rank and graph nullities. Both yield identical deterministic certificate SHA-256.

A historical source caveat is reported rather than hidden: the D47 original certificate's text field identifying its own D46 parent Git commit contains an inaccurate value, whereas the exact actual D46 frozen tag is independently verified. D48 uses the actual verified D47 Git tag c7cdcbebeb0538b234d73015d4d236a33f44c054 as direct scientific parent and preserves all old archive/certificate bytes unchanged. See PROVENANCE.md for exact details.

## 5. Scientific interpretation and mandatory citations

Orthogonal Euclidean completions and uniform graph joins are established methods; this manuscript presents one synthetic exact metric and a separately chosen ideal graph. It does not prove physical higher dimensions, measured frequencies, new particles, a novel universal theorem or independent human peer review. Reproduce with Python 3.12, sympy==1.14.0 and both programs, plus an offline Zenodo metadata gate.

The publication must contain a structured Zenodo relation isDerivedFrom -> direct D47 DOI 10.5281/zenodo.24425675, separate textual references to D47 [1] and original Polybrutus 7D [2], and current exact certificate-based keywords forty-eight and forty-twofold, all publicly verified after release.

## References

[1] St-Pierre, Gabriel (2026). Polybrutus 47D: Exact 52-Point Euclidean Metric and Forty-Onefold Ideal Graph Mode. Zenodo. DOI: 10.5281/zenodo.24425675. https://doi.org/10.5281/zenodo.24425675

[2] St-Pierre, Gabriel (2026). Polybrutus 7D: An Exact Twelve-Point Orthogonal Completion, the 12-35-37 Identity, and an Oscillator Model. Zenodo. DOI: 10.5281/zenodo.24407952. https://doi.org/10.5281/zenodo.24407952

[3] St-Pierre, Gabriel (2026). Polybrutus D47 original frozen scientific tag v0.1.0, GitHub: https://github.com/Topbrutus/polybrutus-d47/tree/v0.1.0 ; commit c7cdcbebeb0538b234d73015d4d236a33f44c054. Original complete ZIP is embedded unchanged.
