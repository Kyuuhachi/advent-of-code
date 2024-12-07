F=lambda b,c:(lambda c,*d:F(b+c,d)or F(b*c,d)or O*F(int(f"{b}{c}"),d))(*c)if c else b==a
A=B=0
for l in open("07.in"):a,b,*c=map(int,l.replace(*': ').split());O=0;A+=a*F(b,c);O=1;B+=a*F(b,c)
print(A,B)
