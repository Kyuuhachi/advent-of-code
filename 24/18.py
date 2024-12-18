I=open("18.in").read().split()
I=[(*map(int,s.split(',')),) for s in I]
W=72
m=12
P=[(0,0,0)]
S={p:-1 for p in I[:m]}
for x,y,s in P:
 if(x,y)not in S and 0<=x<W and 0<=y<W:
  S[x,y]=s
  P+=[(x-1,y,s+1),(x+1,y,s+1),(x,y-1,s+1),(x,y+1,s+1)]
print(S[W-1,W-1])
print(len(S))

class J:v=b=0
def R(v):
 while v.v:v,v.v=v.v,v.v.v
 return v

H={(x,y):J()for x in range(W)for y in range(W)}
l,r=J(),J()
l.b=r.b=1
for i in range(-1,W+1):
 H[-1,i]=H[i,W]=l
 H[W,i]=H[i,-1]=r
for x,y in I:
 for X in-1,0,1:
  for Y in-1,0,1:
   q=R(H[x+X,y+Y])
   if q.b:q.v=H[x,y]
 H[x,y].b=1
 if R(l)==R(r):print("!!!",x,y);break

seen={0:0}
o=[]
for y in range(-1,W+1):
 for x in range(-1,W+1):
  if H[x,y].b:
   c=seen.setdefault(R(H[x,y]),len(seen))
   o.append(f'\x1B\x5B38;5;{c%16}m#\x1B\x5B0m')
  else:
   o.append('.')
 o.append('\n')
print("".join(o))
