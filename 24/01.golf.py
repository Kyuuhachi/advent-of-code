a,b=[sorted(int(x.split()[i])for x in open("01.in"))for i in(0,1)]
print(sum(abs(q-w)+1j*q*b.count(q)for q,w in zip(a,b)))
