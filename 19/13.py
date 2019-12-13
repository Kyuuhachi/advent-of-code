import intcode

def intcode_blocks(code):
	code = list(code)
	coro = intcode.intcode_raw(code)
	grid = {}
	try:
		while True:
			[_, x] = coro.send(None)
			[_, y] = coro.send(None)
			[_, t] = coro.send(None)
			grid[(x+y)] = t
	except StopIteration: pass
	return len([() for v in grid.values() if v == 2])

def intcode_play(code):
	code = list(code)
	code[0] = 2
	coro = intcode.intcode_raw(code)
	grid = {}
	score = 0
	pad, ball = None, None
	try:
		v = coro.send(None)
		while True:
			if v[0] == "output":
				[_, x] = v
				[_, y] = coro.send(None)
				[_, t] = coro.send(None)
				if (x, y) == (-1, 0): score = t
				else: grid[(x, y)] = t

				if t == 3: pad = x
				if t == 4: ball = x
				v = coro.send(None)
			else:
				show(grid)
				v = coro.send(np.sign(ball - pad))
	except StopIteration: pass
	return score

def show(grid):
	a = np.zeros(np.max(list(grid.keys()), axis=0)+(1,1), dtype=int)
	for k, j in grid.items(): a[k] = j
	print(a.T)

import sys
import numpy as np
code = [int(i) for i in sys.stdin.read().split(",")]

print(intcode_blocks(code))
print(intcode_play(code))
