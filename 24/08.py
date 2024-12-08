s=open("08.in",'rb').read()
m=[[]for _ in range(256)]
w=s.find(10)+1
for i,c in enumerate(s):m[c]+=[(i//w,i%w)]
m[10]=m[46]=[]
R=range(w-1)
a={(i,j)for i in R for j in R}
A={
 (x,y)
 for n in m
 for p,q in n
 for r,s in n
 for d in[1]
 if (x:=p+(p-r)*d,y:=q+(q-s)*d) not in n
}&a
B={
 (x,y)
 for n in m
 for p,q in n
 for r,s in n
 for d in R
 if (x:=p+(p-r)*d,y:=q+(q-s)*d)
}&a
print(len(A),len(B))
