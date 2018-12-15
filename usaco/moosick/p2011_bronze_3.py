#
#
#
#


def transposed(chord1, chord2):
	# determines if chord2 is a transposed version of chord1
	chord1 = sorted(chord1)
	chord2 = sorted(chord2)
	common_diff = chord1[0] - chord2[0] # amount by which it is transposed
	for i in range(1, len(chord1)):
		if chord1[i] - chord2[i] != common_diff:
			return False
	return True
	
def moosick(notes, ruminant):
	N = len(notes)
	C = len(ruminant)
	indices = []
	for i in range(N-2):
		chord = [notes[n] for n in range(i, i+C)]
		if transposed(chord, ruminant):
			indices.append(i+1)
	return indices


f = open('I.10', 'r')
lines = f.readlines()
f.close()

notes = []
ruminant = []
N = int(lines[0])
C = int(lines[1+N])

for i in range(1, N+1):
	notes.append(int(lines[i]))
for i in range(2+N, 2+N+C):
	ruminant.append(int(lines[i]))

indices = moosick(notes, ruminant)
count = str(len(indices))

out = open('moosick.out', 'w')
out.write(count+'\n')
for i in indices:
	out.write(str(i)+'\n')
out.close()




	
