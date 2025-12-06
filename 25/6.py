*I,=open(0)
*A,=zip(*[L.split()for L in I])
B=zip(*I)
n=sum(eval(Q[-1].join(Q[:-1]))for Q in A)

m=0
for*L,O in B:
 for Q in B:
  if''.join(Q).strip()=='':break
  L+=O,*Q
 m+=eval("".join(L))
print(n,m)
