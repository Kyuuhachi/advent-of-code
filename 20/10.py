import numpy as np
import itertools as it
ns = [int(x) for x in open("10.in").read().splitlines()]

# Part 1
xs = np.array([0] + sorted(ns) + [max(ns) + 3])
xs = xs[1:] - xs[:-1]
print(np.sum(xs == 1) * np.sum(xs == 3))

# Part 2
n = 1
for a, b in it.groupby(xs):
	b = len(list(b))
	assert a in {1, 3}
	assert 1 <= b <= 4
	if a == 1:
		n *= [None, 1, 2, 4, 7][b]
print(n)
