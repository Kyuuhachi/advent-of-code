import functools as F
s=open("21.in").read().split()
Q=' ^A<v>'

@F.cache
def G(s,N,B):
 if N==0:return len(s)
 o=0
 p=B.find('A')
 H=B.find(' ')
 for c in s:
  P=B.find(c)
  x=P%3-p%3;x='>'*x+'<'*-x
  y=P//3-p//3;y='v'*y+'^'*-y
  o+=min([G(x+y+'A',N-1,Q)][:P%3!=H%3 or p//3!=H//3]+[G(y+x+'A',N-1,Q)][:p%3!=H%3 or P//3!=H//3])
  p=P
 return o
for N in 3,26:print(sum(int(i[:-1])*G(i,N,'789456123 0A')for i in s))
