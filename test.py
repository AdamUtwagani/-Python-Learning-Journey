# firstname + surname)
# age=input("what is your age?")
# position=input("what is your position in your company?")
# maritalstatus=input("what is your marital status?")
# irstname=input("what is your first name? ")
# surname=input("what is your surname? ")
# print(fshortdetail=print(firstname  + surname +  age  + position  + maritalstatus),

# print("karibu katika mashindano ya Iq ya taifa")
# prob1=input("Rais wa kwanza wa marekani anaitwa nani ?").lower()
# if prob1== "adam":
#     prob2= input("Mkoa upi una watu wengi zaidi nchini tanzania ?").lower()
#     if prob2== "dar":
#         prob3= input("mji upi unaongoza kuwa na wamasai wengi nchini tanzania ?").lower()
#         if prob3== "arusha":
#             print("wewe ni noma umeshinda")
#         else:
#             print("Wakati mwingine umeaga mashindano")
#     else:
#         print("Wakati mwingine umeaga mashindano")        
# else:
#     print("Wakati mwingine umeaga mashindano")                

#huduma za vifurushi

# def salamu():
#     print("Habari karibu YOS huduma kwa wateja")
#     languagepreference=str(input("kuendelea kwa kiswahili bonyeza '1',bonyeza '2' kwa kiingereza"))
#     if languagepreference== "1":
#         print(kiswahili)
#     elif languagepreference== "2":
#         print(english)
#     else:
#         print("invalid response chaguo si sahihi")    
#     if kiswahili== "A":
#         print(huduma)  
#     elif kiswahili == "C":
#         print(piga)  
#     else:
#         print("chaguo lako si sahihi")  
#     if english== "B":
#         print(services)
#     elif english== "C":
#         print(call)
#     else:
#         print("invalid response ")   

# kiswahili= input("kwa vifurushi na huduma zetu bonyeza 'A', au bonyeza 'C' kuongea na mtoa huduma wetu ") 
# english= input("for our packages and services press 'A', or press 'C' for direct call to customer care team")
# huduma= ["huduma za SMM", "huduma za ICT"]
# services= ["SMM services", "ICT services"]
# piga= ["subiri kuunganishwa na muhudumu wetu"]
# call=["wait while we are connecting you to our customer care"]
 
# salamu() # its wrong 

#BlackJack Project The Casino Game
# import random 

# def judgement():
#     print("Hello and Welcome to Black jack Game")
#     cards=["11","1","2","3","4","5","6","7","8","9","10","10","10","10"]
#     usercards= random.choice(cards)
#     computercards= random.choice(cards)
#     usercards=int(usercards)
#     usercards2=int(usercards2)
#     print(f"Your first card is {usercards}")
#     print(f"Computer first card is {computercards}")
#     roundtwo= input("Do you want to continue with round two ? write 'y' for yes and 'n' for no\n").lower()
#     if roundtwo=="y":
#            roundtwofunction
#     elif roundtwo=="n" and usercards>computercards:
#              print("Hurray! You won.") 
           
           
                  

# def roundtwofunction():  
#     cards=["11","1","2","3","4","5","6","7","8","9","10","10","10","10"]         
#     usercards2= random.choice(cards)
#     computercards2= random.choice(cards)
#     usercards=int(usercards)
#     usercards2=int(usercards2)
#     totalusercards=(usercards+usercards2)
#     computercards=int(computercards)
#     computercards2=int(computercards2)
#     totalcomputercards=(computercards+computercards2)
#     print(f"Your Cards are {usercards} and {usercards2}")



#     if totalusercards>21:
#             print(f"Your total is {totalusercards}")
#             print("Bust !!! You lost. You exceeded 21")
#     elif totalusercards<totalcomputercards and totalcomputercards<=21:
#             print("Bad Luck! You Lost. Computer is near 21 than you") 
#     elif totalusercards<21 and totalcomputercards>21:
#             print("Hurray! You won.") 
#     elif totalusercards==totalcomputercards:
#             print("Its Draw !") 


# judgement()             
   

# BlackJack Project: The Casino Game
# import random

# def judgement():
#     print("Hello and Welcome to Black jack Game")
#     cards = ["11", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "10", "10", "10"]

#     usercards = int(random.choice(cards))
#     computercards = int(random.choice(cards))

#     print(f"Your first card is {usercards}")
#     print(f"Computer's first card is {computercards}")

