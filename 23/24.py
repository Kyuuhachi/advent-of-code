import numpy as np
POS, VEL = [], []
for line in open("24.in").read().splitlines():
	pos, vel = line.split(" @ ")
	POS.append(np.fromiter((int(p) for p in pos.split(", ")), "i8"))
	VEL.append(np.fromiter((int(v) for v in vel.split(", ")), "i8"))
POS, VEL = np.array(POS), np.array(VEL)

p = POS[:,:2]
v = VEL[:,:2]

d = p[:,None] - p[None,:]
det = np.cross(v[None,:], v[:,None], axis=-1)
a = np.cross(d, v[None,:], axis=-1) / det
b = np.cross(d, v[:,None], axis=-1) / det
q = p[:,None] + v[:,None] * a[:,:,None]
q = np.all((2e14 <= q) & (q <= 4e14), axis=-1)
print(np.tril(q & (a > 0) & (b > 0)).sum())

import sympy as sp
pos = np.array(sp.symbols("px py pz"))
vel = np.array(sp.symbols("dx dy dz"))
eq = np.cross(POS[:3] - [pos], VEL[:3] - [vel], axis=-1).flatten()
sol, = sp.solve(eq, [*vel, *pos])
for q in eq: print(q)
print(sol)
print(sum(sol[-3:]))
