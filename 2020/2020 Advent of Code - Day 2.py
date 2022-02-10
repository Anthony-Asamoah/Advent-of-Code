from pprint import pprint
from re import compile, findall
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

logging.debug('start of program\n')
file = open('Day 2.txt', 'r')
data = file.read()
file.close()
logging.info('File Loading Complete!\n')

lines = data.split('\n')
counter = 0

for i in range(len(lines)):
	lines[i] = lines[i].split()

	charLen = lines[i][0].split('-')
	minChar = int(charLen[0])
	maxChar = int(charLen[1])

	Raw_letter = lines[i][1]
	letter = str(Raw_letter[0])

	pwd = lines[i][2]

	# Part 1
	# ######################################
	# found = 0
	# Valid = False
	# logging.debug("letter scan started")
	# for j in pwd:
	# 	if j == letter:
	# 		found += 1
	# 	else:
	# 		pass
	#
	# if minChar <= found <= maxChar:
	# 	Valid = True
	# 	counter += 1
	# else:
	# 	pass
	#
	# logging.info(f"Found: {found}, {letter}, {minChar}:{pwd}:{maxChar}, Valid: {Valid}\n")
    #
	# ######################################

	# Part 2
	# ######################################
	Valid = False
	logging.debug("Letter scan initiated!")

	check = False
	checkmate = False

	try:
		if pwd[minChar - 1] == letter:
			check = True
			logging.debug(f'{pwd[minChar - 1] == letter} for {letter} == {pwd[minChar - 1]}')
			if pwd[maxChar - 1] != letter:
				check = True
				logging.debug(f'{pwd[maxChar - 1] != letter} for {letter} != {pwd[maxChar - 1]}')
				Valid = True
				counter += 1
			else:
				logging.debug(f'{pwd[maxChar - 1] != letter} for {letter} != {pwd[maxChar - 1]}')
				pass
		else:
			pass

		if pwd[minChar - 1] != letter:
			check = True
			logging.debug(f'{pwd[minChar - 1] != letter} for {letter} != {pwd[minChar - 1]}')
			if pwd[maxChar - 1] == letter:
				check = True
				logging.debug(f'{pwd[maxChar - 1] == letter} for {letter} == {pwd[maxChar - 1]}')
				Valid = True
				counter += 1
			else:
				logging.debug(f'{pwd[maxChar - 1] == letter} for {letter} == {pwd[maxChar - 1]}')
				pass
		else:
			pass
	except IndexError:
		pass

	try:
		logging.info(f" '{letter}', {minChar}:{pwd}:{maxChar}, Valid: {Valid}, Counter: {counter}\n")
	except IndexError:
		logging.info(
			f" {letter}, {minChar}:{pwd}:{maxChar}, Valid: {Valid}, Counter: {counter}\n")
	# ######################################


print(f"\n#: {counter}")

logging.debug('End of program')
