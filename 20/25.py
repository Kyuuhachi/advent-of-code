k1, k2 = map(int, open("25.in").read().splitlines())

# Part 1
# This is the Diffie-Hellman key exchange
def babystep_giantstep(g, h, mod):
	# From wikipedia
	import math
	m = math.ceil(math.sqrt(mod))
	table = {}
	e = 1
	for i in range(m):
		table[e] = i
		e = e * g % mod
	factor = pow(g, mod-m-1, mod)
	e = h
	for i in range(m):
		if e in table:
			return i*m + table[e]
		e = e * factor % mod


print(pow(k1, babystep_giantstep(7, k2, 20201227), 20201227))

# Part 2:
# uhh
