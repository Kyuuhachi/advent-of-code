R=[]
for L in(I:=open(0)):
 if'.'>L:break
 R+=[*map(int,L.split('-'))],
*I,=I
n=P=0
for A,B in sorted(R):K,P=max(A,P),max(B+1,P);n+=sum(K<=int(i)<P for i in I)+(P-K)*1j
print(n)
