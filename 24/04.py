s=open("04.in").read()
w=s.find("\n")+1
c=lambda j:s[i::j][:4]=="XMAS"
d=lambda j:s[i-j::j][:3]=="MAS"
n=m=0
for i in range(len(s)):
 n+=c(1)+c(-1)+c(w)+c(-w)+c(w+1)+c(w-1)+c(-w+1)+c(-w-1)
 m+=d(w+1)+d(-w-1)and d(w-1)+d(-w+1)
print(n,m)
