V=1<<24
def H(x):x^=(x<<6)%V;x^=x>>5;return(x^x<<11)%V
G={}
n=0
for i in open("22.in"):
 i=int(i[:-1]);j=p=i%10;w=[]
 for _ in range(2000):i=H(i);w+=(j:=j*18%18**4-p+(p:=i%10),p),
 n+=i
 for k,v in dict(w[3:][::-1]).items():G[k]=G.get(k,0)+v
print(n,max(G.values()))
