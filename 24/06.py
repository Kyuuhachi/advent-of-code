s=open("06.in").read()
w=s.find('\n')+1
D=-w,1,w,-1
m=set()
K=set()
def run(p,d,v,P):
 if{P}<K:return
 K.add(P)
 while 1:
  N=p+D[d%4]
  n=s[N:][:1]
  if P==s:run(p,d,{*v},N)
  if{k:=(p,d%4)}<v:m.add(P);n=''
  v.add(k)
  if'#'>n or N<0:break
  if'#'==n or N==P:d+=1
  else:p=N

run(s.find('^'),0,v:=set(),s)
print(len({a for a,_ in v}),len(m))
