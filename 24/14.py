import re
R=[]
W,H=101,103
for l in open("14.in"):
 R+=[[*map(int,re.findall(r"-?\d+",l))]]

K=lambda a,b:sum(((y+Y*100)%H-H//2)*b>0<a*((x+X*100)%W-W//2)for x,y,X,Y in R)
print(K(1,1)*K(1,-1)*K(-1,1)*K(-1,-1))

import zlib
g=lambda a:len(zlib.compress(bytes(i in a for i in range(H))))
A=max(range(W),key=lambda t:g({(x+X*t)%W for x,y,X,Y in R}))
B=max(range(H),key=lambda t:g({(y+Y*t)%H for x,y,X,Y in R}))
print((B*5151+A*5253)%10403)