#     roundtwo = input("Do you want to continue with round two? Write 'y' for yes and 'n' for no:\n").lower()
#     if roundtwo == "y":
#         roundtwofunction(usercards, computercards)
#     elif roundtwo == "n":
#         if usercards > computercards:
#             print("Hurray! You won.")
#         elif usercards < computercards:
#             print("Sorry! You lost.")
#         else:
#             print("It's a draw!")

# def roundtwofunction(usercards, computercards):
#     cards = ["11", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "10", "10", "10"]

#     usercards2 = int(random.choice(cards))
#     computercards2 = int(random.choice(cards))

#     totalusercards = usercards + usercards2
#     totalcomputercards = computercards + computercards2

#     print(f"Your cards are {usercards} and {usercards2}. Total = {totalusercards}")
#     print(f"Computer cards are {computercards} and {computercards2}. Total = {totalcomputercards}")

#     if totalusercards > 21:
#         print("Bust!!! You lost. You exceeded 21.")
#     elif totalcomputercards > 21:
#         print("Hurray! You won. Computer busted.")
#     elif totalusercards > totalcomputercards:
#         print("Hurray! You won.")
#     elif totalusercards < totalcomputercards:
#         print("Bad luck! You lost. Computer is closer to 21.")
#     else:
#         print("It's a draw!")

# # Start the game
# judgement()



# Coffee Machine Program

# Initial resources
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
#     "money": 0.0
# }

# # Menu with ingredients and cost
# menu = {
#     "espresso": {
#         "ingredients": {"water": 50, "coffee": 18},
#         "cost": 1.5
#     },
#     "latte": {
#         "ingredients": {"water": 200, "milk": 150, "coffee": 24},
#         "cost": 2.5
#     },
#     "cappuccino": {
#         "ingredients": {"water": 250, "milk": 100, "coffee": 24},
#         "cost": 3.0
#     }
# }

# # Coin values
# coin_values = {
#     "quarters": 0.25,
#     "dimes": 0.10,
#     "nickels": 0.05,
#     "pennies": 0.01
# }

# def print_report():
#     print(f"Water: {resources['water']}ml")
#     print(f"Milk: {resources['milk']}ml")
#     print(f"Coffee: {resources['coffee']}g")
#     print(f"Money: ${resources['money']:.2f}")

# def is_resource_sufficient(drink):
#     for item in menu[drink]["ingredients"]:
#         if resources[item] < menu[drink]["ingredients"][item]:
#             print(f"Sorry there is not enough {item}.")
#             return False
#     return True

# def process_coins():
#     print("Please insert coins.")
#     total = 0
#     for coin in coin_values:
#         count = int(input(f"How many {coin}? "))
#         total += count * coin_values[coin]
#     return total

# def is_transaction_successful(payment, cost):
#     if payment < cost:
#         print("Sorry that's not enough money. Money refunded.")
#         return False
#     elif payment > cost:
#         change = round(payment - cost, 2)
#         print(f"Here is ${change} in change.")
#     resources["money"] += cost
#     return True

# def make_coffee(drink):
#     for item in menu[drink]["ingredients"]:
#         resources[item] -= menu[drink]["ingredients"][item]
#     print(f"Here is your {drink}. Enjoy!")

# # Main loop
# machine_on = True

# while machine_on:
#     choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

#     if choice == "off":
#         machine_on = False
#     elif choice == "report":
#         print_report()
#     elif choice in menu:
#         if is_resource_sufficient(choice):
#             payment = process_coins()
#             if is_transaction_successful(payment, menu[choice]["cost"]):
#                 make_coffee(choice)
#     else:
#         print("Invalid input. Please choose from espresso, latte, cappuccino.")



# Mahitaji ya Programu ya "Mashine ya Vinywaji Baridi"
# 1. Muulize mtumiaji:
# Andika ujumbe ufuatao kila mara:
# "Ungependa kinywaji gani? (cocacola/pepsi/fanta):"

# a. Angalia jibu la mtumiaji ili kuamua hatua inayofuata.

# b. Prompt hiyo irudi kila baada ya hatua kukamilika (mfano: baada ya kunywa kutolewa), tayari kumhudumia mteja mwingine.

# 2. Zima mashine:
# a. Weka neno siri la kuzima mashine:

# "off"

# b. Ikiingizwa, programu isitishe kabisa.

# 3. Toa ripoti ya rasilimali:
# Ikiingizwa neno "ripoti" kwenye prompt, onyesha ripoti ya rasilimali zilizopo:

