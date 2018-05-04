import md5
i = 0
count = 0
code = ''
code_2 = ['' for i in range(8)]
found = False
while count < 8:
	hsh = md5.new('ffykfhsq' + str(i)).hexdigest()
	if str(hsh[:5]) == '00000':
		code += hsh[5]
		print hsh
		if hsh[5].isdigit() and int(hsh[5]) in range(8) and code_2[int(hsh[5])] == '':
			print "adding {} to code in position {}".format(hsh[6],hsh[5])
			code_2[int(hsh[5])] = hsh[6]
			count += 1
	i += 1
print code_2