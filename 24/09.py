*s,=map(int,open("09.in").read().strip())
E=enumerate

a=[]
for i,w in E(s[::2]):a+=[i]*w
o=[]
for w in s:o+=a[:w];a=a[w:][::-1]
print(sum(i*v for i,v in E(o)))

n=0
R=[]
H=[]
for i,w in E(s):
 if~i%2:R+=[[n,w,i//2]]
 else:H+=[[n,w]]
 n+=w
for r in R[::-1]:
 print(r)
 for h in H:
  if h[1]>=r[1]:r[0]=h[0];h[0]+=r[1];h[1]-=r[1];h[1]or H.remove(h)
  if h[0]>=r[0]:break
print(sum(i*k*a+i*k*(k-1)//2 for a,k,i in R))
