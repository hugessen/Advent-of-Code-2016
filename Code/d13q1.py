GRID_SIZE = 40
X = 0
Y = 1

def is_wall(x,y):
	temp = x*x + 3*x + 2*x*y + y + y*y + 1362
	temp = to_bin(temp)
	return sum([1 for bit in temp if bit == "1"]) % 2 == 1

def to_bin(num):
	if num == 0:
		return ""
	return to_bin(num // 2) + str(num % 2)

def get_neighbours(x,y):
	options = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
	neighbours = []
	for option in options:
		if not (option[X] < 0 or option[X] > GRID_SIZE or option[Y] < 0 or option[Y] > GRID_SIZE) and not is_wall(option[X],option[Y]):
			neighbours.append(option)
	return neighbours

def create_grid():
	grid = [[] for i in range(GRID_SIZE)]
	for y in range(GRID_SIZE):
		for x in range(GRID_SIZE):
			if is_wall(x,y):
				grid[y].append("#")
			else:
				grid[y].append(".")
	return grid

def shortest_path_bfs(start, end):
	global grid
	level = [start]
	discovered = {}
	i = 0
	count = 0
	while i < 50:
		new_level = []
		for point in level:
			for v in get_neighbours(point[0], point[1]):
				if str(v) not in discovered:
					discovered[str(v)] = point
					new_level.append(v)
					count += 1
		level = new_level
		i += 1
	print count
	path = []
	curr = end
	while discovered[str(curr)] != start:
		curr = discovered[str(curr)]
		grid[curr[Y]][curr[X]] = "O"
		path.append(curr)
	return path

grid = create_grid()
dest = (31,39)
shortest_path = shortest_path_bfs((1,1),dest)
print len(shortest_path)
for i in range(len(grid)):
	print "".join(grid[i])