V=1<<24
G=[0]*18**4
n=0
for i in open("22.in"):
 i=int(i[:-1]);j=p=i%10;w=[]
 for _ in range(2000):i^=i*64%V;i^=i>>5;i^=i*2048%V;w+=(j:=j*18%18**4-p+(p:=i%10),p),
 n+=i
 for k,v in dict(w[:2:-1]).items():G[k]+=v
print(n,max(G))
