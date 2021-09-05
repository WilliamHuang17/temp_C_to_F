import random 
pw = 'a123456'
cnt = 0;
r = random.randint(1, 100)
while True:
	r_in = int(input('1~100 = ?'))
	if r == r_in:
		print('correct')
		break 
	else:
		print('not correct')
		if r > r_in:
			print('random bit > ', r_in)
		else:
			print('random bit < ', r_in)			