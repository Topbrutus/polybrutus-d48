#!/usr/bin/env python3
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
c=json.loads((R/'results/certificate_d48.json').read_text(encoding='utf8'))
m=json.loads((R/'publication/zenodo_metadata_blueprint.json').read_text(encoding='utf8'))
assert c['status']=='PASS'
assert c['dimension']==m['scientific_dimension']==48
assert c['vertices']==m['norm_one_vertices']==53
assert c['pairs']==m['exact_labelled_squared_pairs']==1378
assert c['affine_rank']==c['centered_gram_rank']==48
assert c['eigenvalue_53_over_2_multiplicity']==m['model_eigenvalue_53_over_2_multiplicity']==42
assert c['eigenvalue_26_multiplicity']==m['model_eigenvalue_26_multiplicity']==4
assert c['parent_tag_commit']=='c7cdcbebeb0538b234d73015d4d236a33f44c054'
assert c['parent_doi']==m['scientific_parent_doi']=='10.5281/zenodo.24425675'
assert m['related_identifiers']==[{'identifier':'10.5281/zenodo.24425675','relation':'isDerivedFrom','resource_type':'publication-preprint','scheme':'doi'}]
assert len(m['keywords'])==9
assert 'affine Euclidean dimension forty-eight' in m['keywords']
assert 'forty-twofold ideal eigenvalue' in m['keywords']
assert len(m['references'])==2
assert '10.5281/zenodo.24425675' in m['references'][0]
assert '10.5281/zenodo.24407952' in m['references'][1]
assert not any(x in str(m['keywords']) for x in ('thirty-one','twenty-fivefold','forty-seven','forty-onefold'))
doc=(R/'publication/POLYBRUTUS_48D_NOTE.md').read_text(encoding='utf8')
assert all(x in doc for x in ('## References','10.5281/zenodo.24425675','10.5281/zenodo.24407952'))
print('D48_ZENODO_KEYWORDS_REFERENCES_PARENT_RELATION_GATE_PASS')
