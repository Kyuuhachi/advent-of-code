s=open("08.in",'rb').read()
m=[set()for _ in s]
w=s.find(10)+1
i=0
for c in s:m[c]|={i//w+i%w*1j};i+=1
m[10]=[]
A={0}.union(*m)
m[46]=[]
f=lambda f,g:len({v for n in m for p in n for q in n for d in g if f(v:=p+(p-q)*d,n)}&A)
print(f(lambda v,n:{v}-n,[1]),f(map,range(w)))
