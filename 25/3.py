def F(I,M,i=0,s=""):
 for k in range(M,0,-1):
  i=max(range(i,len(L)-k),key=lambda i:L[i])
  s+=L[i]
  i+=1
 n[I]+=int(s)
n=[0,0]
for L in open(0):F(0,2);F(1,12)
print(n)
