import re
W,H=101,103
R=[[*map(int,re.findall(r"-?\d+",l))]for l in open("14.in")]

K=lambda a,b:sum(((y+Y*100)%H-51)*b>0<a*((x+X*100)%W-50)for x,y,X,Y in R)
print(K(1,1)*K(1,-1)*K(-1,1)*K(-1,-1))

import zlib
r=range(H)
g=lambda a:len(zlib.compress(bytes(i in a for i in r)))
A=max(r,key=lambda t:g({(x+X*t)%W for x,y,X,Y in R}))
B=max(r,key=lambda t:g({(y+Y*t)%H for x,y,X,Y in R}))
print((B*5151+A*5253)%10403)
