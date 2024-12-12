s=open("12.in","rb").read()
w=s.find(10)+1
s+=b'\n'*w

class A:v=b=0
def R(n):
 while type(n.v)==A:n,n.v=n.v,n.v.v
 return n

g=[A()for _ in s]
for a in range(w*w):
 b,c,d=a-1,a-w-1,a-w
 for()in[()]*4:
  if s[a]!=s[b]:R(g[a]).b += ((s[a]!=s[d])|(s[a]==s[c]))+1j
  elif R(g[a])!=R(g[b]):R(g[a]).b += R(g[b]).b;R(g[b]).v = g[a]
  c,b,a,d=b,a,d,c

R(g[a]).b=0
print(sum(R(a).b for a in g))
