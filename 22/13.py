import json
import functools

inp = []
for chunk in open("13.in").read().split("\n\n"):
	a, b = chunk.strip().split("\n")
	inp.append((json.loads(a), json.loads(b)))

def cmp(a, b):
	match a, b:
		case (int(a), int(b)):
			return (a>b)-(a<b)
		case (list(a), list(b)):
			for ai, bi in zip(a, b):
				if c := cmp(ai, bi): return c
			return cmp(len(a), len(b))
		case (int(a), list(b)):
			return cmp([a], b)
		case (list(a), int(b)):
			return cmp(a, [b])
		case a: raise ValueError(a)

print(sum(i+1 for i, (a, b) in enumerate(inp) if cmp(a, b) < 0))
sort = sorted([a for a in inp for a in a] + [[[2]], [[6]]], key=functools.cmp_to_key(cmp))
print((sort.index([[2]])+1)*(sort.index([[6]])+1))
