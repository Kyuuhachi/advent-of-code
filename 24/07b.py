F=lambda b,c:F(b+(e:=c[0]),d:=c[1:])|F(b*e,d)|O*F(int(f"{b}{e}"),d)if c else(b==a)*a
A=B=0
for l in open("07.in"):a,b,*c=map(int,l.replace(*': ').split());O=0;A+=F(b,c);O=1;B+=F(b,c)
print(A,B)
