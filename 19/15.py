import intcode

def dirs(pos):
	(x, y) = pos
	return [(x-1,y), (x+1, y), (x, y-1), (x, y+1)]

def explore(ic, pos, world):
	for i, pos2 in enumerate(dirs(pos), 1):
		ic2 = ic.clone()
		[_, v] = ic2.send(i)
		[_] = ic2.send(None)
		if pos2 not in world:
			world[pos2] = v
			if v:
				explore(ic2, pos2, world)

import sys
code = [int(i) for i in sys.stdin.read().split(",")]
ic = intcode.intcode_raw(code)
ic.send(None)
world = {(0, 0): 3}
explore(ic, (0, 0), world)

[oxy] = [k for k, v in world.items() if v == 2]
flood = [(oxy, 0)]
for (pos, n) in flood:
	if world[pos] == 3:
		print(n)
	world[pos] = 0
	for pos2 in dirs(pos):
		if world[pos2] == 0: continue
		flood.append((pos2,n+1))
print(n)
