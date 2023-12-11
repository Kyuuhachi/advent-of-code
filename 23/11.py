import numpy as np
input = np.array([list(i) for i in open("11.in").read().splitlines()])

v = np.sum(input == '#', axis=1)
w = np.cumsum(v) * np.roll(np.cumsum(v[::-1])[::-1], -1)
w[-1] = 0

h = np.sum(input == '#', axis=0)
z = np.cumsum(h) * np.roll(np.cumsum(h[::-1])[::-1], -1)
z[-1] = 0

print((w + w*(v==0) + z + z*(h==0)).sum(dtype="u8"))
print((w + w*(v==0)*999999 + z + z*(h==0)*999999).sum(dtype="u8"))
