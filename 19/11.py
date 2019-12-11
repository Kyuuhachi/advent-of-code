import intcode

def intcode_turtle(code, grid=None,mutate=False):
	if not mutate:
		code = list(code)
		grid = set(grid or {})
	coro = intcode.intcode_raw(code)
	pos, dir = 0, -1j
	drawn = set()
	try:
		while True:
			[_] = coro.send(None)
			[_, color] = coro.send(pos in grid)
			[_, rot] = coro.send(None)
			if color: grid |= {pos}
			else: grid -= {pos}
			drawn.add(pos)
			dir *= [-1j, 1j][rot]
			pos += dir
	except StopIteration: pass
	return grid, drawn

import sys
import numpy as np
code = [int(i) for i in sys.stdin.read().split(",")]

print(len(intcode_turtle(code)[1]))

np.set_printoptions(linewidth=3000)
pix = np.array(list(intcode_turtle(code, {0})[0]))
x = (pix.real - pix.real.min()).astype(int)
y = (pix.imag - pix.imag.min()).astype(int)
img = np.zeros((y.max()+1, x.max()+1))
img[y, x] = 1
print(str(img).replace("0", "."))
