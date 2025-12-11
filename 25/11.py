G={}
for L in open(0):
 A,*B=L.split()
 G[A[:-1]]=B
print(G)
O={"out":1}
while G:
 for K in[*G]:
  N=0
  for V in G[K]:
   if V in O:N+=O[V]
   else:break
  else:O[K]=N;del G[K]
print(O["you"])
