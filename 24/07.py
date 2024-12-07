A=B=0
k=lambda c,p:{v*c for v in p}|{v+c for v in p}
for l in open("07.in"):
 a,b,*c=map(int,l.replace(':','').split())
 p={b};q={b}
 for c in c:
  p = k(c,p)
  q = k(c,q)|{int(f"{v}{c}") for v in q}
 A += a*(a in p)
 B += a*(a in q)
print(A,B)
