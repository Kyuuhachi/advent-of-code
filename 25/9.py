P=[eval(x)for x in open(0)]
X=lambda a,c,b,d:~abs(a-b)*~abs(c-d)
print(max(X(*A,*B)for A in P for B in P))
Z=sorted
O=lambda A,B,C,D,E,F:(C-A)*(F-B)-(D-B)*(E-A)
def I(A,B,C,D,E,F,G,H):a,b=Z((A,C));c,d=Z((B,D));e,f=Z((F,H));g,h=Z((E,G));return a<E<b and max(e,c)<min(f,d)if F-H else c<F<d and max(g,a)<min(h,b)
m=0
R=Z(zip(P,P[1:]+P,P[2:]+P))
for A,B,C in R:
 for D in P:
  if m<(s:=X(*B,*D))and Z((O(*A,*B,*D),O(*B,*C,*D)))[O(*A,*B,*C)>0]>0 and 1-any(I(*B,*D,*a,*b)for a,b,_ in R):m=s
print(m)
