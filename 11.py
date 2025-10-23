# BlackJack Project: The Casino Game
import random
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def judgement():
    print("Hello and Welcome to Black jack Game")
    cards = ["11", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "10", "10", "10"]

    usercards = int(random.choice(cards))
    computercards = int(random.choice(cards))

    print(f"Your first card is {usercards}")
    print(f"Computer's first card is {computercards}")

    roundtwo = input("Do you want to continue with round two? Write 'y' for yes and 'n' for no:\n").lower()
    if roundtwo == "y":
        roundtwofunction(usercards, computercards)
    elif roundtwo == "n":
        if usercards > computercards:
            print("Hurray! You won.")
        elif usercards < computercards:
            print("Sorry! You lost.")
        else:
            print("It's a draw!")

def roundtwofunction(usercards, computercards):
    cards = ["11", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "10", "10", "10"]

    usercards2 = int(random.choice(cards))
    computercards2 = int(random.choice(cards))

    totalusercards = usercards + usercards2
    totalcomputercards = computercards + computercards2

    print(f"Your cards are {usercards} and {usercards2}. Total = {totalusercards}")
    print(f"Computer cards are {computercards} and {computercards2}. Total = {totalcomputercards}")

    if totalusercards > 21:
        print("Bust!!! You lost. You exceeded 21.")
    elif totalcomputercards > 21:
        print("Hurray! You won. Computer busted.")
    elif totalusercards > totalcomputercards:
        print("Hurray! You won.")
    elif totalusercards < totalcomputercards:
        print("Bad luck! You lost. Computer is closer to 21.")
    else:
        print("It's a draw!")

# Start the game
judgement()

while True:
    restart = input("Do you want to start a fresh? Type 'y' for Yes or 'n' for No: ").lower()
    if restart == "y":
        clear_console()  # Clear the console before restarting
        judgement()
    elif restart == "n":
        print("You are Welcome again!")
        break
    else:
        print("Invalid input. Please type 'y' or 'n'.")

