*s,=map(int,open("09.in").read().strip())
E=enumerate

a=[]
for i,w in E(s[::2]):a+=[i]*w
o=[]
for w in s:o+=a[:w];a=a[w:][::-1]
print(sum(i*v for i,v in E(o)))

n=0
r=[]
for i,w in E(s):
 if~i%2:r+=[[n,w,i//2]]
 n+=w
for k in r[::-1]:
 print(k)
 for(a,b,c),(d,e,f)in zip(r,r[1:]):
  if d-a-b>=k[1] and a<k[0]:
   k[0]=a+b
   r.sort()
   break
print(sum(i*k*a+i*k*(k-1)//2 for a,k,i in r))
