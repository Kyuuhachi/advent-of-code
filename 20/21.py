import re
from collections import defaultdict, deque

lines = []
for l in open("21.in").read().splitlines():
	ing, allerg = re.fullmatch(r"(.+) \(contains (.+)\)", l).groups()
	lines.append((set(ing.split(" ")), allerg.split(", ")))

has = defaultdict(list)
for ing, allerg in lines:
	for a in allerg:
		has[a].append(ing)

queue = deque((k, set.intersection(*vs)) for k, vs in has.items())
allergens = {}
while queue:
	k, v = queue.popleft()
	v -= allergens.keys()
	if len(v) != 1:
		queue.append((k, v))
		continue
	allergens[v.pop()] = k
assert len(allergens) == len(has)

# Part 1
print(sum(len(x - allergens.keys()) for x, _ in lines))

# Part 2
print(",".join(sorted(allergens, key=allergens.get)))
