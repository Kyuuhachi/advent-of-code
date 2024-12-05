S=str.split
a,b=S(open("05.in").read(),"\n\n")
p={(*S(a,"|"),)for a in S(a)}
A=[0,0]
for b in S(b):
 c=x,d=S(b,","),0
 while c:
  for i in range(c:=0,l:=len(x)-1):
   if(x[i+1],x[i])in p:x[i:i+2]=x[i+1],x[i];c=d=1
 A[d]+=int(x[l//2])
print(*A)
