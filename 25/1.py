v=50
n=m=0
for L in open(0):
	s=L<'R'
	V=v-s
	v+=int('-'*s+L[1:])
	n+=v%100<1
	m+=abs((v-s)//100-V//100)
print(n,m)
