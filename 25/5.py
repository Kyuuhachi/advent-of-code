E=[]
for L in open(0):E+=zip(map(int,('0'+L).split('-')),[-('-'in L),1])
n=d=0
for V,D in sorted(E):d-=D;Q=D>0;n+=(D==0)*(d>0)+(V+Q)*D*(d+Q==1)*1j
print(n)
