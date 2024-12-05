S=str.split
a,b=S(open("05.in").read(),"\n\n")
p={(*S(a,"|"),)for a in S(a)}

A=[0,0]
for b in S(b):
 x=S(b,",");c=1;d=0
 while c:
  c=0
  for a in range(l:=len(x)-1):
   if(x[a+1],x[a])in p:
    x[a:a+2]=x[a+1],x[a]
    c=d=1
 A[d]+=int(x[l//2])
print(*A)
