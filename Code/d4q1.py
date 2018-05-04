import string
pinput = open('Inputs/d4.txt').read().split('\n')
total = 0
real_rooms = []
alphabet = list(string.ascii_lowercase)
for line in pinput:
	freq = dict()
	i = 0
	while i < len(line) and not line[i].isdigit():
		if line[i] != '-':
			if line[i] in freq:
				freq[line[i]] += 1
			else:
				freq[line[i]] = 0
		i += 1
	sec_id = int(line[i:line.find('[')])
	their_checksum = line[line.find('[') + 1:line.find(']')]
	checksum = ''
	char_freqs = [(char,freq[char]) for char in freq.keys()]
	char_freqs = sorted(char_freqs,key=lambda tup: (-tup[1],tup[0]))

	for x in range(5):
		checksum += char_freqs[x][0]
	if checksum == their_checksum:
		total += sec_id
		room = line[:i].replace("-"," ")
		new_str = ''
		for i in range(len(room)):
			if room[i] != ' ':
				new_str += alphabet[(ord(room[i]) - 97 + sec_id) % 26]
			else:
				new_str += ' '
		print new_str, sec_id

print total