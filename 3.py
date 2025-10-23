#rollercoaster ticket system
# print(" welcome to the rollercoaster park !")
# height= int(input("what is your height in cm ?"))
# bill = 0

# if height >= 120:
#     print("you can ride the rollercoaster!")
#     age= int(input("what is your age ?"))
#     if age<12:
#         print("child tickets are $5.") 
#         bill = 5     
#     elif age<=18:
#         print("youth tickets are $7")
#         bill = 7
#     elif age>=45 and age<=55:
#         print("Dont worry we got you covered, have free ride")    
#     else:
#         print("youth tickets are $12 ") 
#         bill = 12
#     wants_photos=input("do you wants photos answer Y for yes and N for no ?")    
#     if wants_photos== "Y":
#         bill = bill + 3
#         print(f" Your total bill is ${bill} ")
# else:
#     print(" sorry you are too short to ride the rollercoaster ?")


# number= int(input("which number do you want to check ?"))
# if number % 2 == 0:
#     print("this is an even number")   
# else:
#     print("this is an odd number")  



# year= int(input("which year do you want to check ?"))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("leap year")
#         else:
#             print("not a leap year")
#     else:
#         print("leap year")
# else:
#     print("not a leap year")  



#pizza ordering system 
# print(" Hello Welcome to our Online pizza deliveries ")
# pizzasize= input(" Which size of the pizza do you want ? S,M or L ?")
# peperon= input(" do you want peperon? Y for yes and N for no")
# extracheese= input(" do you want an extra cheese ? Y for yes and N for no ")

# bill = 0
# if pizzasize== "S":
#     bill+=15
# if pizzasize== "M":
#     bill+=20
# if pizzasize== "L":
#     bill+=25

# if peperon== "Y":
#     if pizzasize== "S":
#         bill+=2
#     else:
#         bill+= 3

# if extracheese=="Y":
#     bill+=1         

# print(f"your total bill is ${bill}")



#love calculator 
# print("Hello wwelcome to the love calculator ")
# name1=input("write your name ?")
# name2=input("what is their name?")
# combined_string= name1 + name2
# lowered_case= combined_string.lower()

# t=lowered_case.count("t")
# r=lowered_case.count("r")
# u=lowered_case.count("u")
# e=lowered_case.count("e")
# true= t + r + u + e

# l=lowered_case.count("l")
# o=lowered_case.count("o")
# v=lowered_case.count("v")
# e=lowered_case.count("e")
# love= l + o + v + e 

# lovescore= int(str(true) + str(love))
# print(lovescore)

# if (lovescore < 10) or (lovescore > 90):
#     print(f"your love score is {lovescore}, you are perfect combo ")
# elif (lovescore >= 40) and (lovescore <= 50):
#     print(f" your love score is {lovescore} you alright together")
# else:
#     print(f"your love score is {lovescore}")



#treasure island game
# print(" Heeey welcome to the treasure island")
# prob1= input ("you are in junction of two ways , are you going right or left").lower()
# if prob1=="right":
#     print("you made a right choice")
# else:
#     print("game over")
# prob2= input("you are at the lake, do you swim or wait").lower()
# if prob2== "wait":
#     print(" you made a great choice ") 
# else:
#     print("game over")  
# prob3= input("you are infront of three doors choose one to enter Red, Blue or Green ?")
# if prob3== "red":
#     print("congratulations you won! you found the treasure")
# else:
#     print("game over") 


print("welcome to the treasure island  ")
print("you are required to find the hidden treasure")
choice1=input("you are at the junction choose 'left' or 'right' ").lower()
if choice1== 'right':
    choice2=input("you are at the lake 'wait' or 'swim'").lower()
    if choice2== 'wait':
        choice3= input("you are infront of three doors choose 'red', 'green' or 'blue' ").lower()
        if choice3== 'red':
            print("you found the treasure congratulations")
        elif choice3== 'green':
            print("game over you are into zombies room")
        elif choice3== 'blue':
            print("gaame over you are into blackhole room")
        else:
            print("you choose wrong option game over")       
    else:
        print("game over you have eaten by crocodiles")
else:
    print("game over you are into hell")                    










