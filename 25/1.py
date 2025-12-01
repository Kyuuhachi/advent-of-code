v,w,u=50,0,0
for l in open(0):
	t=l[0]<'R'
	k=v-t
	v+=int(l[1:-1])*(1-2*t)
	w+=v%100<1
	u+=abs((v-t)//100-k//100)
print(w,u)
