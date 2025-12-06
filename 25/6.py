*I,=open(0)
n=sum(eval(Q[-1].join(Q[:-1]))for Q in zip(*[L.split()for L in I]))
m=0
B=zip(*I)
for*L,O in B:
 for Q in B:
  if''.join(Q).strip()=='':break
  L+=O,*Q
 m+=eval("".join(L))
print(n,m)
