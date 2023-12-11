import numpy as np
input = np.array([list(i) for i in open("11.in").read().splitlines()])

v = np.sum(input == '#', axis=1)
w = np.cumsum(v) * np.roll(np.cumsum(v[::-1])[::-1], -1)
w[-1] = 0

h = np.sum(input == '#', axis=0)
z = np.cumsum(h) * np.roll(np.cumsum(h[::-1])[::-1], -1)
z[-1] = 0

g = np.array([[1, 1], [2, 1000000]])
print(w @ g[(v == 0)+0] + z @ g[(h == 0)+0])
