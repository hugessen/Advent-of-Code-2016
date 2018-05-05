import collections
pinput = open("Inputs/d8.txt").read().split("\n")

grid = [['.' for i in range(50)] for j in range(6)]

for line in pinput:
	words = line.split(" ")
	print words
	if words[0] == 'rect':
		dim = map(int,words[1].split("x"))
		for y in range(dim[1]):
			for x in range(dim[0]):
				grid[y][x] = '#'
	elif words[0] == 'rotate':
		row_col = int(words[2][2:])
		offset = int(words[4])
		if words[1] == 'row':
			width = len(grid[0])
			new_row = ['' for i in range(width)]
			for i in range(offset, offset+width):
				new_row[i % width] = grid[row_col][i - offset]
			grid[row_col] = new_row
		elif words[1] == 'column':
			height = len(grid)
			new_row = ['' for i in range(height)]
			for i in range(offset, offset+height):
				new_row[i % height] = grid[i - offset][row_col]
			for i in range(height):
				grid[i][row_col] = new_row[i]

count = 0
for i in range(len(grid)):
	count += collections.Counter(grid[i])['#']
	print ''.join(grid[i])
print count