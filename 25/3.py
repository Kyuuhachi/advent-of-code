n=m=0
for L in open(0):
 a=max(range(len(L)-2),key=lambda i:L[i])
 b=max(range(a+1,len(L)),key=lambda i:L[i])
 n+=int(L[a]+L[b])

 i,s=0,""
 for k in range(12,0,-1):
  i=max(range(i,len(L)-k),key=lambda i:L[i])
  s+=L[i]
  i+=1
 m+=int(s)
print(n,m)
