import random
start = input('請決定隨機數字範圍開始值: ')
end = input('請決定隨機數字範圍結束值: ')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
	count += 1
	x = input('請輸入數字:')
	x = int(x)
	if x == r:
		print('你共猜了', count,'次,終於猜對了!')
		break
	elif x < r:
		print('比答案小!')
	elif x > r:
		print('比答案大!')
	print('這是你猜的第', count, '次')
