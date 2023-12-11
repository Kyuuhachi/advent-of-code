import numpy as np
input = np.array([list(i) for i in open("11.in").read().splitlines()])

v = np.all(input == '.', axis=1)
h = np.all(input == '.', axis=0)
sx, sy = np.nonzero(input == '#')

n = 0
for r1, c1 in zip(sx, sy):
	for r2, c2 in zip(sx, sy):
		(r1_, r2_) = min(r1, r2), max(r1, r2)
		(c1_, c2_) = min(c1, c2), max(c1, c2)
		x = r2_ - r1_ + v[r1_:r2_].sum() + c2_ - c1_ + h[c1_:c2_].sum()
		n += x
print(n / 2)

n = 0
for r1, c1 in zip(sx, sy):
	for r2, c2 in zip(sx, sy):
		(r1_, r2_) = min(r1, r2), max(r1, r2)
		(c1_, c2_) = min(c1, c2), max(c1, c2)
		x = r2_ - r1_ + v[r1_:r2_].sum() * 999999 + c2_ - c1_ + h[c1_:c2_].sum() * 999999
		n += x
print(n / 2)
