import sys
inp = [int(i) for i in sys.stdin.read().split(",")]
i = 0
inputs = [5]

def p(n):
	mode = inp[i] // 10**(1+n) % 10
	if mode == 0: return inp[inp[i+n]]
	if mode == 1: return inp[i+n]

while True:
	if inp[i] == 99: break
	elif inp[i] % 100 == 1: inp[inp[i+3]] = p(1) + p(2); i += 4
	elif inp[i] % 100 == 2: inp[inp[i+3]] = p(1) * p(2); i += 4
	elif inp[i] % 100 == 3: inp[inp[i+1]] = inputs.pop(); i += 2
	elif inp[i] % 100 == 4: print(p(1)); i += 2
	elif inp[i] % 100 == 5:
		if p(1): i = p(2)
		else: i += 3
	elif inp[i] % 100 == 6:
		if not p(1): i = p(2)
		else: i += 3
	elif inp[i] % 100 == 7: inp[inp[i+3]] = p(1) < p(2); i += 4
	elif inp[i] % 100 == 8: inp[inp[i+3]] = p(1) == p(2); i += 4
