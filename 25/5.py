R=[]
for L in(I:=open(0)):
 if'.'>L:break
 A,B=map(int,L.split('-'))
 R+=(A,B+1),
*I,=I
n=m=0
P=0
for A,B in sorted(R):m-=(K:=max(A,P))-(P:=max(B,P));n+=sum(K<=int(i)<P for i in I)
print(n,m)
