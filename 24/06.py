s=open("06.in").read()
pos=s.find('^')
w=s.find('\n')+1
stride=-w,1,w,-1
d=0

m=set()
K=set()
def run(pos,d,v,P):
 if P in K:return
 K.add(P)
 print(len(m))
 while 1:
  np=pos+stride[d%4]
  n=s[np:][:1]
  if P==s:run(pos,d,{*v},np)
  if'#'>n or np<0:break
  if'#'==n or np==P:d+=1
  else:pos=np
  if(pos,d%4)in v:m.add(P);break
  v.add((pos,d%4))

v={(pos,0)}
run(pos,0,v,s)
print(len({a for a,_ in v}),len(m))
