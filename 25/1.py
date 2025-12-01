v,w,u=50,0,0
for l in open(0):
	t=l[0]<'R'
	k=v
	v+=int(l[1:-1])*(1-2*t)
	w+=v%100<1
	for i in range(min(k,v)+t, max(k,v)+t):
		u+=i%100<1
print(w,u)
