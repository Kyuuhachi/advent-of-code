import numpy as np
input = [np.array([int(a) for a in line.split()]) for line in open("09.in")]

def calc(v):
	w = v if np.all(v == 0) else calc(np.diff(v))
	return np.concatenate([[v[0]], w]).cumsum()
print(sum(calc(v)[-1] for v in input))
print(sum(calc(v[::-1])[-1] for v in input))
