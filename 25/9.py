P=[eval(x)for x in open(0)]
X=lambda a,c,b,d:~abs(a-b)*~abs(c-d)
print(max(X(*A,*B)for A in P for B in P))
Z=sorted
O=lambda A,B,C,D,E,F:(C-A)*(F-B)-(D-B)*(E-A)
Y=lambda A,B,C,D:Z((A,C))+Z((B,D))
def I(a,c,b,d,e,g,f,h):return[a<e<c,b<f<d][f==h]&[max(f,b)<min(h,d),max(e,a)<min(g,c)][f==h]
m=0
R=Z(zip(P,P[1:]+P,P[2:]+P))
for A,B,C in R:
 for D in P:
  if m<(s:=X(*B,*D))and Z((O(*A,*B,*D),O(*B,*C,*D)))[O(*A,*B,*C)>0]>0 and 1-any(I(*Y(*B+D),*Y(*a+b))for a,b,_ in R):m=s
print(m)
