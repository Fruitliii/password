pw = 'a123456'
chance = 0
lchance = 3
while True:
	while chance < 3:
		pww = input('please type your password here: ')
		if pww == pw:
			print('Successfully log in.')
			break
		else:
			lchance = lchance - 1
			print('You have ', lchance, 'more chance')
			chance = chance + 1
	break