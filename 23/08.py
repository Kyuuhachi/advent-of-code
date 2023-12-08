import re
from math import lcm
input = open("08.in").read().splitlines()
directions = input[0]
graph = {}
for line in input[2:]:
	turn, l, r = re.match(r"(\w+) = \((\w+), (\w+)\)", line).groups()
	graph[turn] = (l, r)

def run(pos):
	n = 0
	while not pos.endswith("Z"):
		pos = graph[pos][directions[n % len(directions)] == "R"]
		n += 1
	return n

print(run("AAA"))
print(lcm(*(run(pos) for pos in graph if pos.endswith("A"))))
