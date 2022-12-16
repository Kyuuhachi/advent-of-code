import re
rx = re.compile(r"Valve (.+) has flow rate=(\d+); tunnels? leads? to valves? (.+)")

edges = {}
rate = {}
for line in open("16.in"):
	a, b, c = rx.fullmatch(line.strip()).groups()
	edges[a] = c.split(", ")
	rate[a] = int(b)

bits = {}
for a in rate:
	if rate[a]:
		bits[a] = 1<<len(bits)
bits["AA"] = 0

graph = {}
for k in edges:
	seen = set()
	dist = []
	q = [(k, 0)]
	for k2, v in q:
		for n in edges[k2]:
			if n not in seen:
				q.append((n, v+1))
				if rate[n] != 0:
					dist.append((n, v+2))
			seen.add(n)
	graph[k] = dist

def rec(k: str, t: int, s: int, seen: int):
	seen = seen | bits[k]
	s += rate[k]*t
	yield seen, s
	for k, v in graph[k]:
		if t > v and not (bits[k] & seen):
			yield from rec(k, t-v, s, seen)

print(max(s for _, s in rec("AA", 30, 0, 0)))

xs = {}
for seen, s in rec("AA", 26, 0, 0):
	xs[seen] = max(xs.get(seen, 0), s)
print(max(xs[a]+xs[b] for a in xs for b in xs if not (a&b)))
