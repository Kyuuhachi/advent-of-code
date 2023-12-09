import numpy as np
input = [np.array([int(a) for a in line.split()]) for line in open("09.in")]

def calc(v):
	def inner(v):
		a = np.diff(v)
		if np.all(a == 0):
			a = np.concatenate([a, [0]])
		else:
			a = inner(a)
		return np.concatenate([[v[0]], a]).cumsum()
	return inner(v)[-1]
print(sum(calc(v) for v in input))
print(sum(calc(v[::-1]) for v in input))
