def do_decompression(phrase):
	print ""
	print phrase
	result = ''
	instr_end = phrase.find(')') + 1
	instr = phrase[:instr_end - 1].split('x')
	offset = int(instr[0])
	repeats = int(instr[1])
	for repeat in range(repeats):
		i = instr_end
		while i < instr_end + offset:
			if phrase[i] != '(':
				result += phrase[i]
				i += 1
			else:
				decompressed = do_decompression(phrase[i + 1:])
				result += decompressed[1]
				print phrase[i] + " ", i
				i += decompressed[0]
				print decompressed[0]
				print "it is now: " + phrase[i] + phrase[i + 1] + " ", i
	print "result: " + result
	return offset + instr_end,result

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