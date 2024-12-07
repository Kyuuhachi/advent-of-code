A = 0
for l in open("07.in"):
 a,b,*c=map(int,l.replace(':','').split())
 p={b}
 for c in c:
  p = {v*c for v in p}|{v+c for v in p}
 A += a*(a in p)
print(A)
A = 0
for l in open("07.in"):
 a,b,*c=map(int,l.replace(':','').split())
 p={b}
 for c in c:
  p = {v*c for v in p}|{v+c for v in p}|{int(f"{v}{c}") for v in p}
 A += a*(a in p)
print(A)
