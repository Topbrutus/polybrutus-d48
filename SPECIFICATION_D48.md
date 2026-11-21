# Polybrutus D48 — Exact rational Euclidean labelled-distance metric

## Parent science

Only parent is Topbrutus/polybrutus-d47@v0.1.0, exact Git commit c7cdcbebeb0538b234d73015d4d236a33f44c054, published DOI 10.5281/zenodo.24425675; original source ZIP SHA-256 fa0e823ec641192d43fca92e53808c39a41eaebb3d9edd79230920bf55196322 and original certificate SHA-256 8dd08d1a449c08d77170ab9f23fde174d24b8fba340fc1b1f69f1f7c1f3685b0. All previous ancestry is nested unchanged in the original 47D scientific ZIP.

## Conservative orthogonal extension

Zero-embed 52 predecessor unit vectors p_i as q_i=(p_i,0), then append an independent perpendicular unit vector q_53=e_49. Old labelled squared distances are identical, preserving all 1326 predecessor pairs; 52 new squared distances are ||q_53-q_i||²=2R². Hence C(53,2)=1378=1326+52.

Construct unit-diagonal rational Gram G: canonical seven-point rank-three Gram; separate five-point regular unit-simplex rank-four Gram (diagonal 1, off-diagonal -1/4); and 41 mutually independent orthogonal unit axes. The explicit Gram representation gives PSD and rank(G)=3+4+41=48. Let D_ii=0, D_ij=2-2G_ij and H=I-11ᵀ/53. Centered Euclidean Gram B=-HDH/2=HGH is PSD rank 48; inherited canonical antipodal vertices place origin in the affine hull and prove minimum affine Euclidean realization dimension exactly 48. Ambient coordinate storage: 49.

At R=1, histogram k=4d²/R²: 4:6, 7:2, 8:1347, 9:3, 10:10, 12:6, 13:2, 16:2, 1378 total pairs, exact squared-distance sum 11071/4.

## Separately stipulated ideal weighted graph

Scalar unit masses, symmetric edge weights w_ij=1/d_ij². New unit vertex attaches to every prior vertex at weight 1/2:
L48 = [[L47 + (1/2)I52, -(1/2)1_52],[-(1/2)1_52ᵀ, 26]].
Characteristic recurrence: chi53(z)=z(z-53/2)chi52(z-1/2)/(z-1/2).
With inherited f6(z)=chiP7(z)/z, closed model expression chi53(z)=z(z-53/2)^42(z-26)^4*f6(z-23).
Exact Laplacian nullity checks show eigenvalue 53/2 of multiplicity 42 and eigenvalue 26 multiplicity 4. These modes are dimensionless; there are no measured physical frequencies.

**Bibliography:** direct D47 10.5281/zenodo.24425675, historical Polybrutus 7D 10.5281/zenodo.24407952.
**Scientific limit:** This is one exact synthetic Euclidean metric and a separately stipulated dimensionless ideal weighted graph; no physical extra dimensions, frequencies, particles, novel universal theorem or independent human peer review are demonstrated.
