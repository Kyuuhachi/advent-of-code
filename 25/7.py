N=len(next(I:=open(0)))
S=[n:=0]*N
S[N//2-1]=1
for L in I:
 for i in range(N):
  if'.'<L[i]:s=S[i];S[i-1]+=s;S[i+1]+=s;S[i]=0;n+=s>0
print(n,sum(S))
