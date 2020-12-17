import numpy as np
import itertools

g = np.array([
	[ a == "#" for a in l ]
	for l in open("17.in").read().splitlines()
])

def life(p, n):
	shifts = list(itertools.product((slice(2,None),slice(1,-1),slice(0,-2)), repeat=p.ndim))
	for _ in range(n):
		q = np.pad(p, 1, mode="wrap")
		y = np.array([q[a] for a in shifts]).sum(axis=0)
		p = (y == 3) | p & (y == 4)
	return p.sum()

# Part 1
print(life(np.pad(g[None], 6), 6))

# Part 2
print(life(np.pad(g[None,None], 6), 6))
