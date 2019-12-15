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

class intcode_raw:
	def __init__(self, code):
		self.code = list(code)
		self.i = 0
		self.off = 0
		self.mode = None

	def addr(self, n):
		mode = self.code[self.i] // 10**(1+n) % 10
		p = self.i+n
		while p >= len(self.code): self.code.append(0)

		if mode != 1:
			p = self.code[p] + self.off*(mode==2)
			while p >= len(self.code): self.code.append(0)
		return p

	def __getitem__(self, n): return self.code[self.addr(n)]
	def __setitem__(self, n, v): self.code[self.addr(n)] = v

	def send(self, v=None):
		if self.mode is None: pass
		elif self.mode == "input": self[1] = v; self.i += 2
		elif self.mode == "output": self.i += 2
		while True:
			op = self.code[self.i] % 100
			if   op == 99: raise StopIteration
			elif op == 1: self[3] = self[1]+self[2]; self.i += 4
			elif op == 2: self[3] = self[1]*self[2]; self.i += 4
			elif op == 3: self.mode = "input"; return ("input",)
			elif op == 4: self.mode = "output"; return ("output", self[1])
			elif op == 5: self.i = self[2] if self[1] else self.i+3
			elif op == 6: self.i = self.i+3  if self[1] else self[2]
			elif op == 7: self[3] = int(self[1]<self[2]); self.i += 4
			elif op == 8: self[3] = int(self[1]==self[2]); self.i += 4
			elif op == 9: self.off += self[1]; self.i += 2
			else: raise ValueError(self.code[self.i])

	def clone(self):
		c = type(self)(self.code)
		c.i, c.off, c.mode = self.i, self.off, self.mode
		return c
