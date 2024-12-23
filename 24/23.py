import functools as F
S=sorted
g={}
for l in open("23.in"):a,b=S([l[:2],l[3:5]]);s=g.setdefault;s(a,{b}).add(b);s(b,set())
a=F.cache(lambda w,s:max((a(w+(x,),s&g[x])for x in s),key=len)if s else w)
print(sum('t'in{a[0],b[0],c[0]}for a in g for b in g[a]for c in g[a]&g[b]),','.join(S(a((),frozenset(g)))))
