import numpy as np
import numpy.ma as ma

with open("04.in") as f:
	ns = [int(n) for n in next(f).split(",")]
	grids = np.array(f.read().split()).astype("u4").reshape(-1, 5, 5)

a = ma.array(grids)
for n in ns:
	a.mask |= a == n
	win = (a.mask.all(axis=2) | a.mask.all(axis=1)).any(axis=1)
	for g in a[win]:
		print(g.sum(dtype="u4") * n)
	a = a[~win]
