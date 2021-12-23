import typing as T
from functools import cache
inp = open("23.in").read()

State = tuple[int|tuple[int,int],...]

def free(p: State, i: int, j: int) -> bool:
	for a in range(min(i, j)+1, max(i, j)):
		if isinstance(p[a], int) and p[a] != -1: return False
	return True

def moveto(r: tuple[int,...], e: int) -> T.Optional[int]:
	for i, v in enumerate(r):
		if v != -1: return None
		if r[i+1:] == (e,) * (len(r)-i-1): return i
	return None

def movefrom(r: tuple[int,...], e: int) -> T.Optional[int]:
	for i, v in enumerate(r):
		if r[i:] == (e,) * (len(r)-i): return None
		if v != -1: return i
	return None

def show(state: State) -> str:
	s = "ABCD_"
	x = []
	for a in state:
		if isinstance(a, int):
			x.append(s[a])
		else:
			x.append("[")
			for b in a:
				x.append(s[b])
			x.append("]")
	return "[%s]" % "".join(x)

target = [2,4,6,8]
expect = [-1,-1,0,-1,1,-1,2,-1,3,-1,-1]

def swap(state: State, ci: int, ri: int, k: int) -> (int, State):
	A = T.TypeVar("A")
	def u(a: tuple[A,...], i: int, v: A) -> tuple[A,...]:
		return a[:i] + (v,) + a[i+1:]

	assert free(state, ci, ri)
	c = state[ci]
	r = state[ri][k]
	assert c == -1 or r == -1
	state = u(state, ci, r)
	state = u(state, ri, u(state[ri], k, c))
	moves = abs(ci-ri)+(k+1)
	return (moves*10**max(c,r), state)

@cache
def home(state: State) -> (int, State):
	score = 0
	while True:
		for ci, c in enumerate(state):
			if isinstance(c, int) and c != -1:
				ri = target[c]
				if free(state, ci, ri) and (k := moveto(state[ri], expect[ri])) is not None:
					sc, state = swap(state, ci, ri, k)
					score += sc
					break
		else:
			break
	return score, state

def finished(state: State) -> bool:
	for e, ri in enumerate(target):
		for r in state[ri]:
			if r != e: return False
	return True

@cache
def run(state: State) -> T.Optional[int]:
	if finished(state):
		return 0

	sc = []
	for ri, r in enumerate(state):
		if isinstance(r, tuple) and (k := movefrom(state[ri], expect[ri])) is not None:
			for ci, c in enumerate(state):
				if c == -1 and free(state, ri, ci):
					s1, state2 = swap(state, ci, ri, k)
					s2, state3 = home(state2)
					s3 = run(state3)
					if s3 is not None:
						sc.append(s1+s2+s3)
	return min(sc, default=None)

print(run((
	-1,
	-1,
	("ABCD".index(inp[31]), "ABCD".index(inp[45])),
	-1,
	("ABCD".index(inp[33]), "ABCD".index(inp[47])),
	-1,
	("ABCD".index(inp[35]), "ABCD".index(inp[49])),
	-1,
	("ABCD".index(inp[37]), "ABCD".index(inp[51])),
	-1,
	-1,
)))

print(run((
	-1,
	-1,
	("ABCD".index(inp[31]), 3, 3, "ABCD".index(inp[45])),
	-1,
	("ABCD".index(inp[33]), 2, 1, "ABCD".index(inp[47])),
	-1,
	("ABCD".index(inp[35]), 1, 0, "ABCD".index(inp[49])),
	-1,
	("ABCD".index(inp[37]), 0, 2, "ABCD".index(inp[51])),
	-1,
	-1,
)))
