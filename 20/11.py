import numpy as np
import numpy.ma as ma

# There's gotta be some better way to do this
g = np.array([
	[
		{".": -1, "L": 0, "#": 1}[a]
		for a in l
	] for l in open("11.in").read().splitlines()
])
g = ma.array(g.astype(bool), mask=(g==-1))

def run(x, maxstep, n):
	ng = neighbors(x, maxstep)
	while True:
		x0 = x
		N = x[ng].sum(axis=-1)
		x = np.choose(x, (N == 0, N < n))
		if np.all(x == x0): break
	return x.sum()

def neighbors(x, maxstep):
	ix = np.array(np.meshgrid(*map(range,x.shape))).T[:,:,None,:]
	off = np.array([(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)])[None,None,:,:]

	# An arbitrary index pointing to an empty cell value. I'd prefer to use
	# a masked array, but that doesn't seem to be possible for various reasons.
	inv = tuple(np.transpose(np.where(x == ma.masked))[0])

	y = np.full_like(ix + off, inv)
	for n in range(1, maxstep+1):
		m = x.mask[tuple(np.rollaxis(y,-1))]
		y[m] = (ix+off*n)[m]
		y[~((0 <= y) & (y < x.shape)).all(axis=-1)] = inv

	return tuple(np.rollaxis(y,-1))

# Part 1
print(run(g, 1, 4))

# Part 2
print(run(g, max(g.shape), 5))
