s=open("08.in",'rb').read()
m=[set()for _ in range(256)]
w=s.find(10)+1
for i,c in enumerate(s):m[c]|={i//w+i%w*1j}
m[10]=m[46]=[]
R=range(w-1)
a={(i+j*1j)for i in R for j in R}
A={
 P
 for n in m
 for p in n
 for q in n
 for d in[1]
 if{P:=p+(p-q)*d}-n
}&a
B={
 p+(p-q)*d
 for n in m
 for p in n
 for q in n
 for d in R
}&a
print(len(A),len(B))
