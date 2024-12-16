from heapq import*
s=open("16.in",'rb').read()

def P(W,P,D):
 W+=w;q,m=G[P][D];o=G[p][d][1]|{P}
 if W>q:return
 if W<q:G[P][D]=W,o
 else:m|=o
 heappush(H,(W,P,D))

F=s.find
S=F(83)
G=[S*[(1e9*(c!=35),0)]for c in s]
G[S][1]=(1,{S})
H=[(1,S,1)]
while H:w,p,d=heappop(H);P(1,p+d,d);P(1,p-d,d);P(1e3,p,d^1^F(10)+1)
A,B=min(G[F(69)])
print(A,len(B))
