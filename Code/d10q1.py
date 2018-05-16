import sys
pinput = open("Inputs/d10.txt").read().split("\n")
bots = [None for x in range(210)]
outputs = [None for x in range(21)]
outputted_count = 0
MIN = 0
MAX = 1
found = False

def insert(bot_num, value):
	global found
	if bots[bot_num] is None:
		bots[bot_num] = [value,0]
	elif bots[bot_num][MAX] == 0:
		bots[bot_num][MAX] = value
		bots[bot_num] = sorted(bots[bot_num])

for line in pinput:
	words = line.split(" ")
	if words[0] != "value":
		continue
	bot_num = int(words[5])
	insert(bot_num,int(words[1]))

for bot in bots:
	print bot

while outputted_count < len(outputs) - 1:
	for line in pinput:
		words = line.split(" ")
		if words[0] != "bot":
			continue
		bot_num = int(words[1])
		bot = bots[bot_num]
		if bot is None or bot[MAX] == 0:
			continue
		print line
		print "bot: "
		print bot
		lower = int(words[6])
		higher = int(words[11])
		if words[5] == "bot":
			insert(lower,bot[MIN])
			print "lower: "
			print bots[lower]
		elif words[5] == "output":
			outputs[lower] = bot[MIN]
			outputted_count += 1

		if words[10] == "bot":
			insert(higher,bot[MAX])
			print "higher: "
			print bots[higher]
		elif words[5] == "output":
			outputs[higher] = bot[MAX]
			outputted_count += 1

		bots[bot_num] = None

print outputs[0] * outputs[1] * outputs[2]
print ""
for output in outputs:
	print output