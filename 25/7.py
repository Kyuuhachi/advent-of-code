S=[n:=0]*999
for L in open(0):
 for i in range(len(L)):s=S[i]*('.'<L[i]);S[i-1]+=s;S[i+1]+=s;S[i]-=s-(L[i]=='S');n+=s>0
print(n,sum(S))
