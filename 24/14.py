import re
R=[[*map(int,re.findall(r"-?\d+",l))]for l in open("14.in")]

K=lambda a,b:sum(((y+Y*100)%103-51)*b>0<a*((x+X*100)%101-50)for x,y,X,Y in R)
r=range(99)
A=min(r,key=lambda t:len({(x+X*t)%101 for x,y,X,Y in R}))
B=min(r,key=lambda t:len({(y+Y*t)%103 for x,y,X,Y in R}))
print(K(1,1)*K(1,-1)*K(-1,1)*K(-1,-1),(B*5151+A*5253)%10403)
