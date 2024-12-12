s=open("12.in","rb").read()
w=s.find(10)+1
s+=b'\n'*w

class J:v=b=0
def R(n):
 while type(n.v)==J:n,n.v=n.v,n.v.v
 return n

g=[J()for _ in s]
for a in range(w*w):
 b,c,d=a-1,a-w-1,a-w
 for()in[()]*4:
  c,b,a,d=b,a,d,c;A=R(g[a]);B=R(g[b]);S=s[a]
  if S!=s[b]:A.b+=((S!=s[d])|(S==s[c]))+1j
  elif A!=B:A.b+=B.b;B.v=A

R(g[a]).b=0
print(sum(R(a).b for a in g))
