inp = [(ord(a[0])-ord('A'), ord(a[2])-ord('X')) for a in open("02.in")]

print(
	sum((1+a[1] + 3*((a[1]-a[0]+1)%3)) for a in inp),
	sum((1+(a[1]+a[0]-1)%3 + 3*a[1]) for a in inp)
)
