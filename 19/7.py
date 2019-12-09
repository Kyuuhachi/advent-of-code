import sys
code = [int(i) for i in sys.stdin.read().split(",")]
import itertools

def intcode(code, inp):
	outp = []
	coro = intcode_raw(code, inp.pop, outp.append)
	try:
		v = coro.send(None)
		while True:
			if v[0] == "input": v = coro.send(inp.pop(0))
			elif v[0] == "output": v = coro.send(outp.append(v[1]))
			else: raise ValueError(v)
	except StopIteration: pass
	return outp

def intcode_raw(code):
	def g(n):
		mode = code[i] // 10**(1+n) % 10
		if mode == 0: return code[code[i+n]]
		if mode == 1: return code[i+n]
	def s(n, v):
		code[code[i+n]] = v

	i = 0
	while True:
		if code[i] == 99: break
		elif code[i] % 100 == 1: s(3, g(1)+g(2)); i += 4
		elif code[i] % 100 == 2: s(3, g(1)*g(2)); i += 4
		elif code[i] % 100 == 3: s(1, (yield ("input",))); i += 2
		elif code[i] % 100 == 4: yield ("output", g(1)); i += 2
		elif code[i] % 100 == 5: i = g(2) if g(1) else i+3
		elif code[i] % 100 == 6: i = i+3  if g(1) else g(2)
		elif code[i] % 100 == 7: s(3, g(1)<g(2)); i += 4
		elif code[i] % 100 == 8: s(3, g(1)==g(2)); i += 4
		else: raise ValueError(code[i])

# for s in itertools.permutations([0,1,2,3,4]):
# 	i = 0
# 	for b in s:
# 		[i] = intcode(list(code), [b, i])
# 	print(i, s)

for s in itertools.permutations([5,6,7,8,9]):
	i = [intcode_raw(list(code)) for _ in range(5)]

	for a, b in zip(i, s):
		[_] = a.send(None)
		[_] = a.send(b)

	v = 0
	for a in itertools.cycle(i):
		try: [_, v] = a.send(v)
		except StopIteration: break

		try: [_] = a.send(None)
		except StopIteration: pass
	print(v)
