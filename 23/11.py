import numpy as np
input = np.array([list(i) for i in open("11.in").read().splitlines()])

v = np.sum(input == '#', axis=1)
w = np.cumsum(v[:-1]) * np.cumsum(v[:0:-1])[::-1]

h = np.sum(input == '#', axis=0)
z = np.cumsum(h[:-1]) * np.cumsum(h[:0:-1])[::-1]

g = np.array([[1, 1], [2, 1000000]])
print(w @ g[(v[:-1] == 0)+0] + z @ g[(h[:-1] == 0)+0])
