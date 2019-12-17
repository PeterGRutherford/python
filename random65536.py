import random
x = 0
y = x
while(x != 65536):
	y = random.randint(65, 90)
	x = x + 1
	print(chr(y))
	
