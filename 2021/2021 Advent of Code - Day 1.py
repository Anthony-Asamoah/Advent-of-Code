import re
from pprint import pprint

location = "C:/users/dd/desktop/values.txt"


def extractor():
	file = open(location, "r")
	values_string = file.read()

	regex = re.compile(r"\d+")
	Values = regex.findall(values_string)

	file.close()

	return Values


def main(Val):
	increment = 0
	decrement = 0
	equality = 0
	for i in range(2, len(Val)-1):
		a = int(Val[i-2]) + int(Val[i-1]) + int(Val[i])
		b = int(Val[i-1]) + int(Val[i]) + int(Val[i+1])
		
		if a < b:
			increment += 1
			# print("increase", increment)
		elif a == b:
			# print("Equal", equality)
			equality += 1
		else:
			# print("decrease", decrement)
			decrement += 1

	return increment, decrement, equality


Val = extractor()
increment, decrement, equality = main(Val)

print(f"\n Increase: {increment}, Decrease: {decrement}, Equal: {equality}\nTotal: {increment + decrement + equality}")
