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

def test(what, x,m,a,s):
	if what == "A": return True
	if what == "R": return False

	p, end = scheme[what]
	for var, op, n, then in p:
		match var:
			case "x" if cond(x, op, n): return test(then, x, m, a, s)
			case "m" if cond(m, op, n): return test(then, x, m, a, s)
			case "a" if cond(a, op, n): return test(then, x, m, a, s)
			case "s" if cond(s, op, n): return test(then, x, m, a, s)
	return test(end, x, m, a, s)

n = 0
for line in b.splitlines():
	v = {}
	exec(line.strip()[1:-1].replace(",", ";"), v, v)
	if test("in", v["x"], v["m"], v["a"], v["s"]):
		n += v["x"] + v["m"] + v["a"] + v["s"]
print(n)

def split(r, o, n):
	if o == "<": return (r[0], n-1), (n, r[1])
	if o == ">": return (n+1, r[1]), (r[0], n)
	raise

def parse(what, x,m,a,s):
	if what == "A": return (x[1]-x[0]+1) * (m[1]-m[0]+1) * (a[1]-a[0]+1) * (s[1]-s[0]+1)
	if what == "R": return 0

	k = 0
	p, end = scheme[what]
	for var, op, n, then in p:
		match var:
			case "x": q,x = split(x, op, n); k += parse(then, q, m, a, s)
			case "m": q,m = split(m, op, n); k += parse(then, x, q, a, s)
			case "a": q,a = split(a, op, n); k += parse(then, x, m, q, s)
			case "s": q,s = split(s, op, n); k += parse(then, x, m, a, q)
	return k + parse(end, x, m, a, s)
print(parse("in", (1,4000), (1,4000), (1, 4000), (1,4000)))
