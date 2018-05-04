def move(direc):
	global pos
	prev = pos[:]
	if direc == 'U':
		pos[Y] -= 1
	elif direc =='R':
		pos[X] += 1
	elif direc =='D':
		pos[Y] += 1
	elif direc =='L':
		pos[X] -= 1

	if current_char() == -1:
		pos = prev[:]


def current_char():
	global pos
	return grid[pos[Y]][pos[X]]

pinput = open('Inputs/d2.txt').read().split('\n')
code = ''
X = 0
Y = 1
pos = [3,3]
grid = (
	(-1, -1,  -1,  -1,  -1,  -1,  -1),
	(-1, -1,  -1,   1,  -1,  -1,  -1),
	(-1, -1,   2,   3,   4,  -1,  -1),
	(-1,  5,   6,   7,   8,   9,  -1),
	(-1, -1,  'A', 'B', 'C', -1,  -1),
	(-1, -1,  -1,  'D', -1,  -1,  -1),
	(-1, -1,  -1,  -1,  -1,  -1,  -1),
)

for line in pinput:
	print pos
	for ch in line:
		move(ch)
	print current_char()
