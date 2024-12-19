import functools as F
s=open("19.in").read().splitlines()
G=s[0].split(", ")
@F.cache
def f(s):
 if s == "": return 1
 n = 0
 for g in G:
  if s.startswith(g):
   n += f(s[len(g):])
 return n
print(sum(f(s)!=0 for s in s[2:]))
print(sum(f(s) for s in s[2:]))
