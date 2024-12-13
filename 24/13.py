import re
k=[0,0]
for s in re.finditer(r'\D*(\d+)'*6,open("13.in").read()):
 a,b,c,d,x,y=map(int,s.groups());D=a*d-b*c
 for i in 0,1:A=d*x-c*y;B=a*y-b*x;k[i]+=(3*A+B)/D*(A%D+B%D==0);x+=1e13;y+=1e13
print(*k)
