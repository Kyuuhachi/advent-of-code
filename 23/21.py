import numpy as np
input = np.array([list(line) for line in open("21.in").read().splitlines()])

def run(input, steps):
	input1 = np.pad(input, 1, constant_values='#')
	wall = input1 == '#'
	yes = np.zeros_like(wall)
	yes[yes.shape[0]//2,yes.shape[1]//2] = True

	for _ in range(steps):
		x = np.roll(yes, 1, axis=0) | np.roll(yes, -1, axis=0) \
			| np.roll(yes, 1, axis=1) | np.roll(yes, -1, axis=1)
		yes = x & ~wall
	return yes[1:-1,1:-1]

print(run(input, 64).sum())

assert input.shape == (131, 131)
assert input[65,65] == 'S'
N = 26501365
assert N % 131 == 65

vals = []
for n in range(3):
	g = np.tile(input, (1+2*n,1+2*n))
	f = run(g, 131*n+65)
	vals.append(f.sum())

c = np.diff(vals, 2)[0] // 2
b = np.diff(vals, 1)[0] - c
a = np.diff(vals, 0)[0]
assert np.all(np.diff(vals, 3) == 0)

n = N // 131
print(c*n**2 + b*n + a)
