import re
import itertools as it
from math import lcm
input = open("08.in").read().splitlines()
directions = input[0]
graph = {}
for line in input[2:]:
	turn, l, r = re.match(r"(\w+) = \((\w+), (\w+)\)", line).groups()
	graph[turn] = (l, r)

n = 0
pos = "AAA"
for a in it.cycle(directions):
	pos = graph[pos][a == "R"]
	n += 1
	if pos == "ZZZ": break
print(n)

k = 1
for pos0 in graph:
	if not pos0.endswith("A"): continue
	pos = pos0

	seen = {}
	seen[len(directions)-1, pos] = 0
	for i, (turnp, turn) in enumerate(it.cycle(enumerate(directions)), 1):
		pos = graph[pos][turn == "R"]
		if (turnp, pos) in seen: break
		seen[turnp, pos] = i
	start = seen[turnp, pos]
	seen = [a for _, a in seen]

	## Validate that it does indeed loop
	# pos = pos0
	# for turn, expected in it.islice(zip(
	# 	it.cycle(directions),
	# 	it.chain(seen[:start], it.cycle(seen[start:]))
	# ), 1000000):
	# 	assert pos == expected
	# 	pos = graph[pos][turn == "R"]

	assert seen[-start].endswith("Z")
	k = lcm(k, len(seen) - start)
print(k)
