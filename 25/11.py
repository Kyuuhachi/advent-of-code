G={}
for L in open(0):
 A,*B=L.split()
 G[A[:-1]]=B
print(G)
O={"out":[1,0,0,0]}
while G:
 for K in[*G]:
  N=[0]*4
  for V in G[K]:
   if V in O:
    for i in range(4):N[i]+=O[V][i]
    if V=="fft":N[1]+=O[V][0];N[3]+=O[V][2]
    if V=="dac":N[2]+=O[V][0];N[3]+=O[V][1]
   else:break
  else:O[K]=N;del G[K]
for k,v in O.items():print(k,v)
print(O["you"][0])
print(O["svr"][3])
