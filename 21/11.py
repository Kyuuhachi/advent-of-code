import numpy as np
import itertools
a = np.array([[int(a) for a in line.strip()] for line in open("11.in")])

def step(a):
	a = a + 1
	flashed = np.zeros_like(a, dtype=bool)
	while True:
		next_flash = (a > 9) & ~flashed
		padded = np.pad(next_flash, 1, constant_values=False)
		a += np.sum([
			padded[2:,1:-1],
			padded[:-2,1:-1],
			padded[1:-1,2:],
			padded[1:-1,:-2],

			padded[2:,2:],
			padded[2:,:-2],
			padded[:-2,2:],
			padded[:-2,:-2],
		], axis=0)
		flashed |= next_flash
		if not next_flash.any():
			break
	a[flashed] = 0
	return a, flashed

b = a
nflash = 0
for _ in range(100):
	b, flashed = step(b)
	nflash += flashed.sum()
print(nflash)

b = a
for t in itertools.count(1):
	b, flashed = step(b)
	if flashed.all():
		print(t)
		break
