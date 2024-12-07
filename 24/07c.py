A = B = 0
def r(a,c):
 if[]==c:return(a==Q)*W
 b,*c=c
 v=r(a-b,c)
 if a%b==0:v|=r(a//b,c)
 n=10**len(str(b))
 if O&(a%n==b):v|=r(a//n,c)
 return v

for line in open("07.in"):
 W,Q,*c,=map(int,line.replace(*': ').split())
 c=c[::-1]
 O=0;A+=r(W,c)
 O=1;B+=r(W,c)
print(A, B)
