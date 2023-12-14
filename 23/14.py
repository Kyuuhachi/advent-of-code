import numpy as np

input = np.array([list(i) for i in open("14.in").read().splitlines()])
input = np.pad(input, 1, constant_values='#')

w = input == '#'
def tilt(o, w):
	while True:
		k = o & np.roll(~o & ~w, 1, axis=0)
		if not k.sum(): break
		o = o & ~k | np.roll(k, -1, axis=0)
	return o

def score(grid):
	return (np.argwhere(grid[::-1])[:,0]).sum()

print(score(tilt(input == 'O', input == '#')))

o = input == 'O'
w = input == '#'
h = {}
for i in range(1,1000000):
	for j in range(4):
		o = tilt(o, w)
		o = np.rot90(o, -1)
		w = np.rot90(w, -1)
	bits = np.packbits(o).tobytes()
	if bits in h:
		period = i - h[bits]
		if i % period == 1000000000 % period:
			print(score(o), period, i)
			break
	h[bits] = i
