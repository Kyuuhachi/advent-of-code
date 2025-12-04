i=open(0).read()
R=range(len(i))
W=i.find('\n')+1
P={p for p in R if'?'<i[p]}
n=[]
while True:
 o={p for p in P if sum(p+t in P for t in(-W-1,-W,-W+1,-1,1,W-1,W,W+1))<4}
 n+=len(o),
 print(n)
 P-=o
 if not o:break
print(n[0],sum(n))
