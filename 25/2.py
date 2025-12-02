S={n:=0}
for L in open(0).read()[:-1].split(','):
 A,B=map(int,L.split('-'))
 for i in range(2,10):
  for j in range(B):
   j=int(str(j)*i)
   j*=j>=A
   if j>B:break
   n+=j*(i==2)
   S|={j}
print(n,sum(S))
