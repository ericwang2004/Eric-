# explain why this runs in O(log n) and why it can't be better than log n
#
#
#


def index(l, element):
	lower = 0
	upper = len(l)-1
	while True:
		middle = (lower+upper)//2
		print(lower, upper, middle)
		if l[middle] == element:
			return middle
		elif lower + 1 == upper:
			if l[upper] != element:
				return -1
			else:
				return upper
		elif l[middle] < element:
			lower = middle
		else:
			upper = middle
	return middle

l = [1, 3, 7, 13, 16, 22]





