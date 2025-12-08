S=[]
Z=sorted
for L in open(n:=0):S+=[*map(int,L.split(',')),T:=len(S)],
D=[1]*(T+1)
V=[-1]*(T+1)
R=lambda v:R(V[v])if-1<V[v]else v
for _,i,j in Z((sum((a-b)**2 for a,b in zip(I,J)),i,j)for*I,i in S for*J,j in S[:i]):
 A,B=R(i),R(j);n+=1
 if A!=B:V[A]=B;D[B]+=D[A]
 if D[B]>T:print(k,S[i][0]*S[j][0]);break
 if n==T:*_,p,q,r=Z(d*(v<0)for d,v in zip(D,V));k=p*q*r
