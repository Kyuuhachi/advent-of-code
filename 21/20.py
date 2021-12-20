import numpy as np
import itertools

with open("20.in") as f:
	key = np.array([a == '#' for a in f.readline().strip()])
	f.readline()
	a = np.array([[a == '#' for a in line.strip()] for line in f])

shifts = list(itertools.product((slice(0,-2),slice(1,-1),slice(2,None)), repeat=2))
def enhance(p, fill=0):
	q = np.pad(p, 2, constant_values=fill)
	w = np.moveaxis(np.array([q[a] for a in shifts]), 0, 2)
	y = np.packbits(w[...,::-1], axis=-1, bitorder="little").view("u2")[...,0]
	return key[y]

b = a
for i in range(25):
	b = enhance(enhance(b), key[0])
	if i in (0, 24):
		print(b.sum())
