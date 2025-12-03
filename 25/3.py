def F(M,i=-1):n[M>6]+=int(''.join(L[i:=max(range(i+1,len(L)-k-1),key=lambda i:L[i])]for k in range(M,-1,-1)))
n=[0,0]
for L in open(0):F(1);F(11)
print(n)
