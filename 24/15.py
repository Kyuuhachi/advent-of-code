a,b=open("15.in").read().split("\n\n")
w=a.find('\n')+1
D={'<':-1,'>':1,'^':-w,'v':w,'\n':0}

g=list(a)
r=g.index('@')
for i in b:
 d=D[i]
 R=r
 while g[R+d]=='O':R+=d
 if g[R+d]!='#':
  g[r],g[R+d],g[r+d]='.O@'
  r+=d
print(sum(x%w+x//w*100 for x,c in enumerate(g)if c=='O'))

r=a.find('@')
B={i for i in range(len(a))if a[i]=='O'}
for i in b:
 if i=='\n':continue
 d=D[i]
 R=r
 while R+d in B:R+=d
 if a[R+d]!='#':
  if r+d in B:
   B-={r+d}
   B|={R+d}
  r+=d
print(sum(x%w+x//w*100 for x in B))

r=a.index('@')*2
B={i*2 for i in range(len(a))if a[i]=='O'}
print(B)
