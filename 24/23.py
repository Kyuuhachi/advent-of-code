g={}
for l in open("23.in"):
 a,b=sorted([l[:2],l[3:5]])
 g.setdefault(a,set()).add(b)
 g.setdefault(b,set())

print(sum('t'in{a[0],b[0],c[0]}for a in g for b in g[a]for c in g[a]&g[b]))

import functools as F
@F.cache
def a(w,s):return max((a((w+(x,)),s&g[x])for x in s), key=len)if s else w
print(','.join(sorted(a((),frozenset(g)))))
