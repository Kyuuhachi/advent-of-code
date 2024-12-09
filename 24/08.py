s=open("08.in",'rb').read()
m=[set()for _ in s]
i=j=0
for c in s:
 if c==10:j+=1j;i=0
 else:m[c]|={i+j};i+=1
A={0}.union(*m)
m[46]=[]
f=lambda f,g:len({v for n in m for p in n for q in n for d in g if f(v:=p+(p-q)*d,n)}&A)
print(f(lambda v,n:{v}-n,[1]),f(map,range(99)))
