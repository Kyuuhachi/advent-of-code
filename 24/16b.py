s=open("16.in").read()
G=[2*[[-2,1e9][c!='#']]for c in s]
f=s.find
S=1,f('\n')+1
F=[(f('S'),0,1)]
for p,d,g in F:
 for p,g,k in(p,g,k:=S[d]),(p-k,g+1,-k):
  while G[p][d]>g:G[p][d]=g;F+=(p,1-d,g+1000),;p+=k;g+=1
e=f('E')
P=[(e,G[e][0]>G[e][1])]
for p,d in P:g=G[p][d]-1;P+=[(p,1-d)][G[p][1-d]-g+999:]+[(p+k,d)for k in[-S[d],S[d]]if G[p+k][d]==g]
print(min(G[e]),len(dict(P)))
