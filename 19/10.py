import numpy as np
from collections import defaultdict
import sys

grid = np.array([[i == "#" for i in l] for l in sys.stdin.read().splitlines()]).T
roids = np.argwhere(grid)
cross = roids[:,None]-roids[None,:]

angs = np.arctan2(-cross[:,:,0], cross[:,:,1])
angs[np.diag_indices_from(angs)] = float("nan")
dist = np.linalg.norm(cross, axis=2)

counts = np.array([len(set(l))-1 for l in angs])
print(counts.max())
pos = counts.argmax()

x = angs[pos] % (2*np.pi)
d = defaultdict(list)
for a in np.lexsort((dist[pos],x)):
	d[x[a]].append(roids[a])

d = list(d.values())
l = []
for a in d:
	l.append(a.pop(0))
	if a: d.append(a)

print(l[199])
