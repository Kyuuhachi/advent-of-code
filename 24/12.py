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
  if s[j]==s[i] and R(g[j]) != R(g[i]):
   R(g[j]).v = g[i]

for a in range(w*w):
 b=a-1
 c=a-w-1
 d=a-w
 for()in[()]*4:
  if s[a]!=s[b]:R(g[a]).a+=1; R(g[a]).b += (s[a]!=s[d])|(s[a]==s[c])
  c,b,a,d=b,a,d,c

R(g[-1]).v=A()
print(sum(R(a).a for a in g))
print(sum(R(a).b for a in g))
