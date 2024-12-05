a,b = open("05.in").read().split("\n\n")
pairs = set()
for a in a.split():
 a1, a2 = a.split("|")
 pairs.add((a1, a2))

A=B=0
for b in b.split():
 x = b.split(",")
 any_bad = any((x[b], x[a]) in pairs for a in range(len(x)) for b in range(a+1, len(x)))
 if any_bad:
  c=1
  while c:
   c=0
   for a in range(len(x)):
    for b in range(a+1, len(x)):
     if (x[a], x[a+1]) in pairs:
      x[a], x[a+1] = x[a+1], x[a]
      c=1
  B += int(x[len(x)//2])
 else:
  A += int(x[len(x)//2])
print(A,B)
