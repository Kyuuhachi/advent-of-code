I=[(*map(int,s[:-1].split(',')),)for s in open("18.in")]
def F(n):
 P=[[0]*3];S={*I[:n]}
 for x,y,s in P:
  if{v:=(x,y)}-S and y>-1<x<71>y:S|={v};P+=(x-1,y,w:=s+1),(x+1,y,w),(x,y-1,w),(x,y+1,w)
  if(70,70)==v:return s
print(F(m:=1024))
M=len(I)
while m+1<M:
 if F(q:=m+M>>1):m=q
 else:M=q
print(*I[m],sep=',')
