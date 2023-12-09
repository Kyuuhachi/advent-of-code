import numpy as np
input = [np.array([int(a) for a in line.split()]) for line in open("09.in")]

def calc(v):
	return 0 if np.all(v == 0) else calc(np.diff(v)) + v[-1]
print(sum(calc(v) for v in input))
print(sum(calc(v[::-1]) for v in input))
