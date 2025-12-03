Q=S,T=[{0},{0}]
for L in open(0).read().split(','):
 A,B=map(int,L.split('-'))
 for i in 2,3,5,7:Q[i%2]|={(j:=int(str(J)*i))*(A<=j<=B)for J in range(int(B**(1/i)))}
print(sum(S),sum(S|T))
