import numpy as np
input = np.array([list(i) for i in open("11.in").read().splitlines()])

g = np.array([[1, 1], [2, 1000000]])
def f(a):
	v = np.sum(input == '#', axis=a)
	w = np.cumsum(v[:-1]) * np.cumsum(v[:0:-1])[::-1]
	return w @ g[(v[:-1] == 0)+0]

print(f(0) + f(1))
