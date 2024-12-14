import re
R=[[*map(int,re.findall(r"-?\d+",l))]for l in open("14.in")]
K=lambda a,b:sum(((y+Y*100)%103-51)*b>0<a*((x+X*100)%101-50)for x,y,X,Y in R)
r=range(99)
A=min(r,key=lambda t:len({(r[0]+r[2]*t)%101 for r in R}))
B=min(r,key=lambda t:len({(r[1]+r[3]*t)%103 for r in R}))
print(K(1,1)*K(1,-1)*K(-1,1)*K(-1,-1),(B*5151+A*5253)%10403)
