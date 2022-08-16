import random

while True:
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
         player = input("Choose: Rock, Paper, or Scissors?: ").lower()

    if player == computer:
            print("Computer: ",computer)
            print("Player: ",player)
            print("It is a tie!\n")

    elif player == "rock":
         if computer == "paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Paper coveres rock, you lose!\n")
    if computer == "scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Rock beats scissors, you win!\n")

    elif player == "scissors":
         if computer == "rock":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Rock beats scissors, you lose!\n")
         if computer == "paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Scissors cut paper, you win!\n")
    
    elif player == "paper":
         if computer == "scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Paper gets cut, you lose!\n")
         if computer == "rock":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Paper coveres rock, you win!\n")


    play_again = input("Play again? (Yes/No): ").lower()

    if play_again != "yes":
            break

print("Thanks for playing :)")
        
#Code written & reserved by w0xt3r
