import ast

inp = [ast.literal_eval(a) for a in open("18.in")]

def add_l(xs, y):
	if y == 0: return xs
	match xs:
		case int(x): return x + y
		case [l, r]: return [add_l(l, y), r]

def add_r(xs, y):
	if y == 0: return xs
	match xs:
		case int(x): return x + y
		case [l, r]: return [l, add_r(r, y)]

def reduce(xs):
	def explode(xs, d, ok):
		match xs:
			case [a, b] if d >= 4:
				return ok(a, 0, b)
			case [a, b]:
				if a_ := explode(a, d+1, lambda l, a, r: ok(l, [a, add_l(b, r)], 0)): return a_
				if b_ := explode(b, d+1, lambda l, b, r: ok(0, [add_r(a, l), b], r)): return b_

	def split(xs):
		match xs:
			case int(x) if x >= 10:
				return [x//2, -(-x//2)]
			case [a, b]:
				if a_ := split(a): return [a_, b]
				if b_ := split(b): return [a, b_]

	while True:
		ys = explode(xs, 0, lambda l, m, r: m) or split(xs)
		if ys is None: break
		xs = ys
	return xs

def mag(xs):
	match xs:
		case int(x): return x
		case [a, b]: return 3*mag(a) + 2*mag(b)

xs = reduce(inp[0])
for ys in inp[1:]:
	xs = reduce([xs, ys])
print(mag(xs))

print(max(
	mag(reduce([xs, ys]))
	for xs in inp
	for ys in inp
	if xs != ys
))
