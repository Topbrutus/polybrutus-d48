# Polybrutus 48D — Exact 53-point Euclidean metric and forty-twofold ideal graph mode

**Human scientific author:** Gabriel St-Pierre, independent researcher.
**Material AI assistance:** OpenAI ChatGPT (Astra) assisted exact calculations, separate checker implementations, manuscript and publication. AI is not a scientific author.

## Official published 48D DOI and public verification

- **DOI:** [10.5281/zenodo.24426580](https://doi.org/10.5281/zenodo.24426580); public Zenodo record https://zenodo.org/records/24426580 .
- **Frozen scientific source:** [v0.1.0](https://github.com/Topbrutus/polybrutus-d48/tree/v0.1.0), immutable scientific commit 02e51ca0e0cdb1b30068320c4595e36cc27afc43.
- **GitHub main science CI:** https://github.com/Topbrutus/polybrutus-d48/actions/runs/44942508271 — success.
- **GitHub tag science CI:** https://github.com/Topbrutus/polybrutus-d48/actions/runs/44942552729 — success.
- **Three public Zenodo artifacts:** filenames, sizes and MD5 verified against original SHA-256 archived files.
- **Metadata QA:** exact keywords forty-eight and forty-twofold; structured isDerivedFrom D47 DOI 10.5281/zenodo.24425675; separate two textual citations D47 and D7 (10.5281/zenodo.24407952).
- **Memoria checkpoint:** https://github.com/Topbrutus/topbrutus_one/blob/main/memoria/checkpoints/POLYBRUTUS_D48_PUBLICATION_2026-11-21.md .

## Exact construction

- **53** norm-one labelled vertices; **1,378/1,378** exact unordered labelled squared-distance pairs.
- All **1,326/1,326** parent D47 labelled values remain identical; **52** new squared distances each equal **2R²**.
- Gram PSD and centered Gram PSD, exact rank **48**, minimal affine Euclidean realization dimension **48** for this synthetic metric.
- Histogram k=4d²/R²: 4:6, 7:2, 8:1347, 9:3, 10:10, 12:6, 13:2, 16:2. Exact sum at R=1: **11071/4**.
- Separate chosen ideal complete graph with scalar unit masses and w_ij=R²/d_ij²: eigenvalue **53/2** multiplicity **42**; eigenvalue **26** multiplicity **4**.
- Two exact independently implemented programs (rational Gram and fractions.Fraction direct distance rule); four primary adversarial controls.

Run on Python 3.12:

    python -m pip install sympy==1.14.0
    python src/verify_d48.py
    python tests/independent_d48.py
    python src/check_zenodo_metadata.py

The two programs must output the same deterministic SHA-256 for results/certificate_d48.json. Continuous integration runs both and checks Zenodo metadata before tag.

## Frozen ancestry

**Only direct parent:** [Polybrutus 47D scientific v0.1.0](https://github.com/Topbrutus/polybrutus-d47/tree/v0.1.0), immutable scientific commit c7cdcbebeb0538b234d73015d4d236a33f44c054, DOI [10.5281/zenodo.24425675](https://doi.org/10.5281/zenodo.24425675), original parent certificate SHA-256 8dd08d1a449c08d77170ab9f23fde174d24b8fba340fc1b1f69f1f7c1f3685b0.
Complete original 47D science, including all older nested source ZIPs, is preserved at prior/d47/frozen_scientific_tag_v0.1.0.zip, SHA-256 fa0e823ec641192d43fca92e53808c39a41eaebb3d9edd79230920bf55196322. This exact archive and the byte-identical D47 certificate are authenticated by both checkers.

**Provenance caveat:** The D47 certificate contains an incorrect *textual D46 parent commit ID*, inherited from its construction process. The original D47 tag and D46 tag are independently verifiable. The D48 certificate's direct parent commit ID is taken from the **actual verified D47 Git tag**, not from the erroneous historical field; historical sources are not altered. See [PROVENANCE.md](PROVENANCE.md).

## Manuscript and metadata gate

[Specification](SPECIFICATION_D48.md) | [proof](PREUVE_D48.md) | [source provenance](PROVENANCE.md) | [bibliography](REFERENCES.md) | [PDF preprint](publication/POLYBRUTUS_48D_NOTE.pdf).

Zenodo must include dimension keyword **forty-eight**, ideal multiplicity **forty-twofold**, structured **isDerivedFrom** to verified direct D47 DOI, plus separate **two textual references** (D47 and historical D7). The public Zenodo API must confirm metadata and all three artifacts after release.

**Scope and limitations:** This is one exact synthetic Euclidean metric and a separately stipulated dimensionless ideal weighted graph; no physical extra dimensions, frequencies, particles, novel universal theorem or independent human peer review are demonstrated.
**Licenses:** MIT code, CC BY 4.0 manuscript.
