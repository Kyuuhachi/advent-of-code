def p(n,*x,c=0):
	for y in x:
		if 0<y-n<4:n=y
		else:c+=1
	return c
a=b=0
for l in open("02.in"):w=list(map(int,l.split()));k=min(p(*w),p(*w[::-1]));a+=k<1;b+=k<2
print(a,b)
