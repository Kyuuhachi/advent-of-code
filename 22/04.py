inp = []
for line in open("04.in"):
	a, b = line.strip().split(",")
	inp.append((int(a.split("-")[0]), int(a.split("-")[1]), int(b.split("-")[0]), int(b.split("-")[1])))

n = 0
for a, b, c, d in inp:
	n += (a<=c<=d<=b) or (c<=a<=b<=d)
print(n)

n = 0
for a, b, c, d in inp:
	n += (a<=c<=b) or (a<=d<=b) or (c<=a<=d) or (c<=b<=d)
print(n)
