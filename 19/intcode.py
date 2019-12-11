def intcode(code, inp, mutate=False):
	if not mutate:
		code = list(code)
		inp = list(inp)
	outp = []
	coro = intcode_raw(code)
	try:
		v = coro.send(None)
		while True:
			if v[0] == "input": v = coro.send(inp.pop(0))
			elif v[0] == "output": v = coro.send(outp.append(v[1]))
			else: raise ValueError(v)
	except StopIteration: pass
	return outp

def intcode_raw(code):
	def addr(n):
		mode = code[i] // 10**(1+n) % 10
		p = i+n
		while p >= len(code): code.append(0)

		if mode != 1:
			p = code[p] + off*(mode==2)
			while p >= len(code): code.append(0)
		return p

	def g(n): return code[addr(n)]
	def s(n, v): code[addr(n)] = v

	i = 0
	off = 0
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
		elif code[i] % 100 == 9: off += g(1); i += 2
		else: raise ValueError(code[i])

