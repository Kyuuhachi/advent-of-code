I=[(*map(int,s[:-1].split(',')),) for s in open("18.in")]
def F(n):
 P=[(0,0,0)]
 S={*I[:n]}
 for x,y,s in P:
  if(x,y)==(70,70):return s
  if{(x,y)}-S and 0<=x<71 and 0<=y<71:
   S|={(x,y)}
   P+=[(x-1,y,w:=s+1),(x+1,y,w),(x,y-1,w),(x,y+1,w)]
print(F(m:=1024))

M=len(I)
while m<M:
 if F(q:=m+M>>1):m=q+1
 else:M=q
print(*I[m-1],sep=',')
