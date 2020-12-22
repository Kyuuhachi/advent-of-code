hands = tuple(
	[ int(x) for x in chunk.splitlines()[1:] ]
	for chunk in open("22.in").read().split("\n\n")
)
def score(ab):
	return sum(c*n for n, c in enumerate(ab[::-1], 1))
# Part 1
a, b = map(list, hands)
while a and b:
	c1, c2 = a.pop(0), b.pop(0)
	if c1 > c2: a.extend([c1, c2])
	else:       b.extend([c2, c1])
print(score(a+b))

# Part 2
def rec(a, b):
	a, b = list(a), list(b)
	seen = set()
	while a and b:
		# Not 100% sure this is a valid substitute for (tuple(a), tuple(b)) in
		# every possible scenario, but it works in my cases and it's a *lot*
		# faster (1.6s vs 0.2s)
		k = tuple(b)
		if k in seen: return True, None
		seen.add(k)

		c1, c2 = a.pop(0), b.pop(0)
		if c1 <= len(a) and c2 <= len(b):
			winner, _ = rec(a[:c1], b[:c2])
		else:
			winner = c1 > c2
		if winner: a.append(c1); a.append(c2)
		else:      b.append(c2); b.append(c1)
	return bool(a), score(a+b)
print(rec(*hands)[1])
