import numpy as np
import sympy as sp
hail = []
for line in open("24.in").read().splitlines():
	pos, vel = line.split(" @ ")
	hail.append((
		np.fromiter((int(p) for p in pos.split(", ")), "i8"),
		np.fromiter((int(v) for v in vel.split(", ")), "i8"),
	))
hail = np.array(hail)

n = 0
for i, l1 in enumerate(hail):
	for j, l2 in enumerate(hail[i+1:], i+1):
		nant = lambda a, b: a[1]*b[0] - a[0]*b[1]
		d = l2[0] - l1[0]
		det = nant(l1[1], l2[1])
		if det == 0:
			continue
		u = nant(d, l2[1]) / det
		v = nant(d, l1[1]) / det
		if u > 0 and v > 0:
			p = l1[0] + l1[1] * u
			if all(200000000000000 <= p <= 400000000000000 for p in p[:2]):
				n += 1
print(n)

time = sp.symbols("a b c")
pos = sp.symbols("px py pz")
vel = sp.symbols("dx dy dz")
eq = [
	(h[0][i] + h[1][i] * w) - (pos[i]+vel[i]*w)
	for h, w in zip(hail, time)
	for i in range(3)
]
sol, = sp.solve(eq, [*time, *vel, *pos])
for q in eq: print(q)
print(sol)
print(sum(sol[-3:]))
