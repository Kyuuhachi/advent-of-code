A = B = 0
def r(a,c):
 if a%1 or not c:return(a==Q)*W
 b,*c=c
 v=r(a-b,c)
 v|=r(a/b,c)
 v|=O*r((a-b)/10**len(str(b)),c)
 return v

for line in open("07.in"):
 W,Q,*c,=map(int,line.replace(*': ').split())
 c=c[::-1]
 O=0;A+=r(W,c)
 O=1;B+=r(W,c)
print(A, B)
