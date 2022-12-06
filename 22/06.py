s = open("06.in").read().strip()

for i in range(4, len(s)):
	if len(set(s[i-4:i])) == 4:
		print(i)
		break

for i in range(14, len(s)):
	if len(set(s[i-14:i])) == 14:
		print(i)
		break
