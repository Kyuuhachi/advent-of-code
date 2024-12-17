a,C=open("17.in").read().split()[2::8]
a,*C=map(int,[a,*C[::2]])
R=range(8)
N,M=[C[2*i+1]for i in R if C[2*i]==1]
D=lambda a:(b:=a&7^N)^(a>>b)&7^M
o=[]
while a:o+=[D(a)];a>>=3
print(*o,sep=',')
F=lambda A,c:sum((F(a,c[:-1])for b in R if D(a:=A*8|b)==c[-1]),[])if c else[A]
print(F(0,C)[0])
