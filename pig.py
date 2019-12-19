import random

pone = 0
bot = 0
rchoice = random.choice(['true','false'])
choice = rchoice
di = random.randint(1,6)
sn = 0
print("Hello! Welcome to the game Pig! The rules are as follows:\nWe will go in turns, randomly picked at the start.\nIf you roll it and it lands on numbers 2-6,\nyou gain those points and you can decide to go again.\nIf you land on 1, your points reset!\n")
a = input("Press any key and enter to start")
while(bot < 100 and pone < 100):
	if(rchoice == "true"):
		print("Players turn!")
		a = input("Roll?(yes or no): ")
		while(a == "yes" or a== "Yes"):
			di = random.randint(1,6)
			sn = sn + di
			print("You rolled a " + str(di) + "!")
			if(di == 1):
				print("You rolled a one!")
				sn = 0
				rchoice = "false"
			else:
				pone = pone + sn
				print("Your score: " + str(pone))
				sn = 0
				a = input("Roll?(yes or no): ")
		if(a == "no" or a == "No"):
			print("Turn ending score: " + str(pone))
			rchoice = "false"
	while(rchoice == "false"):
		print("Bot's turn!")
		di = random.randint(1,6)
		yesno = random.choice(["yes","no"])
		if(yesno == "yes"):
			print("I'm rolling!")
			yesno = random.choice(["yes","no"])
			di = random.randint(1,6)
			sn = sn + di
			print("I rolled a " + str(di) + "!")
			if(di == 1):
				print("I rolled a one!")
				sn = 0
				rchoice = "true"
			else:
				bot = bot + sn
				print("Bot score: " + str(bot))
				sn = 0
				yesno = random.choice(["yes","no"])
		if(yesno == "no"):
			print("My turn ending score: " + str(bot))
			rchoice = "false"
			
print("Final Score:")
print("Player = " + str(pone))
print("bot = " + str(bot))
