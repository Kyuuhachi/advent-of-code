s=open("08.in",'rb').read()
m=[set()for _ in s]
A={0}
i=0
for c in s:
 if c-10:m[c]|={i};i+=1j;A|=m[c]
 else:i=i.real+1
m[46]=[]
f=lambda f,g:len({p+d*(p-q)for n in m for p in n for q in n for d in range(f,g)if p-q}&A)
print(f(1,2),f(0,99))
