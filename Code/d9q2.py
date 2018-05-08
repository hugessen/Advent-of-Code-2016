def do_decompression(phrase):
	print ""
	print phrase
	result = ''
	instr_end = phrase.find(')') + 1
	instr = phrase[:instr_end - 1].split('x')
	offset = int(instr[0])
	repeats = int(instr[1])
	if phrase[instr_end: instr_end + offset].find('(') == -1:
		for i in range(repeats):
			# print "adding " + phrase[instr_end:instr_end + offset]
			result += phrase[instr_end:instr_end + offset]
		print result
	else:
		start = phrase[instr_end: instr_end + offset].find('(') + instr_end + 1
		result += do_decompression(phrase[start:])[1]
		for i in range(repeats):
			result += phrase[phrase[start:].find(')') + start + 1: instr_end + offset] # Exclude instructions
	return offset,result

pinput = open("Inputs/d9.txt").read().replace(" ","")
full = ""
i = 0

while i < len(pinput):
	if pinput[i] == '(':
		decompressed = do_decompression(pinput[i + 1:])
		full += decompressed[1]
		i += decompressed[0] + pinput[i + 1:].find(')') - 1
		print "new start: " + pinput[i]
		print "full:", full
	else:
		full += pinput[i]
		i += 1
print full
print len(full)