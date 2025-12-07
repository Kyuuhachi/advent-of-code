L=next(I:=open(0))
N=len(L)
S=[0]*N
S[L.index('S')]=1
n=0
for L in I:
 S2=[*S]
 for i in range(N):
  if'^'==L[i]:s=S[i];S2[i-1]+=s;S2[i+1]+=s;S2[i]-=s;n+=s>0
 S=S2
print(n,sum(S))
