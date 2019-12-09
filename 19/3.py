import sys
l1, l2 = [s.split(",") for s in sys.stdin.read().splitlines()]
dirs = dict(zip("UDLR", [-1,1,-1j,1j]))
def walk(x):
	p = 0
	s = 0
	for insn in x:
		d, l = insn[0], int(insn[1:])
		for a in range(l):
			p += dirs[d]
			s += 1
			yield p, s
l1 = dict(reversed(list(walk(l1))))
l2 = dict(reversed(list(walk(l2))))
sect = {a: (l1[a], l2[a]) for a in l1.keys() & l2.keys()}
print(min(abs(a.real) + abs(a.imag) for a in sect.keys()))
print(min(a+b for a, b in sect.values()))
