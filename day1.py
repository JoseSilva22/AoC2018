from functools import reduce

freqs = []

with open('input1.txt') as f:
	for line in f:
		freqs.append(int(line))

def part1():
	return reduce(lambda x, y : x + y, freqs)

def part2():
	found = False
	state = 0
	states = {}
	while not found:
	    for freq in freqs:
	            state += freq
	            if state in states:
	                    found = True
	                    break
	            states[state] = True
	return state


if __name__ == "__main__":
	print(part1())
	print(part2())