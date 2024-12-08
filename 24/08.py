s=open("08.in",'rb').read()
m=[[]for _ in range(256)]
w=s.find(10)+1
for i,c in enumerate(s):m[c]+=[(i//w,i%w)]
m[10]=m[46]=[]
a={(i,j)for i in range(w-1)for j in range(w-1)}
A={
 (x,y)
 for n in m
 for p,q in n
 for r,s in n
 if (x:=p+p-r,y:=q+q-s)not in n
}&a
B={
 (x,y)
 for n in m
 for p,q in n
 for r,s in n
 for d in range(w)
 if (x:=p+(r-p)*d,y:=q+(s-q)*d)
}&a
print(len(A),len(B))
