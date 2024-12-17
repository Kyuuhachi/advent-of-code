s=open("16.in").read()
G=[2*[[-2,1e9][c!='#']]for c in s]
S=1,s.find('\n')+1
def A(p,d,g,k):
 while G[p][d]>g:G[p][d]=g;F.append((p,1-d,g+1000));p+=k;g+=1
F=[(s.find('S'),0,1)]
for p,d,g in F:k=S[d];A(p,d,g,-k);A(p+k,d,g+1,k)
e=s.find('E')
P=[(e,G[e][0]>G[e][1])]
for p,d in P:
 g=G[p][d]-1;P+=[(p,1-d)]*(G[p][1-d]==g-999)
 for k in-S[d],S[d]:P+=[(p+k,d)]*(G[p+k][d]==g)
print(min(G[e]),len({a for a,b in P}))
