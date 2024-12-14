import re
R=[]
W,H=101,103
for l in open("14.in"):
 R+=[[*map(int,re.findall(r"-?\d+",l))]]
for i in[0]*100:
 for r in R:
  r[0]+=r[2];r[1]+=r[3]
  r[0]%=W;r[1]%=H

K=lambda X,Y:sum((y-H//2)*Y>0<X*(x-W//2)for x,y,*_ in R)
print(K(1,1)*K(1,-1)*K(-1,1)*K(-1,-1))

from collections import Counter
for l in open("14.in"):
 R+=[[*map(int,re.findall(r"-?\d+",l))]]

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


#222997632 too high
