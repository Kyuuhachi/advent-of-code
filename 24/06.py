s=open("06.in").read()
w=s.find('\n')+1
m=set()
K=set()
def run(p,d,v,P):
 while not{P}<K:
  N=p+[-w,1,w,-1][d]
  n=s[N:][:1]
  if P==s:run(p,d,{*v},N)
  if{k:=(p,d)}<v:m.add(P);n=''
  v.add(k)
  if'#'>n or N<0:break
  p=[N,p][q:='#'==n or N==P];d=d+q&3
 K.add(P)

run(s.find('^'),0,v:=set(),s)
print(len({a for a,_ in v}),len(m))
