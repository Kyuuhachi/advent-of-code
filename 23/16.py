import numpy as np

input = np.array([list(i) for i in open("16.in").read().splitlines()])

def run(y, x, rot):
	p = [(y, x, rot)]
	g = np.zeros_like(input, dtype="u1")
	seen = set()
	for (y, x, rot) in p:
		if not (0 <= y < input.shape[0]) or not (0 <= x < input.shape[1]):
			continue
		if (y, x, rot) in seen:
			continue
		seen.add((y, x, rot))
		g[y,x] += 1

		def up(): p.append((y-1, x, '↑'))
		def down(): p.append((y+1, x, '↓'))
		def left(): p.append((y, x-1, '←'))
		def right(): p.append((y, x+1, '→'))

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
	return (g != 0).sum()
print(run(0, 0, '→'))

h, w = input.shape
print(max(run(y, 0, '→') for y in range(h)))
print(max(run(y, w-1, '←') for y in range(h)))
print(max(run(0, x, '↓') for x in range(w)))
print(max(run(h-1, x, '↑') for x in range(w)))
