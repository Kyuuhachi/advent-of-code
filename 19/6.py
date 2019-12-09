import sys
inp = [tuple(l.split(")")) for l in sys.stdin.read().splitlines()]

tree = {b: a for a, b in inp}

cache = {}
def read(node):
	if node not in cache:
		if node in tree:
			cache[node] = read(tree[node])+1
		else:
			cache[node] = 0
	return cache[node]

q1 = sum(read(a) for a in {x for l in inp for x in l})

def path(node):
	a = []
	while node in tree:
		a.append(node := tree[node])
	a.reverse()
	return a
p1 = path("YOU")
p2 = path("SAN")
while p1[0] == p2[0]:
	p1.pop(0)
	p2.pop(0)
print(len(p1)+len(p2))
