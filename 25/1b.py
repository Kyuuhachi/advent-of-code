v=50
n=m=0
for L in open(0):
	for i in range(int(L[1:])):v+=1-2*(L<'R');k=v%100<1;m+=k
	n+=k
print(n,m)
