import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s- %(message)s')

# logging.disable(logging.DEBUG)
# logging.disable(logging.INFO)

logging.info('Program Started!')

# todo; get data from file
file = open('Day 4.txt', 'r')
data = file.read()
file.close()

data = data.split('\n\n')

valid = 0
for passport in data:
	passport = passport.split('\n')

	# todo; organize passport details into a sorted list
	for detail in passport:
		position = passport.index(detail)

		if ' ' in detail:
			bundle = detail.split()
			del passport[position]

			for i in bundle:
				passport.append(i)
		else:
			pass
	passport = sorted(passport)

	# todo: strip data from detail leaving headers only
	headers = []
	for detail in passport:
		position = passport.index(detail)
		detail = detail.split(':')
		headers.append(detail[0])

	logging.debug(f"Headers: {headers}, #:{len(headers)}")

	# todo: Check if necessary headers are in passport (Validity)
	Valid = False
	if len(headers) == 8 or (len(headers) == 7 and 'cid' not in headers):
		Valid = True
		valid += 1
	logging.debug(f'Valid = {Valid}, {valid}\n')

# todo; show number of valid & invalid passports and check if sum = total passports
print(f'\n{valid} passports are valid.')
