from pprint import pprint
from re import compile, findall

file = open('Day 2.txt', 'r')
data = file.read()
file.close()

lines = data.split('\n')
counter = 0


for i in range(len(lines)):
	lines[i] = lines[i].split()

	charLen = lines[i][0].split('-')
	minChar = int(charLen[0])
	maxChar = int(charLen[1])

	letter = lines[i][1]

	pwd = lines[i][2]

	found = 0
	for j in pwd:
		if j == letter:
			found += 1
		else:
			pass

	if found > minChar or found < maxChar:
		counter += 1
	else:
		pass

print(counter)




