G={L[:3]:L[4:].split()for L in open(0)}
from functools import*
R=cache(lambda a,b:(a==b)+sum(R(c,b)for c in G.get(a,())))
A,B,C,D,E="you out svr fft dac".split()
print(R(A,B),R(C,D)*R(D,E)*R(E,B)+R(C,E)*R(E,D)*R(D,B))
