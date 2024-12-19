import functools as F
G,_,*S=open("19.in").read().splitlines()
@F.cache
def f(s):
 if s == "": return 1
 n = 0
 for g in G.split(", "):
  if s.startswith(g):
   n += f(s[len(g):])
 return n
print(sum(f(s)!=0 for s in S))
print(sum(f(s) for s in S))
