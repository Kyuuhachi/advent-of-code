for z in 0,1:
 S=n=i=0;R,H=[],[]
 for w,v in zip(a:=map(int,open("09.in").read().strip()+'0'),a):R+=[[n,w,i]]if z else[[n+m,1,i]for m in range(w)];H+=[[n+w,v]];n+=v+w;i+=1
 for n,w,i in R[::-1]:
  for h in H:
   if h[0]>=n:break
   if h[1]>=w:n=h[0];h[0]+=w;h[1]-=w;h[1]or H.remove(h)
  S+=i*w*(2*n+w-1)//2
 print(S)
