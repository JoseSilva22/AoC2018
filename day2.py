from collections import Counter

ids = open('input2.txt').read().splitlines()


def part1():
	checksum = {2:0, 3:0}
	for _id in ids:
		c = Counter(_id)
		occurrences = list(set(filter(lambda x: x == 2 or x == 3, c.values())))
		if len(occurrences) == 2:
			checksum[2] += 1
			checksum[3] += 1
		elif len(occurrences) > 0:
			checksum[occurrences[0]] += 1
	
	print(checksum[2]*checksum[3])



def part2():
	for i in range(len(ids)):
		for j in range(i,len(ids)):
			if hamming_distance(ids[i], ids[j]) == 1:
				print("".join([x for x, y in zip(ids[i], ids[j]) if x == y]))
				return
	
		



def hamming_distance(s1, s2):
	assert len(s1) == len(s2)
	return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

	

if __name__ == "__main__":
	part1()
	part2()
