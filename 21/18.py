import ast

def parse(x):
	for c in x:
		yield int(c) if '0' <= c <= '9' else c

inp = [list(parse(a.strip())) for a in open("18.in")]

def reduce(xs):
	while True:
		l = 0
		for i in range(len(xs)):
			match xs[i:]:
				case ["[", int(a), ",", int(b), "]", *_] if l >= 4:
					xs[i:i+5] = [0]
					for j in range(i-1,-1,-1):
						if isinstance(xs[j], int):
							xs[j] += a
							break
					for j in range(i+1,len(xs)):
						if isinstance(xs[j], int):
							xs[j] += b
							break
					break
				case ["[", *_]:
					l += 1
				case ["]", *_]:
					l -= 1
		else:
			for i in range(len(xs)):
				match xs[i:]:
					case [int(v), *_] if v >= 10:
						xs[i:i+1] = ["[", v//2, ",", -(-v//2), "]"]
						break
			else:
				break
	return xs

def mag(xs):
	def i(xs):
		match xs:
			case [a, b]: return 3*i(a) + 2*i(b)
			case int(v): return v
	return i(ast.literal_eval("".join(map(str,xs))))

xs = reduce(inp[0])
for ys in inp[1:]:
	xs = reduce(["[", *xs, ",", *ys, "]"])
	print("".join(map(str,xs)))
print(mag(xs))

m = 0
for xs in inp:
	for ys in inp:
		if xs != ys:
			zs = reduce(["[", *xs, ",", *ys, "]"])
			if mag(zs) > m:
				m = mag(zs)
print(m)
