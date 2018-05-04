def is_valid(vals):
	max_side = max(vals)
	return sum(vals) > (2 * max_side)

pinput = open('Inputs/d3.txt').read().split('\n')
total_triangles = len(pinput)
count = 0
for i in range(len(pinput)):
	pinput[i] = map(int,pinput[i].split())

i = 0
while i < total_triangles:
	for x in range(3):
		vals = (pinput[i][x],pinput[i+1][x],pinput[i+2][x])
		if is_valid(vals):
			count += 1
	i += 3
print count