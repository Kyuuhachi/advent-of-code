a,b=open("15.in").read().split("\n\n")
w=a.find('\n')+1
D={'<':-1,'>':1,'^':-w,'v':w,'\n':0}

g=list(a)
r=g.index('@')
for i in b:
 print(f"move {i}")
 d=D[i]
 R=r
 while g[R+d]=='O':R+=d
 if g[R+d]!='#':
  g[r],g[R+d],g[r+d]='.O@'
  r+=d
 print("".join(g))
print(sum(x%w+x//w*100 for x,c in enumerate(g)if c=='O'))
