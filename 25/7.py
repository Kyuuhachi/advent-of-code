S,*I=[sum(1<<i for i,c in enumerate(L)if'.'<c)for L in open(0)]
print(f"{S:032b}")
n=0
for L in I:
 n+=(L&S).bit_count()
 S=(S&~L)|(S&L)<<1|(S&L)>>1
 print(f"{S:032b}", n)
