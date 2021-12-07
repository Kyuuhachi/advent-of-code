import numpy as np
n = np.array([int(a) for a in open("07.in").read().split(",")])

a = np.abs(n[None,:]-np.arange(n.min(), n.max()+1)[:,None])
print(a.sum(axis=1).min())
print((a*(a+1)//2).sum(axis=1).min())
