s=open("04.in").read()
q=lambda j:f(j)+f(-j)
n=m=0
for i in range(len(s)):
 f=lambda j:s[i::j][:4]=="XMAS";n+=q(1)+q(w:=s.find("\n")+1)+q(~w)+q(w-1)
 f=lambda j:s[i-j::j][:3]=="MAS";m+=q(~w)*q(w-1)
print(n,m)
