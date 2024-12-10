*s,=map(int,open("09.in").read().strip()+'0')
for z in 0,1:
 n=i=0
 R=[]
 H=[]
 for w,v in zip(a:=iter(s),a):R+=[[n,w,i]]if z else[[n+m,1,i]for m in range(w)];H+=[[n+w,v]];n+=v+w;i+=1
 S=0
 for a,k,i in R[::-1]:
  for h in H:
   if h[1]>=k:a=h[0];h[0]+=k;h[1]-=k;h[1]or H.remove(h)
   if h[0]>=a:break
  S+=i*k*(2*a+k-1)//2
 print(S)
