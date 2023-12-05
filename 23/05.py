import math

inp = open("05.in").read().strip().split("\n\n");
goal = [int(a) for a in inp[0].removeprefix("seeds: ").split()]
maps = []
for inp in inp[1:]:
	inp = inp.splitlines()
	mapping = sorted(
		[tuple(map(int, line.split())) for line in inp[1:]],
		key=lambda a: a[1],
	)
	
	prev = 0
	mapping2 = []
	for (dst, src, count) in mapping:
		if prev < src:
			mapping2.append((src, 0))
		mapping2.append((src+count, dst-src))
		prev = src + count
	mapping2.append((math.inf, 0))
	maps.append(mapping2)

s = goal
for v in maps:
	s = [next(
		s + off
		for end, off in v
		if s < end
	) for s in s]
print(min(s))

s = sorted((a, a+b) for a, b in zip(goal[0::2], goal[1::2]))
for v in maps:
	s.append((math.inf, math.inf))
	s.reverse()

	prev = 0
	out = []
	for end, off in v:
		while s[-1][1] < prev:
			s.pop()
		if end <= s[-1][0]:
			continue
		while True:
			mn = max(prev, s[-1][0])
			mx = min(end, s[-1][1])
			if mn < mx:
				out.append((mn+off, mx+off))
			if s[-1][1] < end:
				s.pop()
			else:
				break
		prev = end
	out.sort()
	s = out
print(min(s)[0])
