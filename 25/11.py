G={}
for L in open(0):G[L[:3]]=L[4:].split()
O={"out":[1,0,0,0]}
for K in[*G]*99:
 A=B=C=D=0
 try:
  for V in G[K]:p,q=V=="fft",V=="dac";a,b,c,d=O[V];A+=a;B+=b+a*p;C+=c+a*q;D+=d+c*p+b*q
  O[K]=A,B,C,D;del G[K]
 except:0
print(O["you"][0],O["svr"][3])
