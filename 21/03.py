import numpy as np

bits = np.array([[a=="1" for a in a.strip()] for a in open("03.in")])

def to_int(a):
	return int(np.packbits(a[::-1], bitorder="little").view("u2")[0])

def common(a):
	return 2*a.sum(axis=0) >= a.shape[0]

print(to_int(common(bits)) * to_int(~common(bits)))

a = bits
b = bits
for c in range(bits.shape[1]):
	if len(a) > 1: a = a[a[:,c] == common(a[:,c])]
	if len(b) > 1: b = b[b[:,c] != common(b[:,c])]
print(to_int(a[0]) * to_int(b[0]))
