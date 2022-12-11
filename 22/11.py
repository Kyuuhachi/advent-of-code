import re
import dataclasses
import copy
from math import lcm
from types import CodeType
inp = open("11.in").read()

@dataclasses.dataclass(frozen=True)
class Monkey:
	id: int
	items: tuple[int, ...]
	op: CodeType
	modulo: int
	true: int
	false: int

rx = re.compile(r"""
Monkey (\d+):
  Starting items: ([0-9, ]+)
  Operation: new = ([^\n]+)
  Test: divisible by (\d+)
    If true: throw to monkey (\d+)
    If false: throw to monkey (\d+)
""".strip())

monkeys = []
for m in inp.split("\n\n"):
	id, items, op, modulo, true, false = rx.fullmatch(m.strip()).groups()
	monkeys.append(Monkey(
		int(id),
		tuple(int(a) for a in items.split(", ")),
		compile(op, "-", "eval"),
		int(modulo),
		int(true),
		int(false),
	))

@dataclasses.dataclass
class State:
	monkey: Monkey
	items: list[int]
	n: int

states = [State(m, list(m.items), 0) for m in monkeys]
for i in range(20):
	for s in states:
		m = s.monkey
		(items, s.items) = (s.items, [])
		for item in items:
			val = eval(m.op, { "old": item }) // 3
			states[m.true if val % m.modulo == 0 else m.false].items.append(val)
			s.n += 1
	# for i, s in enumerate(states):
	# 	print(i, s.items)
	# print()

[*_, m1, m2] = sorted(states, key=lambda m: m.n)
print(m1.n * m2.n)

states = [State(m, list(m.items), 0) for m in monkeys]
mod = 1
for m in monkeys:
	mod = lcm(mod, m.modulo)
for i in range(10000):
	for s in states:
		(items, s.items) = (s.items, [])
		m = s.monkey
		for item in items:
			val = eval(m.op, { "old": item }) % mod
			states[m.true if val % m.modulo == 0 else m.false].items.append(val)
			s.n += 1
	# if i+1 == 20 or (i+1) % 1000 == 0:
	# 	for i, s in enumerate(states):
	# 		print(i, s.items)
	# 	print()

[*_, m1, m2] = sorted(states, key=lambda m: m.n)
print(m1.n * m2.n)
