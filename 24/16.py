from heapq import*
s=open("16.in",'rb').read()
w=s.find(10)+1
S=s.find(83)
E=s.find(69)

W={1:w,w:-1,-1:-w,-w:1}
def P(W,P,D):
 q,m=G[P][D]
 if W+w>q:return
 if W+w<q:G[P][D]=W+w,G[p][d][1]|{P}
 else:m|=G[p][d][1]|{P}
 heappush(H,(W+w,P,D))

G=[S*[(1e9*(c!=35),0)]for c in s]
G[S][1]=(1,{S})
H=[(1,S,1)]
while H:
 w,p,d=heappop(H)
 P(1,p+d,d)
 P(1e3,p,W[d])
 P(1e3,p,W[-d])
A,B=min(G[E])
print(A,len(B))
