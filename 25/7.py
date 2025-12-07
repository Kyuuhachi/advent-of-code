L=next(I:=open(0))
N=len(L)
S=[0]*N
S[L.index('S')]=1
n=0
for L in I:
 Z=*S,
 for i in range(N):
  if'.'<L[i]:s=Z[i];S[i-1]+=s;S[i+1]+=s;S[i]=0;n+=s>0
print(n,sum(S))
