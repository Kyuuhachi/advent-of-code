s=open("20.in").read()
f=s.find
p,=M={f('S'):0}
P=0
for x in[-1,w:=f('\n')+1,1,-w]*w*w:
 if s<s[p+x]and P+x:P=x;p+=x;M[p]=len(M)

n=0
k = 0
for a in M:
 k += 1
 if k % 10 == 0:print(k,'/',len(M))
 for dx in range(-20,21):
  if(a+dx)//w==a//w:
   for dy in range(r:=abs(dx)-20,1-r):n+=M[a]-M.get(b:=a+dx+dy*w,1e9)-abs(a%w-b%w)-abs(a//w-b//w)>99
print(n)
