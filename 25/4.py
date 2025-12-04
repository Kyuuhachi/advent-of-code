i=open(0).read()
W=i.find('\n')
P={p for p in range(len(i))if'?'<i[p]}
n=[]
while o:={p for p in P if len(P&{p-W-2,p-W-1,p-W,p-1,p+1,p+W,p+W+1,p+W+2})<4}:
 n+=len(o),
 P-=o
print(n[0],sum(n))
