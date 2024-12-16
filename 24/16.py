from heapq import*
s=open("16.in",'rb').read()

def P(W,P,D):
 W+=w;q,m=G[P][D]
 if W>q:return
 if W<q:G[P][D]=W,G[p][d][1]|{P}
 else:m|=G[p][d][1]|{P}
 heappush(H,(W,P,D))

S=s.find(83)
G=[S*[(1e9*(c!=35),0)]for c in s]
G[S][1]=(1,{S})
H=[(1,S,1)]
while H:
 w,p,d=heappop(H)
 P(1,p+d,d)
 P(1,p-d,d)
 P(1e3,p,d^1^s.find(10)+1)
A,B=min(G[s.find(69)])
print(A,len(B))
