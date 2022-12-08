import numpy as np
inp = np.array([[int(a) for a in line] for line in open("08.in").read().splitlines()], dtype="i1")

def parta(inp):
	max = np.maximum.accumulate(inp, axis=0)
	max = np.roll(max, 1, axis=0)
	max[0] = -1
	return inp > max

print(np.bitwise_or.reduce([
	np.rot90(parta(np.rot90(inp, n)), -n)
	for n in range(4)
]).sum())

def partb(inp):
	a = np.zeros_like(inp, dtype="u4")
	for i in range(len(inp)):
		max = np.maximum.accumulate(inp[i+1:], axis=0)
		a[i] = (max < inp[i]).sum(axis=0) + (max >= inp[i]).any(axis=0)
	return a

print(np.multiply.reduce([
	np.rot90(partb(np.rot90(inp, n)), -n)
	for n in range(4)
]).max())
