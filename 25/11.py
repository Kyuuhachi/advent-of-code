G={}
for L in open(0):
 A,*B=L.split()
 G[A[:-1]]=B
O={"out":[1,0,0,0]}
while G:
 for K in[*G]:
  A=B=C=D=0
  for V in G[K]:
   if V in O:p,q=V=="fft",V=="dac";a,b,c,d=O[V];A+=a;B+=b+a*p;C+=c+a*q;D+=d+c*p+b*q
   else:break
  else:O[K]=A,B,C,D;del G[K]
print(O["you"][0],O["svr"][3])
