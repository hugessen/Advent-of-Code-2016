def is_valid(vals):
	max_side = max(vals)
	return sum(vals) > (2 * max_side)

pinput = open('Inputs/d3.txt').read().split('\n')                                                                                                                                                                                                                                                                                                                                                                

num_triangles = 0

for line in pinput:
	sides = [int(side) for side in line.split()]
	if is_valid(sides):
		num_triangles += 1

print num_triangles