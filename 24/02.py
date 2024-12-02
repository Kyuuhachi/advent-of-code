w=lambda*a:all(0<a-b<4for a,b in zip(*a))
q=lambda x:w(x[1:],x)|w(x,x[1:])
print(sum(q(x:=list(map(int,r.split())))+1j*any(q(x[:y]+x[y+1:])for y in range(len(x)))for r in open("02.in")))
