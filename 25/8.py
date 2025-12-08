S=[]
Z=sorted
for L in open(n:=0):S+=[*map(int,L.split(',')),T:=len(S)],
class J:v=0;d=1
V=[J()for _ in S]
R=lambda v:v.v and R(v.v)or v
for _,i,j in Z((sum((a-b)**2 for a,b in zip(I,J)),i,j)for*I,i in S for*J,j in S[:i]):
 A,B=R(V[i]),R(V[j]);n+=1
 if A!=B:A.v=B;B.d+=A.d
 if B.d>T:print(k,S[i][0]*S[j][0]);break
 if n==T:*_,p,q,r=Z(A.d*(A.v==0)for A in V);k=p*q*r
