G={}
for L in open(0):
 A,*B=L.split()
 G[A[:-1]]=B
O={"out":[1,0,0,0]}
while G:
 for K in[*G]:
  N=[0]*4
  for V in G[K]:
   if V in O:
    a,b,c,d=O[V];N[0]+=a;N[1]+=b;N[2]+=c;N[3]+=d
    if"fft"==V:N[1]+=a;N[3]+=c
    if"dac"==V:N[2]+=a;N[3]+=b
   else:break
  else:O[K]=N;del G[K]
print(O["you"][0],O["svr"][3])
