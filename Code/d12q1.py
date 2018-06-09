def value_of(v,registers):
	try:
		return int(v)
	except:
		return registers[v]

pinput = open("../Inputs/d12.txt").read().split("\n")

registers = { 'a':0, 'b':0, 'c':1, 'd':0 }
i = 0

while i < len(pinput):
	line = pinput[i].split(" ")
	if line[0] == "cpy":
		registers[line[2]] = value_of(line[1], registers)
	elif line[0] == "inc":
		registers[line[1]] += 1
	elif line[0] == "dec":
		registers[line[1]] -= 1
	elif line[0] == "jnz":
		if value_of(line[1], registers) != 0:
			i += value_of(line[2], registers) - 1
	i += 1

print registers