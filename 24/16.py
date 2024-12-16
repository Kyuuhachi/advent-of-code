from heapq import*
s=open("16.in",'rb').read()
w=s.find(10)+1
S=s.find(83)
E=s.find(69)

W=[1,w,-1,-w]
r=lambda n:W[W.index(n)-1]

D=[S*[(1e9*(c!=35),0)]for c in s]
d=D[S][1]=(1,{S})
H=[(*d,S,1)]
while H:
 w,l,p,d=heappop(H)
 q,m=D[p][d]
 if w>q:continue
 if w<q:D[p][d]=w,l|l
 else:m|=l
 heappush(H,(w+1,l|{p+d},p+d,d))
 heappush(H,(w+1e3,l,p,r(d)))
 heappush(H,(w+1e3,l,p,r(-d)))
A,B=min(D[E])
print(A,len(B))
