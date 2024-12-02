def p(n,*x,c=0):
 for y in x:k=0<y-n<4;c+=1-k;n=[n,y][k]
 return c
a=b=0
for l in open("02.in"):*w,=map(int,l.split());k=min(p(*w),p(*w[::-1]));a+=k<1;b+=k<2
print(a,b)
