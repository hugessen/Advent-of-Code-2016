pinput = open("Inputs/d9.txt").read().replace(" ","")
full = ""
i = 0

while i < len(pinput):
	if pinput[i] == '(':
		instr_end = pinput[i:].find(')')
		instr = pinput[i+1:i+instr_end].split('x')
		offset = int(instr[0])
		repeats = int(instr[1])
		i += instr_end + 1
		for j in range(repeats):
			full += pinput[i:i + offset]
		i += offset
	else:
		full += pinput[i]
		i += 1
print full
print len(full)