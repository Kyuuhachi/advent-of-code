def F(I,M,i=0):
 for k in range(M,-1,-1):
  i=max(range(i,len(L)-k-1),key=lambda i:L[i])
  n[I]+=int(L[i]+'0'*k)
  i+=1
n=[0,0]
for L in open(0):F(0,1);F(1,11)
print(n)
