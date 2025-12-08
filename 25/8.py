S=[]
for L in open(0):S+=[*map(int,L.split(',')),len(S)],
class J:v=0;d=1
V=[J()for _ in S]
def R(v):
 while v.v:v,v.v=v.v,v.v.v
 return v
n=0
for _,i,j in sorted((sum((a-b)**2 for a,b in zip(I,J)),i,j)for*I,i in S for*J,j in S if i<j):
 A,B=R(V[i]),R(V[j])
 if A!=B:
  A.v=B;B.d+=A.d
  if B.d==len(S):print(k,S[i][0]*S[j][0]);break
 if n==1000:p,q,r=sorted(A.d for A in V if not A.v)[-3:];k=p*q*r
 n+=1
