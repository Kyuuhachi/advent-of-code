graph = {}
for line in open("25.in"):
	a, b = line.split(": ")
	graph[a] = b.split()


print("graph {")
for k, v in graph.items():
	print(f"{k} -- {{{','.join(v)}}}")
print("}")

cut = [
	("hvm", "grd"),
	("pmn", "kdc"),
	("jmn", "zfk"),
]

for a, b in cut:
	graph[a].remove(b)

for a, b in list(graph.items()):
	for b in b:
		graph.setdefault(b, []).append(a)

a = set()
q = [next(iter(graph))]
for v in q:
	if v not in a:
		q.extend(graph[v])
	a.add(v)
print(len(a) * (len(graph) - len(a)))
