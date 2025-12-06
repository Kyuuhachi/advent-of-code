*I,=open(0)
*A,=zip(*[L.split()for L in I])
n=0
for Q in A:
 n+=eval(Q[-1].join(Q[:-1]))
print(n)
