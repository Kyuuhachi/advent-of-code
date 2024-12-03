import re
s=open("03.in").read()
A=B=0
w=1
for a,b,c,d in re.findall(r"mul\((\d+),(\d+)\)|(d)on't\(\)|(d)o\(\)",s):
 if c+d:w=len(d)
 if a:A+=int(a)*int(b);B+=int(a)*int(b)*w
print(A, B)
