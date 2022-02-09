import time

file = open('C:/users/dd/desktop/Advent of code 2020.txt', 'r')
data = file.read().split('\n')
file.close()

length = len(data)

def ADV():
	for x in range(length):
		i = int(data[x])

		for y in range(length):
			j = int(data[y])

			for z in range(length):
				k = int(data[z])

				add = i + j + k

				if add == 2020:
					result = f'\n\n{i} * {j} * {k} = {i * j * k}'
					return print(result)
				else:
					pass

	print("\nComplete")


ADV()