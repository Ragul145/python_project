import random

option = ("ROCK","PAPER","SCISSORS")
running = True

while running:
    player = None
    computer = random.choice(option)

    while player not in option:
        player = input("Enter a choice(ROCK,PAPER,SCISSORS):").upper()
        
    print(f"Player:{player}")
    print(f"Computer:{computer}")

    if player == computer:
           print("is tie")
    elif player == "ROCK" and computer == "SCISSORS":
           print("Player WON!") 
    elif player == "PAPER" and computer == "ROCK":
           print("Player Won!")    
    elif player == "SCISSORS" and computer == "PAPER":
           print("You Won!")
    else:
          print("Computer won!")  

    again = input("play again?(Y/N):").upper()
    if  again == "N":
           running = False

print("thanks for playing")