g={}
for l in open("23.in"):a,b=sorted([l[:2],l[3:5]]);s=g.setdefault;s(a,{b}).add(b);s(b,set())
a=lambda s:max([[]]+[[x]+a(s&g[x])for x in s],key=len)
print(sum('t'in{a[0],b[0],c[0]}for a in g for b in g[a]for c in g[a]&g[b]),','.join(a({*g})))
