from heapq import*
s=open("16.in",'rb').read()
def P(P,D,W=1):
 W+=w;q,m=G[P][D];o=G[p][d][1]|{P}
 if W<q:G[P][D]=W,o
 if W<=q:m|=o;heappush(H,(W,P,D))
F=s.find
S=F(83)
G=[2*[(1e9*(c-35),{0})]for c in s]
G[S][1]=1,{S}
H=[(1,S,1)]
while H:w,p,d=heappop(H);q=1+F(10)*d;P(p+q,d);P(p-q,d);P(p,1-d,1e3)
A,B=min(G[F(69)])
print(A,len(B))
