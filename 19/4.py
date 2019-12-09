import sys
mn, mx = [int(i) for i in sys.stdin.read().split("-")]
x = set()
for a in range(0, 10):
	for b in range(a, 10):
		for c in range(b, 10):
			for d in range(c, 10):
				for e in range(d, 10):
					s = "".join(map(str, [a,b,c,d,e]))
					for f in range(5):
						if (f == 0 or s[f-1] < s[f]) and (f == 4 or s[f] < s[f+1]):
							x.add(int(s[:f+1]+s[f:]))
print(len([a for a in x if mn <= a <= mx]))
