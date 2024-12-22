import functools as F
s=open("21.in").read().split()

@F.cache
def G(s,N,board):
 if N==0:return len(s)
 out=0
 pos=board.find('A')
 hole = board.find(' ')
 for c in s:
  npos=board.find(c)
  dx=npos%3-pos%3;   dx='>'*dx+'<'*-dx
  dy=npos//3-pos//3; dy='v'*dy+'^'*-dy
  k=[]
  if npos%3!=hole%3 or pos//3!=hole//3:k+=[g(dx+dy+'A',N-1)]
  if pos%3!=hole%3 or npos//3!=hole//3:k+=[g(dy+dx+'A',N-1)]
  out+=min(k)
  pos=npos
 return out
f=lambda*a:G(*a,'789456123 0A')
g=lambda*a:G(*a,' ^A<v>')

print(sum(int(i[:-1])*f(i, 3)for i in s))
print(sum(int(i[:-1])*f(i, 26)for i in s))
