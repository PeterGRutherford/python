#Reddit user "eggeggs". My code is below. I also had to edit this one to make it work  :]
import random

player_points = 0
cpu_points = 0
hold_player = 0
hold_cpu = 0

print("Welcome to PIG! \n RULES \n  If you roll '1': No new points, next player's turn \n  If you roll '2-6': either roll again 'r' or hold 'h' \n  If hold: sum of all rolls is added to score & turn passes to other players \n       !!!!FIRST TO 100 OR MORE POINTS WINS!!!!")

print("It is your turn to roll the dice.")

while player_points < 100 and cpu_points < 100: # while both are under 100
    user_turn = input("Enter 'r' to roll or 'h' to hold: ")
    if user_turn == 'r':
        roll = random.randint(1,6)
        if roll != 1:
            hold_player += roll
            print("You rolled:", roll ,"\nYour score:", hold_player)
                continue
        else:
            print("You rolled:" + str(roll) + "\n" "0 points earned""\n""Current score:" + str(player_points))

    else:
        user_turn == 'h'
        player_points += hold_player
        print("You have chosen to hold \nYour score:" + str(player_points))


while player_points < 100 and cpu_points < 100:
    if hold_cpu < 20:
        roll = random.randint(1,6)
    if roll != 1:
        hold_cpu += roll
        print("CPU rolled:" + str(roll) + "\nCPU score:" + str(hold_player))
            continue
    else:
        print("CPU rolled:" + str(roll) + "\n" "0 points earned""\n""Current score:" + str(player_points))
        break
'''
This is my code. Although it doesn't work, I spent at least 6 hours or more on it
I dont want to quit it but I have other finals, I understand the code above.

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
'''