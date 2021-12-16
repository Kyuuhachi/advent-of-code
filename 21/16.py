import typing as T
import bitstring as b
import dataclasses as D
from math import prod
i = b.Bits(hex=open("16.in").read())

Tree = T.Union["Literal", "Op"]

@D.dataclass
class Literal:
	ver: int
	val: int

@D.dataclass
class Op:
	ver: int
	typ: int
	args: list[Tree]

def parse(bs: b.ConstBitStream) -> Tree:
	def n(n: int) -> int:
		return bs.read(f"uint:{n}")
	ver = n(3)
	typ = n(3)

	if typ == 4:
		val = 0
		while True:
			more = n(1)
			val = val << 4 | n(4)
			if not more: break
		return Literal(ver, val)

	else:
		sub = []
		if n(1):
			for _ in range(n(11)):
				sub.append(parse(bs))
		else:
			e = n(15) + bs.pos
			while bs.pos < e:
				sub.append(parse(bs))
		return Op(ver, typ, sub)

def eval_a(t: Tree) -> int:
	if isinstance(t, Literal):
		return t.ver
	else:
		return t.ver + sum(eval_a(c) for c in t.args)

def eval_b(t: Tree) -> int:
	if isinstance(t, Literal):
		return t.val
	else:
		args = [eval_b(c) for c in t.args]
		if t.typ == 0: return sum(args)
		if t.typ == 1: return prod(args)
		if t.typ == 2: return min(args)
		if t.typ == 3: return max(args)
		if t.typ == 5: return args[0] > args[1]
		if t.typ == 6: return args[0] < args[1]
		if t.typ == 7: return args[0] == args[1]

t = parse(b.ConstBitStream(i))
print(eval_a(t))
print(eval_b(t))
