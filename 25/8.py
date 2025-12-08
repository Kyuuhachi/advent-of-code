S=[]
Z=sorted
for L in open(n:=0):S+=[*map(int,L.split(',')),len(S)],
T=1000
*D,=V=[-1]*T
R=lambda v:R(V[v])if-1<V[v]else v
for _,i,j in Z((sum((a-b)**2 for a,b in zip(I,J)),i,j)for*I,i in S for*J,j in S[:i]):
 if n==T:*_,p,q,r=Z(d*v for d,v in zip(D,V))
 A,B=R(i),R(j);n+=1
 if A!=B:V[A]=B;D[B]+=D[A]
 if-T==D[B]:-print(p*q*r,S[i][0]*S[j][0])
