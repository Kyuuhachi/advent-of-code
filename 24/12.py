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
   R(g[j]).v += 1
   R(g[i]).v += 1
  elif R(g[j]) != R(g[i]):
   R(g[i]).v += R(g[j]).v
   R(g[j]).v = g[i]

R(g[-1]).v=0
x={}
for i in range(w*w):
 if i%w==w-1:
  print()
 else:
  if s[i]==10:continue
  n = x.setdefault(R(g[i]),len(x))
  b,n=divmod(n,16)
  # print(b,n)
  print(f'\x1B\x5B38;5;{n}m{chr(s[i])}\x1B\x5B0m',end='')
print(sum(R(a).v for a in g))
print(len(x))

for se in range(w*w):
 ne=se-1
 nw=se-w-1
 sw=se-w
 for()in[()]*4:
  if s[nw]!=s[ne] and (s[nw]!=s[sw])>=(s[nw]!=s[se]): R(g[nw]).b += 1
  nw,ne,se,sw=ne,se,sw,nw

R(g[-1]).b=0
x={}
for i in range(w*w):
 if i%w==w-1:
  print()
 else:
  if s[i]==10:continue
  n = x.setdefault(R(g[i]),len(x))
  b,n=divmod(n,16)
  # print(b,n)
  print(f'\x1B\x5B38;5;{n}m{chr(s[i])}\x1B\x5B0m',end='')
print(sum(R(a).b for a in g))
print(len(x))
