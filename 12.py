####### Scope ##########

# enemies= 1
# def increaseenemies():
#     enemies=2
#     print(f"The enemies inside the function is {enemies}")
# increaseenemies()
# print(f" The enemies outside the function is {enemies}")

#Modfying the Global Enemy
# enemies= 1
# def increaseenemies():
#     global enemies
#     enemies+=1
#     print(f"The enemies inside the function is {enemies}")
# increaseenemies()
# print(f" The enemies outside the function is {enemies}")

#Number Guessing Game 
import random
import os

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def startgame():
    print("Hello and Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    selectednumber = random.randint(1, 100)

    level = input("For difficulty level type 'hard' or 'easy': ").lower()

    if level == "hard":
        lives = 5
    else:
        lives = 10

    while lives > 0:
        try:
            guess = int(input("Guess the number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess > selectednumber:
            print("Too high.")
        elif guess < selectednumber:
            print("Too low.")
        else:
            print(" Correct! You win!")
            break

        lives -= 1
        if lives == 0:
            print(" Game Over. You've run out of lives.")
            print(f"The number was: {selectednumber}")
        else:
            print(f"You have {lives} lives left. Try again.") 


# Game loop
while True:
    clear_console()
    startgame()
    restart = input("Do you want to play again? Type 'y' for yes and 'n' for no: ").lower()
    if restart != 'y':
        print("Thanks for playing! See you next time")
        break ## Exit  the Loop 














