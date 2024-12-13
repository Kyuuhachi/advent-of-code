import re
k=[0,0]
W=10000000000000
for s in re.finditer(r'\D*(\d+)'*6,open("13.in").read()):
 a,b,c,d,x,y=map(int,s.groups())

 D=a*d-b*c
 a,b,c,d=d,-b,-c,a
 for i in 0,1:
  A=a*x+c*y
  B=b*x+d*y
  if A%D+B%D==0:
   k[i]+=(3*A+B)//D
  x+=W;y+=W
print(*k)
