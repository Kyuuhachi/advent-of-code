s=open("16.in").read()
G=[2*[-2 if c=='#'else 1e9]for c in s]
S=1,s.find('\n')+1
def A(p,d,g,j):
 while G[p][d]>g:G[p][d]=g;F.append((p,1-d,g+1000));p+=S[d]*j;g+=1
F=[(s.find('S'),0,1)]
for p,d,g in F:A(p,d,g,-1);A(p+S[d],d,g+1,1)
e=s.find('E')
P=[(e,G[e][0]>G[e][1])]
for p,d in P:
 g=G[p][d]
 P+=[(p,1-d)]*(G[p][1-d]==g-1000)
 for k in-S[d],S[d]:P+=[(p+k,d)]*(G[p+k][d]==g-1)
print(min(G[e]),len({a for a,b in P}))
