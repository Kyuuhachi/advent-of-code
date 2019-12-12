import sys
import numpy as np
pos0 = np.array([[int(b[2:]) for b in a[1:-1].split(", ")] for a in sys.stdin.read().splitlines()])

pos = np.array(pos0)
vel = np.zeros_like(pos)
for _ in range(1000):
	vel += np.sign(pos[:,None] - pos[None,:]).sum(axis=0)
	pos += vel
print(np.abs(pos).sum(axis=1) @ np.abs(vel).sum(axis=1))

x = []
for a in range(3):
	s = set()
	pos = np.array(pos0)[:,a]
	vel = np.zeros_like(pos)
	while True:
		vel += np.sign(pos[:,None] - pos[None,:]).sum(axis=0)
		pos += vel
		v = bytes(pos.data) + bytes(vel.data)
		if v in s: break
		s.add(v)
	x.append(len(s))
print(np.lcm.reduce(x))
