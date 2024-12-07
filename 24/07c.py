A = B = 0
def solve(a, *c):
 if()==c:return(a==Q)*W
 b,*c=c
 v = 0
 if not a % b: v |= solve(a//b, *c)
 if a > b: v |= solve(a-b, *c)
 n = 10**len(str(b))
 if O and a % n == b: v |= solve(a//n, *c)
 return v

for line in open("07.in"):
 W,Q,*c,=map(int,line.replace(*': ').split())
 c=c[::-1]
 O=0;A+=solve(W,*c)
 O=1;B+=solve(W,*c)
print(A, B)
