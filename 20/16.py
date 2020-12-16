lines = open("16.in").read().split("\n\n")
fields = [
	tuple(
		tuple(int(x) for x in r.split("-"))
		for r in line.split(": ")[1].split(" or ")
	)
	for line in lines[0].splitlines()
]
yours = tuple(int(x) for x in lines[1].splitlines()[1].split(","))
nearby = [
	tuple(int(x) for x in line.split(","))
	for line in lines[2].splitlines()[1:]
]

# Part 1
validSet = set.union(*(
	set(range(a,b+1)) | set(range(c,d+1))
	for (a, b), (c, d) in fields
))
print(sum(
	x
	for w in nearby
	for x in w
	if x not in validSet
))

# Part 2
import numpy as np
t = np.array([
	w
	for w in nearby
	if set(w) <= validSet
])
xs = np.array([
	(((a <= t) & (t <= b)) | ((c <= t) & (t <= d))).all(axis=0)
	for (a,b),(c,d) in fields
])
assert sorted(xs.sum(axis=1)) == list(range(1,len(xs)+1))

ys = np.argsort(xs.sum(axis=1))
xs[ys[1:]] ^= xs[ys[:-1]]
assert (xs.sum(axis=0) == 1).all()
assert (xs.sum(axis=1) == 1).all()
xs = np.argmax(xs, axis=1)
print(np.product(np.array(yours)[xs][:6]))
