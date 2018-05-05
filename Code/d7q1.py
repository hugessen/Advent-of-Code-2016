def has_abba(line):
	is_hnet = False
	has_good_abba = False
	for i in range(len(line) - 3):
		if line[i] == '[':
			is_hnet = True
		elif line[i] == ']':
			is_hnet = False
		if line[i] == line[i + 3] and line[i + 1] == line[i + 2] and line[i] != line[i + 1]:
			if is_hnet:
				return False
			has_good_abba = True
	return has_good_abba

pinput = open("Inputs/d7.txt").read().split("\n")
print len(pinput)
good_ips = [line for line in pinput if has_abba(line)]
print len(good_ips)