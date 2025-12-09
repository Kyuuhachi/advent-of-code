P=[eval(x)for x in open(0)]
print(max(~(a-b)*~(c-d)for a,c in P for b,d in P))
Z=sorted
O=lambda A,B,C,D,E,F:(C-A)*(F-B)-(D-B)*(E-A)

def side(a, b, c, d):
 t  = O(*a,*b,*c)
 o1 = O(*a,*b,*d)
 o2 = O(*b,*c,*d)
 return Z((o1,o2))[t>0]<1

def segment_intersects_rect(a, b, c, d):
 ax, ay = a
 bx, by = b
 cx, cy = c
 dx, dy = d

 xmin, xmax = Z((cx, dx))
 ymin, ymax = Z((cy, dy))

 if ax == bx:
  symin, symax = Z((ay, by))
  return xmin < ax < xmax and max(symin, ymin) < min(symax, ymax)
 else:
  sxmin, sxmax = Z((ax, bx))
  return ymin < ay < ymax and max(sxmin, xmin) < min(sxmax, xmax)

n=0
m = 0
k=0
for A,(x,y),B in zip(P[-1:]+P,P,P[1:]+P):
 k+=1
 print(k,end="\r")
 for ox, oy in P:
  s=~abs(x-ox)*~abs(y-oy)
  if s<=m or side(A,(x,y),B,(ox,oy)): continue
  for a,b in zip(P,P[1:]+P):
   n+=1
   if segment_intersects_rect(a,b,(x,y),(ox,oy)):
    break
  else:
    m = s
print(m)
print("checks:", n)
