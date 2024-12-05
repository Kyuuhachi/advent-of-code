S=str.split
a,b = S(open("05.in").read(),"\n\n")
pairs={(*S(a,"|"),)for a in S(a)}

A=[0,0]
for b in S(b):
 x = S(b,",")
 c=1;d=0
 while c:
  c=0
  for a in range(len(x)):
   for b in range(a+1, len(x)):
    if (x[a+1], x[a]) in pairs:
     x[a], x[a+1] = x[a+1], x[a]
     c=d=1
 A[d] += int(x[len(x)//2])
print(*A)
