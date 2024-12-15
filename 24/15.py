a,b=open("15.in",'rb').read().split(b"\n\n")
for*G,n in(0,1),(-1,0,1,2):
 w=a.find(10)*n+n
 r=a.find(64)*n
 B={i*n for i in range(len(a))if a[i]==79}
 W={i*n for i in range(len(a))if a[i]==35}
 for i in b:
  d={60:-1,62:1,94:-w,118:w,10:0}[i]
  v=set()
  R={r+d-g*g for g in G}
  S={i}
  while R-S:
   t,*_=R-S
   S|={t}
   if t in W:
    break
   if t in B:
    v|={t}
    R|={t+d+g for g in G}
  else:
   B-=v
   B|={v+d for v in v}
   r+=d
 print(sum(x%w+x//w*100 for x in B))
