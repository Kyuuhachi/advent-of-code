P=[eval(x)for x in open(0)]
print(max(~(a-b)*~(c-d)for a,c in P for b,d in P))
s="""<svg xmlns="http://www.w3.org/2000/svg" version="1.1" viewBox="0 0 20 20" stroke-width="0.2">\n"""
s += f"""<rect width="20" height="20" fill="#777777"/>\n"""
s += f"""<path d="M{" ".join(f"{x},{y}"for x,y in P)}Z" fill="none" stroke="black"/>\n"""
for p in P:
 s += f"""<circle cx="{p[0]}" cy="{p[1]}" r="0.2" fill="black"/>\n"""

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

def check():
 if side((x0,y0),(x,y),(x2,y2),(ox,oy))<1: return 0
 for a,b in zip(P,P[1:]+P):
  if segment_intersects_rect(a,b,(x,y),(ox,oy)):
   return 1
 else:
  return 2

m = 0
k=0
for (x0,y0),(x,y),(x2,y2) in zip(P[-1:]+P,P,P[1:]+P):
 k+=1
 if k%100:print(k)
 for ox, oy in P:
  # if ox==x or oy==y:continue
  c = check()
  colors = ["#FF0000","#0000FF","#00FF00"]
  if c==2:
   m = max(m, ~abs(x-ox)*~abs(y-oy))

  s += f"""<line x1="{x}" y1="{y}" x2="{(3*x+ox)/4}" y2="{(3*y+oy)/4}" stroke="{colors[c]}" stroke-width="0.1" style="mix-blend-mode:screen"/>\n"""
s += "</svg>"
print(m)
open("9.svg","w").write(s)
