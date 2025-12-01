v=50
n=m=0
for L in open(0):
	for i in range(int(L[1:])):
		v+=(-1)**(L<'R')
		m+=v%100<1
	n+=v%100<1
print(n,m)
