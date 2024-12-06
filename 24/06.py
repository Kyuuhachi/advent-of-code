s=open("06.in").read()
pos=s.find('^')
w=s.find('\n')+1
stride=-w,1,w,-1
d=0

v={pos}
while 1:
 np=pos+stride[d%4]
 n=s[np:][:1]
 if'#'>n or np<0:break
 if'#'==n:d+=1
 else:pos=np
 v.add(pos)
print(len(v))

S=s
x=0
for P in range(len(s)):
 if'.'!=s[P]:continue
 pos=s.find('^')
 d=0
 v={(pos,d%4)}
 # s=S[:P]+'#'+s[P+1:]
 print(P,x)

 while 1:
  np=pos+stride[d%4]
  n=s[np:][:1]
  if'#'>n or np<0:break
  if'#'==n or np==P:d+=1
  else:pos=np
  if(pos,d%4)in v:x+=1;break
  v.add((pos,d%4))
print(x)
