s=open("08.in",'rb').read()
m=[[]for _ in range(256)]
w=s.find(10)+1
for i,c in enumerate(s):m[c]+=[(i//w,i%w)]
m[10]=m[46]=[]
A={
 (x,y)
 for n in m
 for p,q in n
 for r,s in n
 if (x:=p+p-r,y:=q+q-s)not in n
 if 0<x+1<w if 0<y+1<w
}
B={
 (x,y)
 for n in m
 for p,q in n
 for r,s in n
 for d in range(w)
 if (x:=p+(r-p)*d,y:=q+(s-q)*d)
 if 0<x+1<w if 0<y+1<w
}

print(len(A),len(B))

for i,c in enumerate(s):
 k=i//w,i%w
 if k in B:print(f"\x1B\x5B7m{c:c}\x1B\x5B0m",end="")
 else:print(chr(c),end="")
