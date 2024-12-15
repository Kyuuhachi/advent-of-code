a,b=open("15.in",'rb').read().split(b"\n\n")
F=a.find
E=lambda C:{i*n for i,c in enumerate(a)if c==C}
for*G,n in(0,1),(-1,0,1,2):
 r=F(64)*n;B=E(79);W=E(35)
 for i in b:
  d=[0,-1,w:=F(10)*n+n,-w,1][i%23%5];v=set();R={r-d-g*g for g in G};S={i}
  while R-S:
   t,*_=R-S;S|={t}
   if{t}<W:break
   if{t}<B:v|={t};R|={t-d+g for g in G}
  else:B-=v;B|={v-d for v in v};r-=d
 print(sum(x%w+x//w*100 for x in B))
