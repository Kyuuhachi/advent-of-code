n = [int(a) for a in open("06.in").read().split(",")]

w = [0] * 9
for i in n:
	w[i] += 1

for t in range(256):
	w[(t+7)%9] += w[t%9]

	if t == 79 or t == 255:
		print(sum(w))
