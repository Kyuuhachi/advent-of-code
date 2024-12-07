s=open("06.in").read()
w=s.find('\n')+1
m=set()
def r(p,d,v,P,K={()}):
 while not{P}<K:
  N=p+[-w,1,w,-1][d];n=s[N:N+1]
  if P==s:r(p,d,{*v},N)
  if{k:=(p,d)}<v:m.add(P);n=''
  v|={k};p=[N,p][q:=n=='#'or N==P];d=d+q&3
  if'#'>n or N<0:K|={P}
r(s.find('^'),0,v:=set(),s)
print(len({a for a,_ in v}),len(m))
