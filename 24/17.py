a,C=open("17.in").read().split()[2::8]
a,*C=map(int,[a,*C[::2]])
N,M=[C[i+1]for i in range(0,16,2)if C[i]==1]
D=lambda a:(b:=a&7^N)^(a>>b)&7^M
o=[]
while a:o+=[D(a)];a>>=3
print(*o,sep=',')
F=lambda A,c:sum((F(a, c[:-1])for b in range(8)if D(a:=A<<3|b)==c[-1]),[])if c else[A]
print(F(0,C)[0])
