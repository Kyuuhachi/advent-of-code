*s,=map(int,open("22.in").read().split())
def H(x):
 x ^= x << 6 & 0xFFFFFF
 x ^= x >> 5
 x ^= x << 11 & 0xFFFFFF
 return x


o = []
n = 0
for i in s:
 j = [i%10]
 for _ in range(2000):
  i = H(i)
  j.append(i%10)
 n += i
 g = {}
 for a,b,c,d,e in zip(j,j[1:],j[2:],j[3:],j[4:]):
  p = (b-a,c-b,d-c,e-d)
  if p not in g: g[p] = e
 o.append(g)
print(n)

S={K for k in o for K in k}

v = 0
for i,D in enumerate(S):
 if i % 100 == 0: print(i, '/', len(S))
 banana = 0
 for k in o:
  banana += k.get(D, 0)
 v = max(v,banana)
print(v)
# 1450 too high
