n = 0
for l in open("25.in").read().splitlines():
	w = 0
	for k in l:
		w = w * 5 + "=-012".find(k)-2
	n += w

s = ""
while n:
	n, q = divmod(n+2, 5)
	s = "=-012"[q] + s
print(s)
