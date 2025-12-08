S=[]
Z=sorted
for L in open(n:=0):S+=[*map(int,L.split(',')),T:=len(S)],
class J:v=-1;d=1
D=[1]*(T+1)
V=[J()for _ in S]
R=lambda v:V[v].v>-1 and R(V[v].v)or v
for _,i,j in Z((sum((a-b)**2 for a,b in zip(I,J)),i,j)for*I,i in S for*J,j in S[:i]):
 A,B=R(i),R(j);n+=1
 if A!=B:V[A].v=B;D[B]+=D[A]
 if D[B]>T:print(k,S[i][0]*S[j][0]);break
 if n==T:*_,p,q,r=Z(D[A]*(V[A].v<0)for A in range(T));k=p*q*r
