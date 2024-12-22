*s,=map(int,open("22.in").read().split())
def H(x):
 x ^= x << 6 & 0xFFFFFF
 x ^= x >> 5
 x ^= x << 11 & 0xFFFFFF
 return x

G={}
n = 0
for i in s:
 j = [i%10]
 for _ in range(2000):
  i = H(i)
  j.append(i%10)
 n += i
 g = {}
 j=j[::-1]
 for a,b,c,d,e in zip(j,j[1:],j[2:],j[3:],j[4:]):
  g[b-a,c-b,d-c,e-d] = e
 for k,v in g.items(): G[k]=G.get(k,0)+v
print(n)
print(max(G.values()))
