a,b=open("15.in").read().split("\n\n")
def F(n,*G):
 w=a.find('\n')*n+n
 r=a.find('@')*n
 B={i*n for i in range(len(a))if a[i]=='O'}
 W={i*n for i in range(len(a))if a[i]=='#'}
 for i in b:
  d={'<':-1,'>':1,'^':-w,'v':w,'\n':0}[i]
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
F(1,0)
F(2,-1,0,1)
