s=open("16.in",'rb').read()
w=s.find(10)+1
S=s.find(83)
E=s.find(69)

W=[1,w,-1,-w]
r=lambda n:W[W.index(n)-1]

def m(a,b,c,d):
 t,u=p.setdefault((a,b),[c,{a}])
 if c<t:u.clear()
 if c<=t:u|=d|{a}

K=[1e9,{S}]
p={};m(S,1,0,{S})
while 1:
 q={}
 while q!=p:
  q|=p
  for(a,b),(c,d)in q.items():
   if s[a+b]-35:m(a+b,b,c+1,d)

 k=min(p.get((E,v),K)for v in W)
 if k!=K:print(k[0],len(k[1]));break
 for(a,b),(c,d)in q.items():
  m(a,r(b),c+1e3,d)
  m(a,r(-b),c+1e3,d)

for i,c in enumerate(s):
 if i in k[1]:print('█',end='')
 else: print(chr(c),end='')

for v in sorted(p.items()):
 print(v)
