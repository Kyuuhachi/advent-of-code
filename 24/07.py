A=B=0
i=int
k=lambda c,p:[v*c for v in p]+[v+c for v in p]
for l in open("07.in"):
 a,b,*C=l.split();p=q=[i(b)]
 for c in C:p=k(i(c),p);q=k(i(c),q)+[i(str(v)+c)for v in q]
 a=i(a[:-1]);A+=a*(a in p);B+=a*(a in q)
print(A,B)
