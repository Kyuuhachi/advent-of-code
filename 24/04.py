s=open("04.in").read()
q=lambda f,j:f(j)+f(-j)
n=m=0
for i in range(len(s)):
 n+=q(c:=lambda j:s[i::j][:4]=="XMAS",1)+q(c,w:=s.find("\n")+1)+q(c,~w)+q(c,w-1)
 m+=q(d:=lambda j:s[i-j::j][:3]=="MAS",~w)and q(d,w-1)
print(n,m)
