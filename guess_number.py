import random
r = random.randint(1, 100)
while True:
	x = input('請輸入數字:')
	x = int(x)
	if x == r:
		print('終於猜對了!')
		break
	else:
		if x < r:
			print('比答案小!')
		if x > r:
			print('比答案大!')
