v=50
w=u=0
for l in open(0):
	t=l<'R'
	k=v-t
	v+=int('-'*t+l[1:-1])
	w+=v%100<1
	u+=abs((v-t)//100-k//100)
print(w,u)
