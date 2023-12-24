import numpy as np
input = np.array([list(i) for i in open("23.in").read().splitlines()])

slope = np.isin(input, list(">v"))
hor = np.roll(slope, 1, axis=0) & np.roll(slope, -1, axis=0)
ver = np.roll(slope, 1, axis=1) & np.roll(slope, -1, axis=1)
nodes = set(zip(*np.where(hor | ver)))
end = input[:-2,:-2].shape
nodes.add((1,1))
nodes.add(end)

seen = input == '#'
seen[0,1] = True
seen[~0,~1] = True
graph = {}
w = [(1,1,(1,1),0)]
for y,x,start,n in w:
	if (y,x) in nodes and (y,x) != start:
		graph.setdefault(start, {})[(y,x)] = n
	if seen[y,x]:
		continue
	seen[y,x] = True
	if (y,x) in nodes:
		w.append((y+1,x,(y,x),1))
		w.append((y,x+1,(y,x),1))
	else:
		w.append((y-1,x,start,n+1))
		w.append((y,x-1,start,n+1))
		w.append((y+1,x,start,n+1))
		w.append((y,x+1,start,n+1))

# print("digraph {")
# for k, v in graph.items():
# 	for v, d in v.items():
# 		print(f"{str(k)!r} -> {str(v)!r} [label={d}]")
# print("}")

def p1(start):
	if start == end:
		return 0
	return max(v+p1(k) for k, v in graph[start].items())
print(2+p1((1,1)))

for k, n in list(graph.items()):
	for v, d in n.items():
		graph.setdefault(v, {})[k] = d

def p2(start, seen):
	if start in seen:
		return float("-inf")
	seen = seen | {start}
	if start == end:
		return 0
	return max(v+p2(k, seen) for k, v in graph[start].items())
print(2+p2((1,1), set()))
