s=open("12.in").read()
w=s.find('\n')+1
s+='\n'*w
class J:v=b=0
def R(v):
 while v.v:v,v.v=v.v,v.v.v
 return v
g=[J()for _ in s]
for a in range(w*w):
 b,c,d=a-1,a+~w,a-w
 for()in[()]*4:
  c,b,a,d=b,a,d,c;A=R(g[a]);B=R(g[b]);S=s[a]
  if S!=s[b]:A.b+=((S!=s[d])|(S==s[c]))+1j
  elif A!=B:A.b+=B.b;B.v=A
R(g[a]).b=0
print(sum(R(a).b for a in g))
