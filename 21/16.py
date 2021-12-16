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
	match t:
		case Literal(ver=ver):       return ver
		case Op(ver=ver, args=args): return ver + sum(eval_a(c) for c in args)

def eval_b(t: Tree) -> int:
	match t:
		case Op(typ=0, args=args): return sum(eval_b(c) for c in args)
		case Op(typ=1, args=args): return prod(eval_b(c) for c in args)
		case Op(typ=2, args=args): return min(eval_b(c) for c in args)
		case Op(typ=3, args=args): return max(eval_b(c) for c in args)
		case Literal(val=val):     return val
		case Op(typ=5, args=[a, b]): return eval_b(a) > eval_b(b)
		case Op(typ=6, args=[a, b]): return eval_b(a) < eval_b(b)
		case Op(typ=7, args=[a, b]): return eval_b(a) == eval_b(b)

t = parse(b.ConstBitStream(i))
print(eval_a(t))
print(eval_b(t))
