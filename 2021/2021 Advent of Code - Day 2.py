import logging


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


# Retrieving data from file
try:
    with open('Day 2.txt', 'r') as file:
        data = file.read().split('\n')
        logging.info('file read successfully')

except FileNotFoundError:
    logging.error('File cannot be found')

# Part I 
# ###########################################################################
'''
# Declaring position as variables where [depth is vertical]
vertical = 0
horizontal = 0

# Updating positions with data
for i in data:

    pos = i[:-2]
    amt = int(i[-1])

    if  pos == 'forward':
        horizontal = horizontal + amt
        logging.info(f"{pos}: {amt} -- H: {horizontal}, V: {vertical}\n")
    elif pos == 'up':
        vertical = vertical - amt
        logging.info(f"{pos}: {amt} -- H: {horizontal}, V: {vertical}\n")
    elif pos == 'down':
        vertical = vertical + amt
        logging.info(f"{pos}: {amt} -- H: {horizontal}, V: {vertical}\n")
'''
# ###########################################################################

# Part II
# ###########################################################################
# Declaring position as variables where [depth is vertical]
vertical = 0
horizontal = 0
aim = 0

# Updating positions with data
for i in data:

    pos = i[:-2]
    amt = int(i[-1])

    if  pos == 'forward':
        horizontal = horizontal + amt
        vertical = vertical + (aim * amt)
        logging.info(f"{pos}: {amt} -- H: {horizontal}, V: {vertical}, A: {aim}\n")
    elif pos == 'up':
        aim = aim - amt
        logging.info(f"{pos}: {amt} -- H: {horizontal}, V: {vertical}, A: {aim}\n")
    elif pos == 'down':
        aim = aim + amt
        logging.info(f"{pos}: {amt} -- H: {horizontal}, V: {vertical}, A: {aim}\n")


# showing positions
print("=".center(50, "="))
print(f"\n\nHorizontal position is {horizontal} and depth is {vertical}")

# Multiplying horizontal by vertical
product = horizontal * vertical
print(f"\nFinal product is {product}")