import collections
pinput = open("Inputs/d6.txt").read().split("\n")
letters = ["" for i in range(len(pinput[0]))]

for i in range(len(pinput)):
	for j in range(len(pinput[i])):
		letters[j] += pinput[i][j]

code = ''
for i in range(len(letters)):
	# code += collections.Counter(letters[i]).most_common(1)[0][0] Part 1
	code += collections.Counter(letters[i]).most_common()[-1][0][0]
print code