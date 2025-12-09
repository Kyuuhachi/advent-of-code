P=[eval(x)for x in open(0)]
print(max(~(a-b)*~(c-d)for a,c in P for b,d in P))

def orient(a, b, c):
 return (b[0] - a[0])*(c[1] - a[1]) - (b[1] - a[1])*(c[0] - a[0])

def side(a, b, c, d):
 t  = orient(a, b, c)
 o1 = orient(a, b, d)
 o2 = orient(b, c, d)
 s = min(o1,o2) if t>0 else max(o1,o2)
 return (s>0)-(s<0)

def segment_intersects_rect(a, b, c, d):
 ax, ay = a
 bx, by = b
 cx, cy = c
 dx, dy = d

 xmin, xmax = sorted((cx, dx))
 ymin, ymax = sorted((cy, dy))

 if ax == bx:
  symin, symax = sorted((ay, by))
  return xmin < ax < xmax and max(symin, ymin) < min(symax, ymax)
 else:
  sxmin, sxmax = sorted((ax, bx))
  return ymin < ay < ymax and max(sxmin, xmin) < min(sxmax, xmax)

n=0
m = 0
k=0
for A,(x,y),B in zip(P[-1:]+P,P,P[1:]+P):
 k+=1
 print(k,end="\r")
 for ox, oy in P:
  s=~abs(x-ox)*~abs(y-oy)
  if s<=m or side(A,(x,y),B,(ox,oy))<1: continue
  for a,b in zip(P,P[1:]+P):
   n+=1
   if segment_intersects_rect(a,b,(x,y),(ox,oy)):
    break
  else:
    m = s
print(m)
print("checks:", n)
