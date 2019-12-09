import sys
inp_ = [int(i) for i in sys.stdin.read().split(",")]
for noun in range(100):
	for verb in range(100):
		inp = list(inp_)
		i = 0
		inp[1], inp[2] = noun, verb
		while True:
			if inp[i] == 99: break
			elif inp[i] == 1: inp[inp[i+3]] = inp[inp[i+1]] + inp[inp[i+2]]; i += 4
			elif inp[i] == 2: inp[inp[i+3]] = inp[inp[i+1]] * inp[inp[i+2]]; i += 4
		print(noun, verb, inp)
