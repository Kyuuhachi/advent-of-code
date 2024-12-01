x=list(map(int,open("01.txt").read().split()));a=x[::2];b=x[1::2]
s=sorted;print(sum(abs(q-w)for q,w in zip(s(a),s(b))))
print(sum(q*(q==w)for q in a for w in b))
