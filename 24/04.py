s=open("04.in").read()
w=s.find("\n")+1
c=lambda j:s[i::j][:4]=="XMAS"
d=lambda j:s[i-j::j][:3]=="MAS"
q=lambda f,j:f(j)+f(-j)
n=m=0
for i in range(len(s)):
 n+=q(c,1)+q(c,w)+q(c,w+1)+q(c,w-1)
 m+=q(d,w+1)and q(d,w-1)
print(n,m)
