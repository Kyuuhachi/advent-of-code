import lark
[a, b] = open("19.in").read().split("\n\n")
rules = {}
for r in a.splitlines():
	k, v = r.split(": ")
	if '"' in v:
		rules[int(k)] = v[1:-1]
	else:
		rules[int(k)] = tuple(tuple(int(w) for w in a.split(" ")) for a in v.split(" | "))
lines = b.splitlines()

import re
class a(dict):
	def __missing__(f, key):
		v = rules[key]
		if isinstance(v, str):
			return v
		else:
			return "(%s)" % "|".join("".join(f[a] for a in b) for b in v)
r = re.compile(a()[0])
print(sum(bool(r.fullmatch(s)) for s in lines))

w = a()
w[8] = f"({w[42]}+)"
w[11] = "(%s)" % ("(".join([w[42]]*8) + ")?".join([w[31]]*8))
r = re.compile(w[0])
print(sum(bool(r.fullmatch(s)) for s in lines))
