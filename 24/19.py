import functools as F
G,_,*S=open("19.in").read().splitlines()
f=F.cache(lambda s:sum(f(s[len(g):])for g in G.split(", ")if s.startswith(g))if s else 1)
print(sum(0!=f(s)for s in S),sum(f(s)for s in S))
