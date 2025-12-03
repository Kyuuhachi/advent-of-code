def F(M,i=-1):n[M>6]+=int(''.join(L[i:=max(range(i+1,len(L)-M+k),key=lambda i:L[i])]for k in range(M)))
n=[0,0]
for L in open(0):F(2);F(12)
print(n)
