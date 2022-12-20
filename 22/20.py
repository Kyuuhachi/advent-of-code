inp = list(map(int, open("20.in")))
K = len(inp)

m = list(inp)
n = list(range(K))
for i in range(K):
	p = n.index(i)
	q = (p+m[p])%(K-1) # -1 because we pop an item
	m.insert(q, m.pop(p))
	n.insert(q, n.pop(p))

p = m.index(0)
print(m[(p+1000)%K] + m[(p+2000)%K] + m[(p+3000)%K])


m = [a*811589153 for a in inp]
n = list(range(K))
for _ in range(10):
	for i in range(K):
		p = n.index(i)
		q = (p+m[p])%(K-1)
		m.insert(q, m.pop(p))
		n.insert(q, n.pop(p))

p = m.index(0)
print(m[(p+1000)%K] + m[(p+2000)%K] + m[(p+3000)%K])
