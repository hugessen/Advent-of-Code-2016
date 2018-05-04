pinput = open('Inputs/d3.txt').read().split('\n')                                                                                                                                                                                                                                                                                                                                                                                     

# Another way to do it:
# print sum(vals[0] + vals[1] > vals[2]
#       for vals in [sorted([int(x) for x in line.split()])
#       for line in pinput])

num_triangles = 0

for line in pinput:
	sides = [int(side) for side in line.split(" ") if side != '']
	i = 0
	is_good = True
	while i < 3:
		if sides[i] + sides[(i + 1) % 3] <= sides[(i + 2) % 3]:
			is_good = False
			break
		i += 1
	if is_good:
		num_triangles += 1

print num_triangles