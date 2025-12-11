G={L[:3]:L[4:].split()for L in open(0)}
from functools import*
R=cache(lambda a,b="out":(a==b)+sum(R(c,b)for c in G.get(a,())))
print(R("you"),R(C:="svr",D:="fft")*R(D,E:="dac")*R(E)+R(C,E)*R(E,D)*R(D))
