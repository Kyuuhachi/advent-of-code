lines = []
for l in open("08.in"):
	a, b = l.split(" | ")
	lines.append((a.split(), b.split()))

print(sum(sum(len(w) in [2, 4, 3, 7] for w in b) for a, b in lines))

s = 0
for a, b in lines:
	a = list(a)
	def fd(n, f=lambda a: True):
		w = [a for a in a if len(a) == n and f(a)]
		assert len(w) == 1, w
		w = w[0]
		a.remove(w)
		return sorted(w)
	n1 = fd(2)
	n7 = fd(3)
	n4 = fd(4)
	n8 = fd(7)
	n3 = fd(5, lambda a: set(a) > set(n1))
	n9 = fd(6, lambda a: set(a) > set(n3))
	n0 = fd(6, lambda a: set(a) | set(n1) < set(n8))
	n6 = fd(6)
	n5 = fd(5, lambda a: set(a) < set(n6))
	n2 = fd(5)
	d = [n0, n1, n2, n3, n4, n5, n6, n7, n8, n9]
	s += int("".join(str(d.index(sorted(b))) for b in b))
print(s)
