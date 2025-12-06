*I,=open(0)
n=sum(eval(Q[-1].join(Q[:-1]))for Q in zip(*[L.split()for L in I]))
m=0
M=[]
for*L,O in [*zip(*I)][::-1]:
 M+=''.join(L),
 if O in"+*":m+=eval(O.join(M[1:]));M=[]
print(n,m)
