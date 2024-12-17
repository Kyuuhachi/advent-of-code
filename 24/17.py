s=open("17.in").read().split()
a,b,c=map(int,s[2::3])
*C,=map(int,s[-1].split(','))
i=0
o=[]
while i<len(C):
 v=C[i+1];V=[0,1,2,3,a,b,c,0][v];i+=2
 match C[i-2]:
  case 0:a=a>>V
  case 1:b^=v
  case 2:b=V%8
  case 3 if a:i=v
  case 4:b^=c
  case 5:o+=[V%8]
  case 6:b=a>>V
  case 7:c=a>>V
print(','.join(map(str,o)))
