input = []
for i in open("12.in"):
	a, b = i.split()
	input.append((a, [int(b) for b in b.split(",")]))

def count(a: str, b: list[int]):
	import functools
	@functools.lru_cache(None)
	def rec(ai: int, bi: int):
		if ai >= len(a): return bi == len(b)
		if bi == len(b): return '#' not in a[ai:]
		n = 0
		if a[ai] in "#?":
			w = ai+b[bi]
			if '.' not in a[ai:w]:
				if len(a) >= w and not a[w:].startswith('#'):
					n += rec(w+1, bi+1)
		if a[ai] in ".?":
			n += rec(ai+1, bi)
		return n
	return rec(0, 0)

print(sum(count(a, b) for a, b in input))
print(sum(count(f"{a}?{a}?{a}?{a}?{a}", b * 5) for a, b in input))
