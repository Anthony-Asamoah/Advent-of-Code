import logging, pprint

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.disable(logging.DEBUG)


def main():
	try:
		file = open(r'Day 3.txt', 'r')
		data = file.read()
		file.close()
		logging.info('File Load complete')
	except Exception:
		logging.error('File Load Unsuccessful')

	data = data.split('\n')
	column = len(data)
	row = len(data[0])
	logging.debug(f'Row: {row}, Column: {column}\n')

	# Part I
	# ##################################################
	# trees = 0
	# x = 0
	# y = 0
	# for i in range(column):
	# 	if x >= row:
	# 		x = x - row
	# 		logging.debug(f'{i} -> x: {row + x}: {x}\n')
	# 	else:
	# 		logging.debug(f'{i} -> x: {x}')
	#
	# 	z = data[y][x]
	# 	x += 3
	# 	y += 1
	#
	# 	if z == '#':
	# 		trees += 1
	# 		logging.debug(f'{z} -> {trees} Trees')
	# 	else:
	# 		pass
	#
	#
	# 	print(f"There are {trees} Tree(s)")
	# ##################################################

	# Part II
	# ##################################################################

	def treeCounter(a, b):
		trees = 0
		x = 0
		y = 0

		column = len(data)//b

		for i in range(column):
			if x >= row:
				x = x - row
				logging.debug(f'{i} -> x: {row + x}: {x}\n')
			else:
				logging.debug(f'{i} -> x: {x}')

			z = data[y][x]
			x += a
			y += b

			if z == '#':
				trees += 1
			else:
				pass
		logging.info(f'Trees: {trees} for {a} & {b} with column as {column} out of {len(data)}')
		return trees

	product = (treeCounter(1, 1) * treeCounter(3, 1) * treeCounter(5, 1) * treeCounter(7, 1) * treeCounter(1, 2))

	# ##################################################################

	print(f"All trees combined give: {product}")


if __name__ == '__main__':
	main()
