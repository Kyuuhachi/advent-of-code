B={}
for l in open("24.in"):
 match l.split():
  case [a,b,c,d,e]:B[b,a,c]=B[b,c,a]=e

m=[]
K='x00','y00'
c,p=B['XOR',*K],B['AND',*K]
assert c == 'z00', c
n=1
while 1:
 N="%02d"%n
 K='x'+N,'y'+N
 if('XOR',*K)not in B:break
 if p[0]=='z':c,p=p,c;m+=[c,p]
 a,b=B['XOR',*K],B['AND',*K]
 if('XOR',p,b)in B:a,b=b,a;m+=[a,b]
 c,d=B['XOR',p,a],B['AND',p,a]
 if b[0]=='z':c,b=b,c;m+=[c,b]
 if d[0]=='z':c,d=d,c;m+=[c,d]
 p=B['OR',d,b]
 n+=1
print(','.join(sorted(m)))
