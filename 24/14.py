import re
R=[]
W,H=101,103
for l in open("14.in"):
 R+=[[*map(int,re.findall(r"-?\d+",l))]]

K=lambda X,Y:sum(((y+A*100)%H-H//2)*Y>0<X*((x+B*100)%W-W//2)for x,y,B,A in R)
print(K(1,1)*K(1,-1)*K(-1,1)*K(-1,-1))

from collections import Counter
def K(t):
 c=Counter(((x+X*t)%W,(y+Y*t)%H)for x,y,X,Y in R)
 for i in range(H):
  for j in range(W):
   print(f"\x1B\x5B4{c[j,i]}m.\x1B\x5Bm",end="")
  print()
 print(t)
 print()
 print()

def crt(a, b):
 return(a*W*pow(H,-1,W)+b*H*pow(W,-1,H))%(H*W)

K(6346)
K(6446)

K(crt(60,83))
K(crt(63,84))

import zlib
# A=[]
# for t in range(W*H):
#  c={((x+X*t)%W,(y+Y*t)%H)for x,y,X,Y in R}
#  A+=[(len(zlib.compress(bytes((i%W,i//W)in c for i in range(W*H)))),t)]
# print(min(A)[1])

A=[]
for t in range(W):
 a={(x+X*t)%W for x,y,X,Y in R}
 A+=[(len(zlib.compress(bytes(i in a for i in range(W)))),t)]
print(sorted(A))
A=[]
for t in range(H):
 a={(y+Y*t)%H for x,y,X,Y in R}
 A+=[(len(zlib.compress(bytes(i in a for i in range(H)))),t)]
print(sorted(A))
