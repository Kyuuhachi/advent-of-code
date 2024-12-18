s=open("16.in").read()
G=[2*[1e9*(c>s)-2]for c in s]
f=s.find
S=1,f('\n')+1
F=[(f('S'),0,1)]
for p,d,g in F:
 for p,g,k in(p,g,k:=S[d]),(p-k,g+1,-k):
  while G[p][d]>g:G[p][d]=g;g+=1;F+=(p,1-d,g+999),;p+=k
e=f('E')
T=G[e]
P=[(e,T[0]>T[1])]
for p,d in P:g=G[p][d]-1;P+=[(p,1-d)][G[p][1-d]-g+999:]+[(p+k,d)for k in[-S[d],S[d]]if G[p+k][d]==g]
print(min(T),len(dict(P)))
