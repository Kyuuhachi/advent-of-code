R=[]
for L in(I:=open(0)):
 if'.'>L:break
 A,B=map(int,L.split('-'))
 R+=(A,B+1),
R.sort()
n=m=0
for L in I:n+=any(A<=int(L)<B for A,B in R)
P=0
for A,B in R:m-=max(A,P)-(P:=max(B,P))
print(n,m)
