E=[]
for L in open(0):E+=zip(map(int,L.split('-')),[-1,1])if'-'in L else[(int('0'+L),0)]
n=m=d=0
for V,D in sorted(E):
 d+=D<0
 n+=(D==0)*(d>0)
 m+=(V+(D>0))*D*(d==1)
 d-=D>0
print(n,m)
