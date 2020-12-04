import re
items = [
	dict(e.split(":") for e in item.split())
	for item in open("4.in").read().split("\n\n")
]

fields = {
	"byr": re.compile(r"19[2-8]\d|199\d|200[0-2]"),
	"iyr": re.compile(r"201\d|2020"),
	"eyr": re.compile(r"202\d|2030"),
	"hgt": re.compile(r"(1[5-8]\d|19[0-3])cm|(59|6\d|7[0-6])in"),
	"hcl": re.compile(r"#[0-9a-f]{6}"),
	"ecl": re.compile(r"amb|blu|brn|gry|grn|hzl|oth"),
	"pid": re.compile(r"[0-9]{9}"),
	# cid ignored
}

# Part 1
print(len([
	item
	for item in items
	if item.keys() - {"cid"} == fields.keys()
]))

# Part 2
print(len([
	item
	for item in items
	if all(
		k in item
		and fields[k].fullmatch(item[k])
		for k in fields
	)
]))
