A = B = 0
def solve(partb, a, b, *c):
 l = [a]
 for item in c[::-1]:
  m = []
  for val in l:
   if not val % item: m.append(val//item)
   if val > item: m.append(val-item)
   n = 10**len(str(item))
   if partb and val % n == item: m.append(val//n)
  l = m
 return(b in l)*a

for line in open("07.in"):
 *v,=map(int,line.replace(*': ').split())
 A+=solve(False, *v)
 B+=solve(True, *v)
print(A, B)
