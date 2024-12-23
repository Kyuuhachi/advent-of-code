g={}
for l in open("23.in"):
 a,b=l[:2],l[3:5]
 for a,b in(a,b),(b,a):g.setdefault(a,set()).add(b)

n=0
for a in g:
 for b in g[a]:
  for c in g[a]&g[b]:
   if a<b<c and't'in{a[0],b[0],c[0]}:
    n+=1
print(n)

import functools as F
@F.cache
def a(w,s):return max((a((w|{x}),s&g[x])for x in s), key=len)if s else w
print(','.join(sorted(a(frozenset(),frozenset(g)))))
