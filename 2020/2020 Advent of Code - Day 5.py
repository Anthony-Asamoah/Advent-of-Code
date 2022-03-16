import logging
from collections import OrderedDict as order
from pprint import pprint as pp

logging.basicConfig(filename='Log.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.disable(level=logging.INFO)


def main():
	# get data from file
	try:
		with open('Day 5.txt', 'r') as file:
			data = file.read().split('\n')
			logging.info('File read successful\n')
	except FileNotFoundError:
		logging.critical("File not found\n")

	counter = 0  # to store highest seat ID
	S_id_list = []  # list of each seat id

	for i in data:  # handle each boarding pass
		# extract data
		row = i[:-3]
		col = i[-3:]

		logging.debug(F"{row} - {col}")

		rows = range(0, 128)
		cols = range(0, 8)

		# function to perform splits
		def split(item, req='mid'):
			upper = (item[-1] + 1)
			lower = item[0]
			length = len(item)

			mid = length // 2
			ans = (upper - mid)

			# for lower bound
			low = range(lower, ans)

			# for upper bound
			up = range(ans, upper)

			if req == 'up':
				return up
			elif req == 'low':
				return low
			else:
				return ans

		for j in row:  # derive row num
			if j == 'F':
				rows = split(rows, 'low')
				logging.debug(f'Row low {rows}')
			else:
				rows = split(rows, 'up')
				logging.debug(f'Row high {rows}')

		for j in col:  # derive col num
			if j == 'L':
				cols = split(cols, 'low')
				logging.debug(f'Col low {cols}')
			else:
				cols = split(cols, 'up')
				logging.debug(f'Col high {cols}')

		logging.debug(F"Row #: {rows}, Col #: {cols}\n\n")

		# derive seat ID
		s_id = (rows[0] * 8) + cols[0]

		# Part I
		# ###########################################################
		'''	
			# return highest seat ID
				if s_id > counter:
					counter = s_id
				else:
					pass
		
			print(f"\nHighest seat ID is {counter}")
		
			return 1
			'''
		# ###########################################################

		# Part II
		# ###########################################################

		# get a list of all seat IDs
		s_details = {
			"Seat ID": s_id,
			"Row #": rows[0],
			"Col #": cols[0]
		}
		S_id_list.append(s_details)

		# sort the list
		S_id_list = sorted(S_id_list, key=lambda i: i['Seat ID'])

	# find missing IDs
	missing_id = 0
	for i in range(len(S_id_list)):
		item1 = S_id_list[i]['Seat ID']
		item2 = S_id_list[i+1]['Seat ID']

		if item2 - item1 == 1:
			pass
		else:
			missing_id = item1 + 1
			break
		print(item1, item2)

	print(f'missing: {missing_id}')

	return 1
	# ###########################################################


if __name__ == '__main__':
	main()
