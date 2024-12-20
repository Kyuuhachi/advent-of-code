s=open("20.in").read()
f=s.find
p,=M={f('S'):0}
P=0
for x in[-1,w:=f('\n')+1,1,-w]*w*w:
 if s<s[p+x]and P+x:P=x;p+=x;M[p]=len(M)

n=0
for a in M:
 for X in range(-20,21):
  if(a+X)//w==a//w:
   for Y in range(r:=abs(X)-20,1-r):n+=M[a]-M.get(b:=a+X+Y*w,1e9)-abs(a%w-b%w)-abs(a//w-b//w)>99
print(n)
