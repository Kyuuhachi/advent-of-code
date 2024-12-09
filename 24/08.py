s=open("08.in",'rb').read()
m=[set()for _ in s]
A={0}
i=j=0
for c in s:
 if c-10:m[c]|={i+j};i+=1;A|=m[c]
 else:j+=1j;i=0
m[46]=[]
f=lambda f,g:len({v for n in m for p in n for q in n for d in g if f(v:=p+(p-q)*d,n)}&A)
print(f(lambda v,n:{v}-n,[1]),f(map,range(99)))
