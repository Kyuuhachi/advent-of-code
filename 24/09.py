*s,=map(int,open("09.in").read().strip())
def Z(z):
 n=0
 R=[]
 H=[]
 for i,w in enumerate(s):
  if~i%2:R+=[[n,w,i//2]]if z else[[n+m,1,i//2]for m in range(w)]
  else:H+=[[n,w]]
  n+=w
 for r in R[::-1]:
  for h in H:
   if h[1]>=r[1]:r[0]=h[0];h[0]+=r[1];h[1]-=r[1];h[1]or H.remove(h)
   if h[0]>=r[0]:break
 print(sum(i*k*(2*a+k-1)//2 for a,k,i in R))
Z(0)
Z(1)
