import re,zlib
R=[[*map(int,re.findall(r"-?\d+",l))]for l in open("14.in")]

K=lambda a,b:sum(((y+Y*100)%103-51)*b>0<a*((x+X*100)%101-50)for x,y,X,Y in R)
print(K(1,1)*K(1,-1)*K(-1,1)*K(-1,-1))

r=range(103)
g=lambda a:len(zlib.compress(bytes(i in a for i in r)))
A=max(r,key=lambda t:g({(x+X*t)%101 for x,y,X,Y in R}))
B=max(r,key=lambda t:g({(y+Y*t)%103 for x,y,X,Y in R}))
print((B*5151+A*5253)%10403)
