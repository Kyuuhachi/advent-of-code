I={}
A,X,O={},{},{}
for l in open("24.in"):
 match l.split():
  case k,v:I[k[:-1]]=int(v)
  case a,b,c,d,e:I[e]=b[0],a,c;G=globals()[b[0]];G[a,c]=G[c,a]=e

def f(k):
 match I[k]:
  case'X',a,b:return f(a)^f(b)
  case'O',a,b:return f(a)|f(b)
  case'A',a,b:return f(a)&f(b)
  case v:return v
z=0
for k in sorted(I)[::-1]:
 if'z'<k:z=z<<1|f(k)

m=[]
K='x00','y00'
c,p=X[K],A[K]
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
print(z,','.join(sorted(m)))
