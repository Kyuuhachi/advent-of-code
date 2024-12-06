s=open("06.in").read()
w=s.find('\n')+1
stride=-w,1,w,-1
m=set()
K=set()
def run(pos,d,v,P):
 if{P}<K:return
 K.add(P)
 while 1:
  np=pos+stride[d%4]
  n=s[np:][:1]
  if P==s:run(pos,d,{*v},np)
  k=(pos,d%4)
  if{k}<v:m.add(P);break
  v.add(k)
  if'#'>n or np<0:break
  if'#'==n or np==P:d+=1
  else:pos=np

run(s.find('^'),0,v:=set(),s)
print(len({a for a,_ in v}),len(m))
