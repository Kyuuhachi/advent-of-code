import numpy as np
import sys

input = np.array([list(i) for i in open("16.in").read().splitlines()])

PENDING = object()
cache = {}
sys.setrecursionlimit(2*input.shape[0]*input.shape[1])
def run(y, x, rot):
	if not (0 <= y < input.shape[0]) or not (0 <= x < input.shape[1]):
		return False

	w = np.zeros(input.shape, dtype=bool)

	if (cache.get((y,x,rot))) is None:
		cache[y,x,rot] = PENDING
	elif (cache.get((y,x,rot))) is PENDING:
		cache[y,x,rot] = w
	else:
		return cache[y,x,rot]

	w[y,x] = True
	def up(): nonlocal w; w |= run(y-1, x, '↑')
	def down(): nonlocal w; w |= run(y+1, x, '↓')
	def left(): nonlocal w; w |= run(y, x-1, '←')
	def right(): nonlocal w; w |= run(y, x+1, '→')

	match input[y,x], rot:
		case '|', ('→' | '←'): up(); down()
		case '-', ('↓' | '↑'): left(); right()
		case '/',  '←': down()
		case '/',  '↓': left()
		case '/',  '↑': right()
		case '/',  '→': up()
		case '\\', '←': up()
		case '\\', '↓': right()
		case '\\', '↑': left()
		case '\\', '→': down()
		case ('.' | '-'), '←': left()
		case ('.' | '-'), '→': right()
		case ('.' | '|'), '↑': up()
		case ('.' | '|'), '↓': down()
		case _: raise ValueError(y, x, rot)
	cache[y,x,rot] = w
	return w
print(run(0, 0, '→').sum())

h, w = input.shape
print(max([
	max(run(y, 0, '→').sum() for y in range(h)),
	max(run(y, w-1, '←').sum() for y in range(h)),
	max(run(0, x, '↓').sum() for x in range(w)),
	max(run(h-1, x, '↑').sum() for x in range(w)),
]))
