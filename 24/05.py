a,b = open("05.in").read().split("\n\n")
pairs = set()
for a in a.split():
 a1, a2 = a.split("|")
 pairs.add((a1, a2))

A=[0,0]
for b in b.split():
 x = b.split(",")
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
