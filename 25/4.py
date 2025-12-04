i=open(0).read()
R=range(len(i))
W=i.find('\n')+1
P={p for p in R if'?'<i[p]}
n=0
for p in R:
 b=sum(p+t in P for t in(-W-1,-W,-W+1,-1,1,W-1,W,W+1))<4*(p in P)
 n+=b
 print('x'if b else i[p],end='')
print(n)
