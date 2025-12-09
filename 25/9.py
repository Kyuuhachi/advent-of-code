P=[eval(x)for x in open(0)]
X=lambda a,c,b,d:~abs(a-b)*~abs(c-d)
Z=sorted
O=lambda A,B,C,D,E,F:(C-A)*(F-B)-(D-B)*(E-A)
Y=lambda A,B,C,D:Z((A,C))+Z((B,D))
I=lambda A,B,C,D,E,F,G,H:[A<E<B,C<G<D][G==H]&[max(G,C)<min(H,D),max(E,A)<min(F,B)][G==H]
n=m=0
R=Z(zip(P,P[1:]+P,P[2:]+P))
for A,B,C in R:
 for D in P:
  n=max(n,s:=X(*B+D))
  if m<s and Z((O(*A+B+D),O(*B+C+D)))[O(*A+B+C)>0]>0 and 1-any(I(*Y(*B+D)+Y(*a+b))for a,b,_ in R):m=s
print(n,m)
