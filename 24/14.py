import re
R=[]
W,H=101,103
for l in open("14.in"):
 R+=[[*map(int,re.findall(r"-?\d+",l))]]

K=lambda X,Y:sum(((y+A*100)%H-H//2)*Y>0<X*((x+B*100)%W-W//2)for x,y,B,A in R)
print(K(1,1)*K(1,-1)*K(-1,1)*K(-1,-1))

C=lambda a,b:(a*5151+b*5253)%10403
import zlib
g=lambda a:len(zlib.compress(bytes(i in a for i in range(H))))
A=max(range(W),key=lambda t:g({(x+X*t)%W for x,y,X,Y in R}))
B=max(range(H),key=lambda t:g({(y+Y*t)%H for x,y,X,Y in R}))
print(C(B,A))
