import re
m=n=0
for s in re.finditer(r'\D*(\d+)'*6,open("13.in").read()):
 a,b,c,d,x,y=map(int,s.groups())

 D=a*d-b*c
 a,b,c,d=d,-b,-c,a

 A=a*x+c*y
 B=b*x+d*y
 if A%D+B%D==0:
  m+=(3*A+B)//D

 x+=10000000000000
 y+=10000000000000
 A=a*x+c*y
 B=b*x+d*y
 if A%D+B%D==0:
  n+=(3*A+B)//D
print(m,n)
