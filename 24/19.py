import functools as F
G,_,*S=open("19.in")
f=F.cache(lambda s:sum(f(s[len(g):])for g in G[:-1].split(", ")if s[:len(g)]==g)if s else 1)
print(sum(map(bool,v:=[f(s[:-1])for s in S])),sum(v))
