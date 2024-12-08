s=open("08.in",'rb').read()
m=[set()for _ in range(256)]
w=s.find(10)+1
i=0
for c in s:m[c]|={i//w+i%w*1j};i+=1
m[10]=m[46]=[]
R=range(w-1)
f=lambda f,g:len({v for n in m for p in n for q in n for d in g if f(n,v:=p+(p-q)*d)}&{i+j*1j for i in R for j in R})
print(f(lambda n,v:{v}-n,[1]),f(lambda n,v:1,R))
