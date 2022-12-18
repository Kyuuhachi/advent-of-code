import numpy as np
x = np.zeros((23,23,23), dtype=bool)
for l in open("18.in"):
	a, b, c = map(int, l.strip().split(","))
	x[a+1,b+1,c+1] = True

n = 0
for a in 0,1,2:
	for b in -1,1:
		n += (x & ~np.roll(x, b, axis=a)).sum()
print(n)

y = np.zeros_like(x)
y[0,:,:] = True
y[:,0,:] = True
y[:,:,0] = True
assert not np.any(x&y)
while True:
	p = y.sum()
	for a in 0,1,2:
		for b in -1,1:
			y |= np.roll(y, b, axis=a) & ~x
	if y.sum() == p:
		break

x = ~y
n = 0
for a in 0,1,2:
	for b in -1,1:
		n += (x & ~np.roll(x, b, axis=a)).sum()
print(n)
