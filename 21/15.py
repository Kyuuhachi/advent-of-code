import numpy as np
import dataclasses as D
import heapq
a = np.array([[int(a) for a in line.strip()] for line in open("15.in")])

def dijk(a):
	weight = np.zeros_like(a)
	@D.dataclass
	class Node:
		y: int
		x: int
		def __lt__(self, other):
			return weight[self.y, self.x] < weight[other.y, other.x]

	q = [Node(0, 0)]
	while q:
		i = heapq.heappop(q)
		if i == Node(a.shape[0]-1, a.shape[1]-1):
			return weight[i.y, i.x]
		for j in [ Node(i.y+1, i.x), Node(i.y, i.x+1), Node(i.y-1, i.x), Node(i.y, i.x-1) ]:
			if 0 <= j.y < a.shape[0] and 0 <= j.x < a.shape[1] and weight[j.y, j.x] == 0:
				weight[j.y, j.x] = weight[i.y, i.x] + a[j.y, j.x]
				heapq.heappush(q, j)

print(dijk(a))

b = a[None, :, None, :]
b = b + [[[[0]]],[[[1]]],[[[2]]],[[[3]]],[[[4]]]]
b = b + [[[[0],[1],[2],[3],[4]]]]
b = (b-1)%9+1
b = b.reshape(b.shape[0]*b.shape[1], b.shape[2]*b.shape[3])
print(dijk(b))
