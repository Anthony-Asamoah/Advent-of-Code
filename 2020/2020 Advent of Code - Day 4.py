import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s- %(message)s')
#
# logging.disable(logging.DEBUG)
# logging.disable(logging.INFO)

logging.info('Program Started!')

# get data from file
file = open('Day 4.txt', 'r')
data = file.read()
file.close()

data = data.split('\n\n')

stringed = ''

valid = 0
invalid = 0
for passport in data:
	passport = passport.split('\n')
	stringed += '\n\n\nPassport -> ' + str(passport) + '\n'

	# organize passport details into a sorted list
	x = []
	for i in range(0, len(passport)):
		# temp = list(passport[i].split())

		if ' ' in passport[i]:
			temp = []
			temp = passport[i].split()
			for j in temp:
				x.append(j)
		else:
			x.append(passport[i])

	passport = sorted(x)

	# delete cid from list since it is not required

	if passport[1][:3] == 'cid':
		del (passport[1])
	else:
		pass

	stringed += f'New: {passport}\n'

	# strip data from detail leaving headers only
	headers = []
	values = []
	for detail in passport:
		position = passport.index(detail)
		detail = detail.split(':')
		headers.append(detail[0])  # Part 1
		values.append(detail[1])  # Part 2

	logging.debug(f"Headers: {headers}, #:{len(headers)}\n")

	# # Check if necessary headers and details are in passport (Validity)
	Valid = False
	if len(headers) == 7:
		Valid = True
		while Valid:
			if int(values[0]) in range(1920, 2003):
				logging.info('byr checked and true')
			else:
				logging.info('byr checked and false')
				Valid = False
				break
			if values[1] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
				logging.info('ecl checked and true')
			else:
				logging.info('ecl checked and false')
				Valid = False
				break
			if int(values[2]) in range(2020, 2031):
				logging.info('eyr checked and true')
			else:
				logging.info('eyr checked and false')
				Valid = False
				break
			if values[3].startswith('#') and values[3][1:].isalnum() and len(values[3][1:]) == 6:
				logging.info('hcl checked and true')
			else:
				logging.info('hcl checked and false')
				Valid = False
				break
			if (values[4].endswith('cm') and int(values[4][:-2]) in range(150, 194)) or \
				(values[4].endswith('in') and int(values[4][:-2]) in range(59, 77)):
				logging.info('hgt checked and true')
			else:
				logging.info('hgt checked and false')
				Valid = False
				break
			if int(values[5]) in range(2010, 2021):
				logging.info('iyr checked and true')
			else:
				logging.info('iyr checked and false')
				Valid = False
				break
			if len(values[6]) == 9:
				for u in values[6]:
					if int(u) in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
						logging.info('pid checked and true')
					else:
						logging.info('pid checked and false')
						Valid = False
			else:
				Valid = False
				break

			break

	if Valid:
		valid += 1
	else:
		logging.info('Insufficient Details')
		invalid += 1

	logging.debug(f'Valid = {Valid}, #:{valid}, !#:{invalid}\n')

	stringed += f'Headers extracted -> {headers}\n'
	stringed += f'Values extracted -> {values}\n\n'

# show number of valid & invalid passports and Valid if sum = total passports
print(f'\n{valid} passports are valid. out of {invalid + valid}')

file = open('Day 4 log.txt', 'w')
file.write(stringed)
file.close()
