E=[]
for L in open(0):E+=zip(map(int,('0'+L).split('-')),[-('-'in L),1])
n=d=0
for V,D in sorted(E):
 d+=D<0
 n+=(D==0)*(d>0)+(V+(D>0))*D*(d==1)*1j
 d-=D>0
print(n)
