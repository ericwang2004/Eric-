#
#
#
# 2011 bronze 2

def correct_number(b2, b3):
	b2 = str(b2)
	b3 = str(b3)
	for i in range(2):
		for j in range(3):
			for x in range(len(b2)):
				for y in range(len(b3)):
					new_b2 = b2[:x]+str(i)+b2[x+1:]
					new_b3 = b3[:y]+str(j)+b3[y+1:]
					b2_dec = int(new_b2, 2)
					b3_dec = int(new_b3, 3)
					if b2_dec == b3_dec:
						return b2_dec

f = open('I.10', 'r')
lines = f.readlines()
f.close()

x1 = lines[0]
x2 = lines[1]

out = open('digits.out', 'w')
out.write(str(correct_number(x1, x2)))
out.close()


