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
 if len(v)%100==0:print(''.join('o' if p in v else s[p] for p in range(len(s))))
print(len(v))


