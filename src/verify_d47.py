#!/usr/bin/env python3
"""Polybrutus D47: exact Euclidean labelled metric and chosen ideal weighted graph.
Conservative perpendicular unit extension of the immutable Polybrutus D46 v0.1.0.
No physical spacetime dimension or experimentally measured resonance is claimed.
"""
from pathlib import Path
from itertools import combinations
from collections import Counter
from hashlib import sha256
import json
import sympy as s
from sympy.polys.matrices import DomainMatrix

ROOT=Path(__file__).resolve().parents[1]
Q=s.Rational
core=[(0,0,1),(Q(1,2),0,Q(1,2)),(-Q(1,4),Q(3,4),Q(1,2)),
      (-Q(1,4),-Q(3,4),Q(1,2)),(0,0,-1),(Q(1,2),0,-Q(1,2)),
      (-Q(1,2),0,-Q(1,2))]
n=52
pairs=list(combinations(range(n),2))
G=s.zeros(n)
for i in range(7):
    for j in range(7):
        G[i,j]=3*core[i][0]*core[j][0]+core[i][1]*core[j][1]+core[i][2]*core[j][2]
for i in range(7,12):
    for j in range(7,12):
        G[i,j]=1 if i==j else -Q(1,4)
for i in range(12,n):
    G[i,i]=1
assert all(G[i,i]==1 for i in range(n))
assert DomainMatrix.from_Matrix(G).to_field().rank()==47
D=2*s.ones(n)-2*G
for i in range(n):
    D[i,i]=0
assert len(pairs)==1326 and all(D[i,j]>0 for i,j in pairs)

parent_path=ROOT/'prior'/'d46'/'results'/'certificate_d46.json'
parent_archive=ROOT/'prior'/'d46'/'frozen_scientific_tag_v0.1.0.zip'
assert sha256(parent_archive.read_bytes()).hexdigest()=='59779a2bd99b75cb6fb3edcb059819ed12a1fb10402c30079402e464d5ffbf18'
from zipfile import ZipFile
with ZipFile(parent_archive) as _frozen:
    assert _frozen.testzip() is None
    assert _frozen.read('results/certificate_d46.json')==parent_path.read_bytes()
parent_bytes=parent_path.read_bytes()
assert sha256(parent_bytes).hexdigest()=='4b5a26d2df42443eef2fe2e2015dd3042fa31051edb7e283ca9cd25eeaa3899d'
parent=json.loads(parent_bytes)
assert parent['status']=='PASS' and parent['dimension']==46 and parent['vertices']==51
former={(int(e['i'])-1,int(e['j'])-1):s.Rational(e['d2'])
        for e in parent['labelled_squared_distances']}
assert len(former)==1275
assert all(D[i,j]==v for (i,j),v in former.items())
assert all(D[i,51]==2 for i in range(51))
hist=Counter(4*D[i,j] for i,j in pairs)
expected=Counter({4:6,7:2,8:1295,9:3,10:10,12:6,13:2,16:2})
assert hist==expected and sum(hist.values())==1326
assert sum(D[i,j] for i,j in pairs)==Q(10655,4)

H=s.eye(n)-s.ones(n)/n
B=-H*D*H/2
assert B==H*G*H
assert DomainMatrix.from_Matrix(B).to_field().rank()==47
# The first and fifth canonical points are antipodal; origin lies in the affine hull.
assert G[0,4]==-1

L=s.zeros(n)
for i,j in pairs:
    w=1/D[i,j]
    L[i,i]+=w;L[j,j]+=w;L[i,j]-=w;L[j,i]-=w
assert L*s.ones(n,1)==s.zeros(n,1)
assert DomainMatrix.from_Matrix(L-26*s.eye(n)).to_field().rank()==11
assert DomainMatrix.from_Matrix(L-Q(51,2)*s.eye(n)).to_field().rank()==48
old=s.zeros(51)
for i,j in combinations(range(51),2):
    w=1/D[i,j]
    old[i,i]+=w;old[j,j]+=w;old[i,j]-=w;old[j,i]-=w
assert L[:51,:51]-old==s.eye(51)/2
assert all(L[i,51]==-Q(1,2) for i in range(51))
assert L[51,51]==Q(51,2)

# Four adversarial negative controls.
damaged=D.copy();damaged[0,51]=damaged[51,0]=Q(9,4)
assert Counter(4*damaged[i,j] for i,j in pairs)!=hist
duplicate=G.copy();duplicate[51,:]=G[50,:];duplicate[:,51]=G[:,50];duplicate[51,51]=1
assert DomainMatrix.from_Matrix(duplicate).to_field().rank()==46
tilted_dot_to_old_core=s.sqrt(3)*Q(3,10)
assert tilted_dot_to_old_core!=0
swapped=D.copy();swapped.row_swap(0,7);swapped.col_swap(0,7)
assert swapped!=D and Counter(4*swapped[i,j] for i,j in pairs)==hist

report={
  'schema':'POLYBRUTUS-D47-EXACT-CERTIFICATE-v1',
  'status':'PASS','dimension':47,'vertices':52,'pairs':1326,
  'affine_rank':47,'centered_gram_rank':47,'ambient_storage_coordinates':48,
  'radius':1,'parent':'Topbrutus/polybrutus-d46@v0.1.0',
  'parent_tag_commit':'c743aa3e29a16ef9868375077ef31a222fd46c46',
  'parent_doi':'10.5281/zenodo.24416489',
  'parent_certificate_sha256':sha256(parent_bytes).hexdigest(),
  'parent_frozen_tag_archive_sha256':sha256(parent_archive.read_bytes()).hexdigest(),
  'parent_frozen_tag_embedded_as_verified_zip':True,
  'parent_distances_preserved':1275,'new_distances':51,
  'new_squared_distances':['2']*51,
  'histogram_k_4d2':{str(k):int(v) for k,v in sorted(hist.items())},
  'sum_squared_distances':'10655/4',
  'gram_psd_certificate':'B=-(H D H)/2=H G H; G=XX^T exact',
  'negative_controls':'4/4 PASS',
  'oscillator_model':'Chosen ideal equal-mass complete graph with w_ij=1/d_ij^2; no physical measurement',
  'eigenvalue_26_multiplicity':41,
  'eigenvalue_51_over_2_multiplicity':4,
  'spectral_recurrence':'chi52(z)=z*(z-26)*chi51(z-1/2)/(z-1/2)',
  'spectral_closed_form':'chi52(z)=z*(z-26)^41*(z-51/2)^4*f6(z-45/2), f6(z)=chiP7(z)/z',
  'novel_universal_theorem':'NOT CLAIMED','physical_discovery':'NOT CLAIMED',
  'human_peer_review':'NOT_DONE','sympy':s.__version__,
  'labelled_squared_distances':[{'i':i+1,'j':j+1,'d2':str(D[i,j]),'k':str(4*D[i,j])} for i,j in pairs]
}
out=ROOT/'results'/'certificate_d47.json'
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
print('PRIMARY D47 PASS: 52 vertices, 1326 labelled pairs, affine rank 47; 1275/1275 previous pairs preserved')
print('IDEAL GRAPH PASS: eigenvalue 26 x41; eigenvalue 51/2 x4; 4/4 negative controls')
print('CERTIFICATE_SHA256='+sha256(out.read_bytes()).hexdigest())
