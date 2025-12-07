L=next(I:=open(0))
N=len(L)
S=[0]*N
S[L.index('S')]=1
n=0
for L in I:
 Z=[*S]
 for i in range(N):
  if'^'==L[i]:s=S[i];Z[i-1]+=s;Z[i+1]+=s;Z[i]=0;n+=s>0
 S=Z
print(n,sum(S))
