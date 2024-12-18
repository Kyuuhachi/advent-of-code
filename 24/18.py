I=open("18.in").read().split()
I=[(*map(int,s.split(',')),) for s in I]
def F(n):
 P=[(0,0,0)]
 S={p:-1 for p in I[:n]}
 W=70
 for x,y,s in P:
  if(x,y)not in S and 0<=x<=W and 0<=y<=W:
   S[x,y]=s
   P+=[(x-1,y,s+1),(x+1,y,s+1),(x,y-1,s+1),(x,y+1,s+1)]
 return S.get((W,W))
print(F(m:=1024))

M=len(I)
while m<M:
 if F(q:=(m+M)//2):m=q+1
 else:M=q
print(*I[m-1],sep=',')
