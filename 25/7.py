L=next(I:=open(0))
S=[0]*len(L)
S[L.index('S')]=1
n=0
for L in I:
 S2=[*S]
 for i in range(len(L)):
  if'^'==L[i]:S2[i-1]+=S[i];S2[i+1]+=S[i];S2[i]-=S[i];n+=S[i]>0
 S=S2
print(n,sum(S))
