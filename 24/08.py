s=open("08.in",'rb').read()
m=[set()for _ in range(256)]
w=s.find(10)+1
for i,c in enumerate(s):m[c]|={(i//w,i%w)}
m[10]=m[46]=[]
R=range(w-1)
a={(i,j)for i in R for j in R}
A={
 P
 for n in m
 for p,q in n
 for r,s in n
 for d in[1]
 if{P:=(p+(p-r)*d,q+(q-s)*d)}-n
}&a
B={
 (p+(p-r)*d,q+(q-s)*d)
 for n in m
 for p,q in n
 for r,s in n
 for d in R
}&a
print(len(A),len(B))
