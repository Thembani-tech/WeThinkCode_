import random

win_map = { "rock": "scissors", "paper": "rock", "scissors": "paper" }
choices= list(win_map.keys())

player = input("Enter rock, paper, or scissors: ").lower()
computer = random.choice(choices)

print (f"you chose {player}, computer chose {computer}")
if player == computer:
    print("It's a tie!")
elif win_map[player] == computer:
    print("You win!")
else:
    print("You lose!")