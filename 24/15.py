a,b=open("15.in").read().split("\n\n")
w=a.find('\n')+1

r=a.find('@')
B={i for i in range(len(a))if a[i]=='O'}
W={i for i in range(len(a))if a[i]=='#'}
for i in b:
 if i=='\n':continue
 d={'<':-1,'>':1,'^':-w,'v':w,'\n':0}[i]
 v=set()
 R={r}
 while R:
  t=R.pop()
  if t+d in W:break
  if t+d in B:R|={t+d}
  v|={t}
 else:
  v-={r}
  B-=v
  B|={v+d for v in v}
  r+=d
print(sum(x%w+x//w*100 for x in B))

w*=2
r=a.find('@')*2
B={i*2 for i in range(len(a))if a[i]=='O'}
W={i*2 for i in range(len(a))if a[i]=='#'}
for i in b:
 if i=='\n':continue
 d={'<':-1,'>':1,'^':-w,'v':w,'\n':0}[i]
 v=set()
 R={r+d,r+d-1}
 S={i}
 while R-S:
  t,*_=R-S
  S|={t}
  if t in W:
   break
  if t in B:
   v|={t}
   R|={t+d+g for g in[-1,0,1]}
 else:
  B-=v
  B|={v+d for v in v}
  r+=d
print(sum(x%w+x//w*100 for x in B))
