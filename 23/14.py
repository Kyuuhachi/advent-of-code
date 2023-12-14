import numpy as np

input = np.array([list(i) for i in open("14.in").read().splitlines()])
input = np.pad(input, 1, constant_values='#')

def tilt(grid):
	while True:
		a = grid == 'O'
		b = np.roll(grid, 1, axis=0) == '.'
		k = a & b
		if not k.sum(): break
		grid[k] = '.'
		grid[np.roll(k, -1, axis=0)] = 'O'
	return grid

def score(grid):
	return (np.argwhere(grid[::-1] == 'O')[:,0]).sum()

print(score(tilt(np.copy(input))))

g = np.copy(input)
h = {}
for i in range(1,1000000):
	for j in range(4):
		g = tilt(g)
		g = np.rot90(g, -1)
	bits = np.packbits(g == 'O').tobytes()
	if bits in h:
		period = i - h[bits]
		if i % period == 1000000000 % period:
			print(score(g), period, i)
			break
	h[bits] = i
