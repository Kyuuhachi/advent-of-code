E=[]
for L in open(0):E+=zip(map(int,('0'+L).split('-')),[-('-'in L),1])
n=d=0
for V,D in sorted(E):d-=D;n+=(D==0)*(d>0)+(V+(D>0))*D*(d+(D>0)==1)*1j
print(n)
