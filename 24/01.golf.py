a,b=[sorted(int(x.split()[i]) for x in open("01.in"))for i in(0,1)]
print(sum(abs(q-w)for q,w in zip(a,b)),sum(q*b.count(q)for q in a))
