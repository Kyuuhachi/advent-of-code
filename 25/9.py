P=[eval(x)for x in open(0)]
Z=sorted
O=lambda A,B,C,D,E,F:(C-A)*(F-B)-(D-B)*(E-A)
Y=lambda A,B,C,D:Z((A,C))+Z((B,D))
I=lambda A,B,C,D,E,F,G,H:A<E<B>0<max(G,C)<min(H,D)or C<G<D>0<max(E,A)<min(F,B)
n=m=0
R=Z(zip(P,P[1:]+P,P[2:]+P))
for A,B,C in R:
 for D in P:
  V=a,c,b,d=B+D;n=max(n,s:=~abs(a-b)*~abs(c-d))
  if s-m>0<Z((O(*A+V),O(*B+C+D)))[O(*A+B+C)>0]and 1-any(I(*Y(*V)+Y(*a+b))for a,b,_ in R):m=s
print(n,m)
