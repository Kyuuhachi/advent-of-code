l1, l2 = open("13.in").read().splitlines()
start = int(l1)
ids = [(i, int(x)) for i, x in enumerate(l2.split(",")) if x != "x"]

# Part 1
a, b = min((-start % x, x) for _, x in ids)
print(a*b)

# Part 2
def eea(r, r_):
	s, s_ = 1, 0
	t, t_ = 0, 1
	while r != 0:
		q = r_ // r
		r, r_ = r_ - q * r, r
		s, s_ = s_ - q * s, s
		t, t_ = t_ - q * t, t
	sgn = r_ // abs(r_)
	return r_ * sgn, s_ * sgn, t_ * sgn

def crt(q1, q2):
	r1, n1 = q1
	r2, n2 = q2
	_, a1, a2 = eea(n1, n2)
	a = r2*a1*n1 + r1*a2*n2
	n = n1 * n2
	return a % n, n

from functools import reduce
print(reduce(crt, [(-i % x, x) for i, x in ids])[0])
