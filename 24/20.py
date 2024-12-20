s=open("20.in").read()
f=s.find
p,=M={f('S'):0}
P=0
for x in[-1,w:=f('\n')+1,1,-w]*w*w:
 if s<s[p+x]and P+x:P=x;p+=x;M[p]=len(M)
R=range
A=abs
for x in 2,20:
 print(sum(
M[a]-M.get(b:=a+X+Y*w,1e9)>99+A(a%w-b%w)+A(a//w-b//w)
for a in M
for X in R(-x,x+1)
for Y in R(A(X)-x,1-A(X)+x)
if-1<a%w+X<w
 ))
