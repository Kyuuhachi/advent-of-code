s=open("08.in",'rb').read()
m=[set()for _ in s]
A={0}
i=0
for c in s:
 if c-10:m[c]|={i};i+=1j;A|=m[c]
 else:i=i.real+1
m[46]=[]
for g in[1],range(99):print(len({p+d*(p-q)for n in m for p in n for q in n-{p}for d in g}&A))
