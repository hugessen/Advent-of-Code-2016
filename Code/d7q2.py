def is_valid(line):
	is_hnet = False
	abas = []
	babs = []
	for i in range(len(line) - 2):
		if line[i] == '[':
			is_hnet = True
		elif line[i] == ']':
			is_hnet = False
		if line[i] == line[i + 2]:
			seq = line[i:i+3]
			if is_hnet:
				babs.append(seq)
			else:
				abas.append(seq)
	for bab in babs:
		if inverse(bab) in abas:
			return True
	return False

def inverse(aba):
	return aba[1] + aba[0] + aba[1]

pinput = open("Inputs/d7.txt").read().split("\n")
print len([line for line in pinput if is_valid(line)])