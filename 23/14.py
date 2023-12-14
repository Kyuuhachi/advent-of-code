import numpy as np

input = np.array([list(i) for i in open("14.in").read().splitlines()])
input = np.pad(input, 1, constant_values='#')

w = input == '#'
def tilt(o, w):
	while True:
		a = o
		b = np.roll(~o & ~w, 1, axis=0)
		k = a & b
		if not k.sum(): break
		o[k] = False
		o[np.roll(k, -1, axis=0)] = True
	return o

def score(grid):
	return (np.argwhere(grid[::-1])[:,0]).sum()

print(score(tilt(input == 'O', input == '#')))

g = input == 'O'
w = input == '#'
h = {}
for i in range(1,1000000):
	for j in range(4):
		g = tilt(g, w)
		g = np.rot90(g, -1)
		w = np.rot90(w, -1)
	bits = np.packbits(g).tobytes()
	if bits in h:
		period = i - h[bits]
		if i % period == 1000000000 % period:
			print(score(g), period, i)
			break
	h[bits] = i
