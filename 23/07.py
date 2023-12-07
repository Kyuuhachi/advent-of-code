from collections import Counter
input = []
for line in open("07.in"):
	a, b = line.split()
	input.append((a, int(b)))

def score(cardvalue, hands):
	def score(cards):
		return (
			sorted(hands(cards).values(), reverse=True),
			[cardvalue.find(v) for v in cards],
		)
	return sum((i+1)*b for i, (_, b) in enumerate(sorted(input, key=lambda a: score(a[0]))))

print(score("23456789TJQKA", Counter))

def JokerCounter(cards):
	count = Counter(cards)
	if len(count) > 1:
		jokers = count.pop("J", 0)
		[(best, _), *_] = count.most_common()
		count[best] += jokers
	return count
print(score("J23456789TQKA", JokerCounter))
