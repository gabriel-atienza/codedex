#rock paper scissors game
import random

print("================================\nRock Paper Scissors Lizard Spock\n================================")
print("")
print("1) ✊\n2) ✋\n3) ✌️\n4) 🦎\n5) 🖖")

player = int(input("Pick a number:   "))
computer = random.randint(1, 5)

print("")

if player == 1:
    print("You chose ✊")
elif player == 2:
    print("You chose ✋")
elif player == 3:
    print("You chose ✌️")
elif player == 4:
    print("You chose 🦎")
elif player == 5:
    print("You chose 🖖")
else:
    print("Invalid input. Please choose a number between 1 and 5.")

if computer == 1:
    print("CPU chose ✊")
elif computer == 2:
    print("CPU chose ✋")
elif computer == 3:
    print("CPU chose ✌️")
elif computer == 4:
    print("CPU chose 🦎")
elif computer == 5:
    print("CPU chose 🖖")

if player == 1: #player chose rock
    if computer == 1:   #CPU chose rock
        print("It's a tie!") #rock vs rock
    elif computer == 2: #CPU chose paper
        print("The CPU won!") #rock loses to paper
    elif computer == 3: #CPU chose scissors
        print("The player won!") #rock beats scissors
    elif computer == 4: #CPU chose lizard
        print("The player won!") #rock crushes lizard
    else: #CPU chose spock
        print("The CPU won!") #spock vaporizes rock
elif player == 2:   #player chose paper
    if computer == 1:   #CPU chose rock
        print("The player won!")    #paper beats rock
    elif computer == 2: #CPU chose paper
        print("It's a tie!") #paper vs paper
    elif computer == 3: #CPU chose scissors
        print("The CPU won!") #scissors cuts paper
    elif computer == 4: #CPU chose lizard
        print("The CPU won!") #lizard eats paper
    else:   #CPU chose spock
        print("The player won!")    #paper disproves spock
elif player == 3:  #player chose scissors
    if computer == 1:  #CPU chose rock
        print("The CPU won!") #scissors loses to rock
    elif computer == 2: #CPU chose paper
        print("The player won!") #scissors cuts paper
    elif computer == 3: #CPU chose scissors
        print("It's a tie!") #scissors vs scissors
    elif computer == 4: #CPU chose lizard
        print("The player won!") #scissors decapitates lizard
    else: #CPU chose spock
        print("The CPU won!") #spock smashes scissors
elif player == 4:   #player chose lizard
    if computer == 1: #CPU chose rock
        print("The CPU won!") #rock crushes lizard
    elif computer == 2: #CPU chose paper
        print("The player won!") #lizard eats paper
    elif computer == 3: #CPU chose scissors
        print("The CPU won!") #scissors decapitates lizard
    elif computer == 4: #CPU chose lizard
        print("It's a tie!") #lizard vs lizard
    else: #CPU chose spock
        print("The player won!") #lizard poisons spock
elif player == 5:   #player chose spock
    if computer == 1: #CPU chose rock
        print("The player won!") #spock vaporizes rock
    elif computer == 2: #CPU chose paper
        print("The CPU won!") #paper disproves spock
    elif computer == 3: #CPU chose scissors
        print("The player won!") #spock smashes scissors
    elif computer == 4: #CPU chose lizard
        print("The CPU won!") #lizard poisons spock
    else: #CPU chose spock
        print("It's a tie!") #spock vs spock
else:
    print("Invalid input. Please choose a number between 1 and 5.")