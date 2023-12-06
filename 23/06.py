import numpy as np
inp = open("06.in")
a1 = inp.readline().removeprefix("Time:")
b1 = inp.readline().removeprefix("Distance:")

n = 1
for a, b in zip(map(int, a1.split()), map(int, b1.split())):
	r = np.arange(a)
	n *= np.sum(r * (a-r) > b)
print(n)

a = int(a1.replace(' ', ''))
b = int(b1.replace(' ', ''))
r = np.arange(a)
print(np.sum(r * (a-r) > b))
