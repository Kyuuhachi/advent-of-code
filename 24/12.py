s=open("12.in").read()
w=s.find('\n')+1
s+='\n'*w
class J:v=b=0
def R(v):
 while v.v:v,v.v=v.v,v.v.v
 return v
g=[J()for _ in s]
for a in range(w*w):
 for k in[a,b:=a-1,c:=b-w,d:=a-w]:
  d,A,B,c=a,R(g[a:=b]),R(g[b:=c]),d;S=s[a]
  if S!=s[b]:A.b+=1-(s[d]==S!=s[c])+1j
  elif A!=B:A.b+=B.b;B.v=A
R(g[a]).b=0
print(sum(R(a).b for a in g))
