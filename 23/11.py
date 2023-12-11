import numpy as np
input = np.array([list(i) for i in open("11.in").read().splitlines()])

v = np.all(input == '.', axis=1)
h = np.all(input == '.', axis=0)
sx, sy = np.nonzero(input == '#')

w = np.zeros_like(input[0,:], dtype="u8")
for a in sx:
	for b in sx:
		w[a:b] += 1
z = np.zeros_like(input[0,:], dtype="u8")
for a in sy:
	for b in sy:
		z[a:b] += 1
print((w + w*v + z + z*h).sum(dtype="u8"))
print((w + w*v*999999 + z + z*h*999999).sum(dtype="u8"))
