code = [a.split() for a in open("24.in")]

def run(code, inp):
	inp = list(inp)
	var = {"x": 0, "y": 0, "z": 0, "w": 0}
	def v(x): return var[x] if x in var else int(x)
	for a in code:
		match a:
			case ["inp", o]:    var[o] = inp.pop(0)
			case ["add", o, i]: var[o] += v(i)
			case ["mul", o, i]: var[o] *= v(i)
			case ["div", o, i]: var[o] //= v(i)
			case ["mod", o, i]: var[o] %= v(i)
			case ["eql", o, i]: var[o] = var[o] == v(i)
			case a: raise ValueError(a)
	assert not inp
	return var

data = []
inp0 = code
while True:
	match inp0:
		case [
			["inp", "w"], # w = ?
			["mul", "x", "0"],
			["add", "x", "z"],
			["mod", "x", "26"], # x = z % 26
			["div", "z",  a ], # z /= a ? 26 : 1
			["add", "x",  b ],
			["eql", "x", "w"],
			["eql", "x", "0"], # x = x+b != w
			["mul", "y", "0"],
			["add", "y", "25"],
			["mul", "y", "x"],
			["add", "y", "1"],
			["mul", "z", "y"], # z *= x ? 26 : 1
			["mul", "y", "0"],
			["add", "y", "w"],
			["add", "y",  c ],
			["mul", "y", "x"],
			["add", "z", "y"], # z += x ? w+c : 0
			*inp0,
		]:
			a,b,c = int(a), int(b), int(c)
			assert a == (26 if b <= 0 else 1)
			assert not (0 < b < 10)
			assert c > 0
			# a is directly dependent on b, so we don't need it
			data.append((b, c))
		case []:
			break
		case _:
			raise ValueError(inp0)

"""
x = z % 26
if b <= 0:
	z = z/26
if x != w-b:
	z = z*26 + (w+c)
"""

# if b > 0 then b >= 10, so x+b != w, so we must push.
# Since w+c >= 2 is nonzero, we need to pop for every push, so the b<0 cases must not push

def aaa(f):
	stack = []
	ws = []
	for b, c in data:
		if b > 0:
			stack.append((len(ws), c))
			ws.append(None)
		else:
			p, c = stack.pop()
			x = f(b,-c)
			ws[p] = x-c
			ws.append(x+b)

	assert run(code, ws)["z"] == 0
	print("".join(map(str, ws)))

aaa(lambda a, b: 9-max(a,b))
aaa(lambda a, b: 1-min(a,b))
