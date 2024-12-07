m=set()
def r(P,p,d,v,K={()}):
 while{P}-K:
  N=p-[w:=s.find('\n')+1,-1,-w,1][d];n=s[N:N+1]
  if P==s:r(N,p,d,{*v})
  if{k:=(p,d)}<v:m.add(P);n=s
  v|={k};p=[N,p][q:=n=='#'or N==P];d=d+q&3
  if'#'>n or N<0:K|={P}
r(s:=open("06.in").read(),s.find('^'),0,v:=set())
print(len({a for a,_ in v}),len(m))
