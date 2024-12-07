A = B = 0
def solve(val, *c):
 if not c: return(val == Q)*a
 item,*c=c
 v = 0
 if not val % item: v |= solve(val//item, *c)
 if val > item: v |= solve(val-item, *c)
 n = 10**len(str(item))
 if O and val % n == item: v |= solve(val//n, *c)
 return v

for line in open("07.in"):
 a,Q,*c,=map(int,line.replace(*': ').split())
 c=c[::-1]
 O=0;A+=solve(a,*c)
 O=1;B+=solve(a,*c)
print(A, B)
