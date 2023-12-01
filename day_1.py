import re

sample = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
result = 0

for line in sample.split('\n'):
	first, last = (-1, ''), (-1, '')

	for num in nums:
		for itr in re.finditer(num, line):
			ind = itr.start()
			if ind > -1:
				if last[0] == -1 or ind >= last[0]:
					last = (ind, nums.index(num) % 10)
				if first[0] == -1 or ind <= first[0]:
					first = (ind, nums.index(num) % 10)

	result += (first[1] * 10 + last[1])

print(result)
