A=B=0
for l in open("07.in"):
 a,b,*c=map(int,l.replace(':','').split())
 p={b};q={b}
 for c in c:
  p = {v*c for v in p}|{v+c for v in p}
  q = {v*c for v in q}|{v+c for v in q}|{int(f"{v}{c}") for v in q}
 A += a*(a in p)
 B += a*(a in q)
print(A,B)
