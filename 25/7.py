N=len(next(I:=open(0)))
S=[n:=0]*999
S[N//2-1]=1
for L in I:
 for i in range(N):s=S[i]*('.'<L[i]);S[i-1]+=s;S[i+1]+=s;S[i]-=s;n+=s>0
print(n,sum(S))
