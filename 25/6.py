*I,=open(0)
n=sum(eval(Q[-1].join(Q[:-1]))for Q in zip(*[L.split()for L in I]))
m=0
B=zip(*I)
for*L,O in B:
 for Q in B:
  if''.join(Q).strip()=='':m+=eval("".join(L));break
  L+=O,*Q
print(n,m)
