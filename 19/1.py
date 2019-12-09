import sys
inp = [int(i) for i in sys.stdin.read().splitlines()]
s = 0
for i in inp:
	i2 = (i//3)-2
	if i2 <= 0: continue
	s += i2
	inp.append(i2)
print(s)
