from collections import Counter
import sys

r = {}
def parse(s): a, b = s.split(); return b, int(a)
for a in sys.stdin.read().splitlines():
	f, t = a.split(" => ")
	f, t = [parse(b) for b in f.split(", ")], parse(t)
	assert t[0] not in r
	r[t[0]] = (t[1], Counter(dict(f)))

def produce(s, c, n):
	if s == "ORE": return
	n -= c[s]
	if n <= 0: return

	count, ingr = r[s]
	rounds = -(-n//count)
	for k, v in ingr.items():
		produce(k, c, rounds*v)
		c[k] -= rounds*v
	c[s] += count * rounds

def produceFuel(n):
	c = Counter()
	produce("FUEL", c, n)
	return -c["ORE"]

print(produceFuel(1))

def recurse(n): # I could reuse the computation from 2n and just add n more, but produce() is fast enough
	if produceFuel(n) > 1e12: return 0
	n2 = recurse(n*2)
	if produceFuel(n2 + n) > 1e12: return n2
	return n2 + n

print(recurse(1))
