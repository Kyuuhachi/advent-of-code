r=lambda a,c:W*(a==Q)if a%1 or[]==c else O*r(10**-len(str(b:=c[0]))*(a-b),c:=c[1:])|r(a-b,c)|r(a/b,c)
A=B=0
for l in open("07.in"):*c,Q,W=map(int,l.replace(*': ').split()[::-1]);O=0;A+=r(W,c);O=1;B+=r(W,c)
print(A,B)