# text
# Copy
# Edit
# Maji: 1000ml  
# Barafu: 500g  
# Soda: 3L  
# Pesa: TSh 5,000
# 4. Angalia kama rasilimali zinatosha:
# Kabla ya kutengeneza kinywaji, hakikisha kuna rasilimali za kutosha.

# Mfano: Pepsi inahitaji 300ml ya maji, kama kuna 200ml tu basi ujumbe:

# "Samahani, hakuna maji ya kutosha."

# Hii ifanyike pia kwa barafu au soda.

# 5. Shughulikia sarafu:
# Ikiwa rasilimali zinatosha, mteja atatakiwa kuingiza sarafu.

# Viwango vya sarafu:

# Shilingi 500

# Shilingi 200

# Shilingi 100

# Shilingi 50

# Mfano: 2x 500 + 1x 100 = 1,100 TSh

# 6. Angalia kama malipo yanatosha:
# Ikiwa pesa hazitoshi:

# "Samahani, pesa haitoshi. Pesa yako imerejeshwa."

# Ikiwa pesa zinatosha:

# Ongeza kwenye salio la mashine.

# Toa chenji kama ilizidisha:

# "Hii hapa TSh 300 kama chenji yako."

# Toa chenji iliyopangwa hadi desimali 2.

# 7. Tengeneza Kinywaji:
# Ukaguzi wa rasilimali na malipo ukikamilika:

# Punguza kiwango cha maji, soda, barafu kulingana na aina ya kinywaji.

# Ongeza kiasi cha pesa kulingana na bei ya kinywaji.

# Toa ujumbe:

# "Hii hapa ${kinywaji chako}. Furahia!"

# Orodha ya Vinywaji na Maelezo Yake:
# 🥤 Cocacola
# Gharama: TSh 1,500

# Rasilimali Inayohitajika:

# Maji: 300ml

# Soda: 500ml

# Barafu: 100g

# 🥤 Pepsi
# Gharama: TSh 1,300

# Rasilimali Inayohitajika:

# Maji: 250ml

# Soda: 450ml

# Barafu: 80g

# 🥤 Fanta
# Gharama: TSh 1,200

# Rasilimali Inayohitajika:

# Maji: 200ml

# Soda: 400ml

# Barafu: 70g

# import turtle
# import math

# # Setup screen and turtle
# screen = turtle.Screen()
# screen.bgcolor("white")
# pen = turtle.Turtle()
# pen.speed(0)  # Fastest drawing

# # List of (name, sides, color)
# polygons = [
#     ("Triangle", 3, "red"),
#     ("Square", 4, "blue"),
#     ("Pentagon", 5, "green"),
#     ("Hexagon", 6, "purple"),
#     ("Heptagon", 7, "orange"),
#     ("Octagon", 8, "brown"),
#     ("Nonagon", 9, "cyan"),
#     ("Decagon", 10, "magenta")
# ]

# # Function to draw a polygon from the same center
# def draw_polygon(sides, length):
#     angle = 360 / sides
#     for _ in range(sides):
#         pen.forward(length)
#         pen.left(angle)

# # Draw each polygon from same center, rotating before each for clarity
# start_length = 100  # You can adjust this size
# angle_offset = 15   # To separate them visually

# for name, sides, color in polygons:
#     pen.penup()
#     pen.goto(0, 0)
#     pen.setheading(0)  # Reset angle
#     pen.left(angle_offset * polygons.index((name, sides, color)))  # Offset for visibility
#     pen.pendown()
#     pen.color(color)
#     draw_polygon(sides, start_length)

# pen.hideturtle()
# screen.mainloop()

def maxCardCount(n, card):
    return dp(0, n, card, 0)  # Start from index 0 and sum 0

def dp(i, n, card, current_sum):
    if i == n:
        return 0
    elif current_sum + card[i] >= i:
        # Option 1: pick this card
        pick = 1 + dp(i + 1, n, card, current_sum + card[i])
        # Option 2: skip this card
        skip = dp(i + 1, n, card, current_sum)
        return max(pick, skip)
    else:
        return dp(i + 1, n, card, current_sum)

# Read input values
n = int(input("Enter number of cards: "))
cards = list(map(int, input("Enter card values: ").split()))

# Validate input
if len(cards) != n:
    print("Error: number of card values does not match n.")
else:
    # Find and print result
    result = maxCardCount(n, cards)
    print("Maximum cards that can be picked:", result)












