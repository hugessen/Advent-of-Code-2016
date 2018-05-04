def turn(left_or_right):
	global c_dir
	if c_dir[X] == 1:
		c_dir = [0, -1*left_or_right]
	elif c_dir[X] == -1: 
		c_dir = [0, 1*left_or_right]
	elif c_dir[Y] == 1:
		c_dir = [1*left_or_right, 0]
	elif c_dir[Y] == -1:
		c_dir = [-1*left_or_right, 0]

pinput = open('Inputs/d1.txt').read().split(", ")

X = 0
Y = 1
LEFT = -1
RIGHT = 1
c_dir = [0,1]
pos = [0,0]
visited = dict()

for move in pinput:
	if move[0] == 'L':
		turn(LEFT)
	elif move[0] == 'R':
		turn(RIGHT)
	for i in range(int(move[1:])):
		pos[X] += c_dir[X]
		pos[Y] += c_dir[Y]
		key = str(pos[X] + pos[Y])
		if key in visited:
			found = False
			for visited_pos in visited[key]:
				if visited_pos == tuple(pos):
					found = True
					print "Distance to closest double visit = %d" % (abs(pos[X]) + abs(pos[Y]))
					break
			if found is False:
				visited[key].append( (pos[X], pos[Y]) )
		else:
			visited[key] = [(pos[X], pos[Y])]

print "Distance = %d" % (abs(pos[X]) + abs(pos[Y]))