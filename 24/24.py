A,X,O={},{},{}
for l in open("24.in"):
 match l.split():
  case [a,b,c,d,e]:G=globals()[b[0]];G[a,c]=G[c,a]=e

m=[]
K='x00','y00'
c,p=X[K],A[K]
assert c == 'z00', c
n=1
while 1:
 N="%02d"%n
 K='x'+N,'y'+N
 if K not in X:break
 if'z'<p:c,p=p,c;m+=c,p
 a,b=X[K],A[K]
 if(p,b)in X:a,b=b,a;m+=a,b
 c,d=X[p,a],A[p,a]
 if'z'<b:c,b=b,c;m+=c,b
 if'z'<d:c,d=d,c;m+=c,d
 p=O[d,b]
 n+=1
print(*sorted(m),sep=',')
