import re
a, b = open("19.in").read().split("\n\n")

scheme = {}
for line in a.splitlines():
	name, body = re.match(r"(\w+)\{(.*)\}", line.strip()).groups()
	*p, end = body.split(",")
	then = []
	for p in p:
		p, q = p.split(":")
		then.append((p[0], p[1], int(p[2:]), q))
	scheme[name] = (then, end)

def cond(r, o, n):
	if o == "<": return r < n
	if o == ">": return r > n
	raise

def test(what, **vars):
	if what == "A": return True
	if what == "R": return False

	p, end = scheme[what]
	for var, op, n, then in p:
		if cond(vars[var], op, n): return test(then, **vars)
	return test(end, **vars)

n = 0
for line in b.splitlines():
	vars = {}
	exec(line.strip()[1:-1].replace(",", ";"), {}, vars)
	if test("in", **vars):
		n += sum(vars.values())
print(n)

def split(r, o, n):
	if o == "<": return (r[0], n-1), (n, r[1])
	if o == ">": return (n+1, r[1]), (r[0], n)
	raise

def parse(what, **vars):
	from math import prod
	if what == "A": return prod(a[1]-a[0]+1 for a in vars.values())
	if what == "R": return 0

	k = 0
	p, end = scheme[what]
	for var, op, n, then in p:
		v1, v2 = split(vars[var], op, n)
		vars[var] = v1
		k += parse(then, **vars)
		vars[var] = v2
	return k + parse(end, **vars)
print(parse("in", x=(1,4000), m=(1,4000), a=(1, 4000), s=(1,4000)))
