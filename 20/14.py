import re
lines = []
for line in open("14.in").read().splitlines():
	if m := re.fullmatch(r"mask = ([10X]+)", line):
		mask = (
			int(m.group(1).translate(str.maketrans("10X", "110")), 2),
			int(m.group(1).translate(str.maketrans("10X", "100")), 2),
		)
	elif m := re.fullmatch(r"mem\[(\d+)\] = (\d+)", line):
		lines.append((mask, int(m.group(1)), int(m.group(2))))

# Part 1
mem = {}
for (m0, m1), k, v in lines:
	mem[k] = v & ~m0 | m1
print(sum(mem.values()))

# Part 2
from itertools import chain, combinations
def powerset(iterable):
	s = list(iterable)
	return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

mem = {}
for (m0, m1), k, v in lines:
	for i, j in enumerate(powerset(1<<x for x in range(36) if 1<<x & ~m0)):
		mem[k & m0 | m1 + sum(j)] = v
print(sum(mem.values()))
