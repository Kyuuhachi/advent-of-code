E=enumerate
S=[]
for i,L in E(open(0)):
 X,Y,Z=map(int,L.split(','))
 S+=[i,X,Y,Z],
D=sorted(
 ((a-b)**2+(c-d)**2+(e-f)**2,i,j)
 for i,a,c,e in S
 for j,b,d,f in S
 if i<j
)
class J:v=0;d=1
V=[J()for _ in S]
def R(v):
 while v.v:v,v.v=v.v,v.v.v
 return v
for q,(_,i,j)in E(D):
 A,B=R(V[i]),R(V[j])
 if A!=B:
  A.v=B
  B.d+=A.d
  if B.d==len(S):
   print(k,S[i][1]*S[j][1])
   break
 if q==1000:
  p,q,r=sorted(A.d for A in V if not A.v)[-3:]
  k=p*q*r
