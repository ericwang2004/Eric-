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
	C = len(ruminant)
	N = len(notes)
	for i in range(N-2):
		chord = [notes[n] for n in range(i, i+C)]
		if transposed(chord, ruminant):
			print(chord)
	
