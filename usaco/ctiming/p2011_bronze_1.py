#
#
#
# 2011 bronze 1


def minutes_spent(d, h, m):
	if h > 23 or m > 59:
		return -1
	time_difference = (h*60+m)-(11*60+11)
	day_difference = (d-11)*60*24
	total_mins = time_difference + day_difference
	if total_mins < 0:
		return -1
	return total_mins

f = open('I.6', 'r')
line = f.readlines()[0]
f.close()

d, h, m = line.split(' ')
out = open('ctiming.out', 'w')
out.write(str(minutes_spent(int(d), int(h), int(m))))
out.close()



