inp = {}
for l in open("21.in"):
	k, v = l.split(": ", 1)
	match v.split():
		case [a]:
			inp[k] = int(a)
		case [a, o, b]:
			inp[k] = (a, o, b)

def e(n):
	match inp[n]:
		case (a, '+', b): return e(a) + e(b)
		case (a, '-', b): return e(a) - e(b)
		case (a, '*', b): return e(a) * e(b)
		case (a, '/', b): return e(a) / e(b)
		case v: return v

print(e("root"))

inp["humn"] = 1j
a = e(inp["root"][0])
b = e(inp["root"][2])
print((b - a.real) / a.imag) # due to floating-point it does not print exactly the right value
