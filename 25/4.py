i=open(0).read()
W=i.find('\n')+1
P={p for p in range(len(i))if'?'<i[p]}
n=[]
o=1
while o:
 o={p for p in P if len(P&{p-W-1,p-W,p-W+1,p-1,p+1,p+W-1,p+W,p+W+1})<4}
 n+=len(o),
 P-=o
print(n[0],sum(n))
