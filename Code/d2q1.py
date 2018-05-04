def move(direc):
	global pos
	if direc == 'U':
		pos[Y] -= 1
		if pos[Y] < 0:
			pos[Y] = 0
	elif direc =='R':
		pos[X] += 1
		if pos[X] > 2:
			pos[X] = 2
	elif direc =='D':
		pos[Y] += 1
		if pos[Y] > 2:
			pos[Y] = 2
	elif direc =='L':
		pos[X] -= 1
		if pos[X] < 0:
			pos[X] = 0

pinput = open('Inputs/d2.txt').read().split('\n')
code = ''
X = 0
Y = 1
pos = [1,1]
grid = (
	(1,2,3),
	(4,5,6),
	(7,8,9)
)

for line in pinput:
	for ch in line:
		move(ch)
	print grid[pos[Y]][pos[X]]