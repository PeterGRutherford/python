


import random
round = 0
turn = 0
pone = 0
bot = 0
round = 0
rchoice = random.choice(['true','false'])
choice = rchoice
yesno = random.choice(['yes','no'])
di = random.randint(1,6)
sn = 0
print("Hello! Welcome to the game Pig! The rules are as follows:\nWe will go in turns, randomly picked at the start.\nIf you roll it and it lands on numbers 2-6,\nyou gain those points and you can decide to go again.\nIf you land on 1, your points reset!\n")
a = input("Press Enter")
while(round != 10):
    if(turn == 2):
        round = round + 1
        turn = 0
    while(rchoice or choice == "true"):
        print("Your turn!")
        b = input("Roll?(yes, no): ")
        if(b == "No" or "no" or "n" or "N"):
            turn = turn + 1
            print("Your points: " + str(pone))
            di = random.randint(1,6)
            choice = "false"
        elif(b == "Yes" or "yes" or "y" or "Y"):
            print("You rolled a " + str(di) + "!")
            if(di == 1):
                print("Points reset!")
                pone = 0
                turn = turn + 1
                choice = "false"
    while(rchoice or choice == "false"):
        print("My turn!")
        if(yesno == "no"):
            turn = turn + 1
            print("My points: " + str(bot))
            di = random.randint(1,6)
            yesno = random.choice(['yes','no'])
            choice = "true"
        elif(yesno == "yes"):
            print("You rolled a " + str(di) + "!")
            if(di == 1):
                print("Points reset!")
                bot = 0
                turn = turn + 1
                choice = "true"
            bot = bot + di
            print("Bot total: " + str(bot))
