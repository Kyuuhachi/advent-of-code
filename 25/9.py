P=[eval(x)for x in open(0)]
X=lambda a,c,b,d:~abs(a-b)*~abs(c-d)
print(max(X(*A,*B)for A in P for B in P))
Z=sorted
O=lambda A,B,C,D,E,F:(C-A)*(F-B)-(D-B)*(E-A)

def I(A,B,C,D,E,F,G,H):
 a,b=Z((E,G));c,d=Z((F,H))
 if A == C:e,f=Z((B,D));return a<A<b and max(e,c)<min(f,d)
 else:e,f=Z((A,C));return c<B<d and max(e,a)<min(f,b)

m = 0
k=0
*R,=zip(P[-1:]+P,P,P[1:]+P)
for A,B,C in R:
 k+=1
 print(k,end="\r")
 for D in P:
  s=X(*B,*D)
  if s<=m or Z((O(*A,*B,*D),O(*B,*C,*D)))[O(*A,*B,*C)>0]<1: continue
  for a,b,_ in R:
   if I(*a,*b,*B,*D):
    break
  else:
    m = s
print(m)
