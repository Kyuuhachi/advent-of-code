S=[n:=0]*999
for L in open(0):
 i=0
 for c in L:s=S[i]*(L<c);S[i-1]+=s;S[i]-=s-(c=='S');n+=s>0;i+=1;S[i]+=s
print(n,sum(S))
