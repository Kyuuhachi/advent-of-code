import re
R=[[*map(int,re.findall(r"-?\d+",l))]for l in open("14.in")]
K=lambda a,b:sum(((y+Y*100)%103-51)*b>0<a*((x+X*100)%101-50)for x,y,X,Y in R)
r=range(99)
F=lambda i,j:min(r,key=lambda t:len({(r[i]+r[2+i]*t)%j for r in R}))
print(K(1,1)*K(1,-1)*K(-1,1)*K(-1,-1),(F(1,103)*5151+F(0,101)*5253)%10403)
