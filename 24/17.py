s=open("17.in").read().split()
a,b,c=map(int,s[2::3])
*C,=map(int,s[-1].split(','))

N,M=[C[i+1]for i in range(0,16,2)if C[i]==1]

def dec(a):
 b  = a & 7
 b ^= N
 b ^= (a >> b) & 7
 b ^= M
 return b

o=[]
while a:
 o+=[dec(a)]
 a >>= 3

print(','.join(map(str,o)))

F = lambda A, c: (
 k
 for b in range(8)
 if dec(a:=A<<3|b)==c[0]
 for k in F(a, c[1:])
) if c else [A]
print(next(F(0, C[::-1])))
