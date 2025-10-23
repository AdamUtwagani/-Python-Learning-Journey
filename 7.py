#step1
word_list=["baby", "love", "sweet"]
import random
chosenword = random.choice(word_list)
print(f"psst the solution is {chosenword}")
#step2
display=[]
for letter in range(len(chosenword)):
    display+="_"
print(display)  

lives = 6

end_of_the_game=False
while not end_of_the_game:
    guess= input("guess a letter to save life\n").lower()
    for position in range(len(chosenword)):
        letter = chosenword[position]
        if letter== guess:
            display[position] = letter
    print(display)  

    if guess not in chosenword:
        lives-= 1
        if lives == 0:
            end_of_the_game = True
            print("you lose!")

    if "_" not in display:
        end_of_the_game=True
        print("you win !")  







