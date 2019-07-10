import numpy as np
import matplotlib.pyplot as plt


def part1(fabric, claims):
	overlaps = 0
	for claim in claims:
		args = claim.split(" ")
		y, x = map(int, args[2][:-1].split(","))
		len_y, len_x = map(int, args[3].split("x"))
		
		for i in range(x, x + len_x):
			for j in range(y, y + len_y):
				fabric[i,j] += 1
				if fabric[i,j] == 2:
					overlaps += 1

	print(overlaps)
	#plt.imshow(fabric, cmap='hot', interpolation='nearest')
	#plt.show()

def part2(fabric, claims):
	for claim in claims:
		args = claim.split(" ")
		claim_id = args[0][1:]
		y, x = map(int, args[2][:-1].split(","))
		len_y, len_x = map(int, args[3].split("x"))
		
		for i in range(x, x + len_x):
			for j in range(y, y + len_y):
				fabric[i,j] += 1

	for claim in claims:
		args = claim.split(" ")
		claim_id = args[0][1:]
		y, x = map(int, args[2][:-1].split(","))
		len_y, len_x = map(int, args[3].split("x"))
		overlaps = False
		
		for i in range(x, x + len_x):
			for j in range(y, y + len_y):
				if fabric[i,j] > 1:
					overlaps = True
					continue
		
		if overlaps == False:
			print(claim_id)
			break

		overlaps = False



if __name__ == "__main__":
	fabric = np.zeros((1000,1000))
	claims = open('input3.txt').read().splitlines()

	#part1(fabric, claims)
	part2(fabric, claims)
