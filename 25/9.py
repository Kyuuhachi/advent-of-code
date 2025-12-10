Z=sorted
Y=lambda A,B,C,D:Z((A,C))+Z((B,D))
I=lambda A,B,C,D,E,F,G,H:A<E<B>0<max(G,C)<min(H,D)or C<G<D>0<max(E,A)<min(F,B)
n=m=0
R=Z(zip(P:=[*map(eval,open(0))],P[1:]+P))
for A,B in R:
 for D in P:y=a,b,c,d=Y(*B+D);n=max(n,s:=~(b-a)*~(d-c));m=[m,s][m<s>1>any(I(*y+Y(*a+b))for a,b in R)]
print(n,m)
