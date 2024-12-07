r=lambda a,c:W*(a==Q)if a%1 or[]==c else r(a-(b:=c[0]),c:=c[1:])|r(a/b,c)|O*r((a-b)/10**len(str(b)),c)
A=B=0
for line in open("07.in"):*c,Q,W=map(int,line.replace(*': ').split()[::-1]);O=0;A+=r(W,c);O=1;B+=r(W,c)
print(A,B)
