s=open("12.in","rb").read()
w=s.find(10)+1
s+=b'\n'*w

class A:v=a=b=0
def R(n):
 while type(n.v)==A:n,n.v=n.v,n.v.v
 return n

g=[A()for _ in s]
for i in range(w*w):
 for j in i-1,i-w:
  if s[j]-s[i]:
   R(g[j]).a += 1
   R(g[i]).a += 1
  elif R(g[j]) != R(g[i]):
   R(g[i]).a += R(g[j]).a
   R(g[j]).v = g[i]

for se in range(w*w):
 ne=se-1
 nw=se-w-1
 sw=se-w
 for()in[()]*4:
  if s[nw]!=s[ne]: R(g[nw]).b += (s[nw]!=s[sw])|(s[nw]==s[se])
  nw,ne,se,sw=ne,se,sw,nw

R(g[-1]).v=A()
print(sum(R(a).a for a in g))
print(sum(R(a).b for a in g))
