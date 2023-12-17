import numpy as np
import heapq

input = np.array([list(int(i) for i in i) for i in open("17.in").read().splitlines()])

def run(y, x, rot, mn, mx):
	heap = [(0, y, x, rot, mn)]
	v = np.full((*input.shape, 4, mx), 1000000000)
	while heap:
		(score, y, x, rot, n) = heapq.heappop(heap)
		if score >= v[y, x, rot, n]:
			continue
		v[y, x, rot, n] = score

		def push(y, x, rot, n):
			if not (0 <= y < input.shape[0]) or not (0 <= x < input.shape[1]):
				return
			heapq.heappush(heap, (score+input[y,x], y, x, rot, n))
		def up(n): push(y-1, x, 0, n)
		def down(n): push(y+1, x, 1, n)
		def left(n): push(y, x-1, 2, n)
		def right(n): push(y, x+1, 3, n)

		match rot:
			case 0:
				if n+1 < mx: up(n+1)
				if n+1 >= mn: left(0); right(0)
			case 1:
				if n+1 < mx: down(n+1)
				if n+1 >= mn: left(0); right(0)
			case 2:
				if n+1 < mx: left(n+1)
				if n+1 >= mn: up(0); down(0)
			case 3:
				if n+1 < mx: right(n+1)
				if n+1 >= mn: up(0); down(0)
			case _: raise ValueError(y, x, rot)
	return v[-1,-1,:,mn:].min()
print(run(0, 0, 3, 0, 3))
print(run(0, 0, 3, 4, 10))
