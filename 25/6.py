A=[]
for L in open(0):
    A.append(L.split())
*A,=zip(*A)
n=0
for Q in A:
 n+=eval(Q[-1].join(Q[:-1]))
print(n)
