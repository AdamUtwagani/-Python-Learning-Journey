# import random
# cc= random.randint(50, 100)
# print(f"your cc score is {cc}")

#heads or tails 
# h="Heads"
# t="Tails"
# A= random.randint(1,2)
# if A==1:
#     print(h)
# elif A==2:
#     print(t)

# cars=["mazda","toyota", "suzuki", "lamboghini"]
# print(cars[1])
# cars[3]="lamborghini"
# cars.append("Ferrari")
# print(cars)

# import random
# string_names= input("Give me your names and i will choose randomly our today's boss")
# names=string_names.split(",")
# numb_ppl=len(names)
# randomly=random.randint(0, numb_ppl-1)
# boss= names[randomly]
# print(f"Our today's boss is {boss}")

# musicians= ["Harmonize", "alikiba", "Diamond","zuchu" ]
# comedians= ["Leornado", "txdullah", "ndaro", "jolmaster"]
# entertainers= [musicians, comedians]
# print(entertainers)

import random
print("welcome to the Rock paper and scissor game")
userchoice=int(input("type 0 for rock, 1 for paper and 2 for scissor"))
computerchoice= random.randint(0, 2)
print(f"your opponent chose {computerchoice}")
if userchoice>=3 or userchoice<0:
    print(" You selected unknown choice so you lost")
elif userchoice==0 and computerchoice==2:
    print("You won")
elif computerchoice== 0 and userchoice== 2:
    print("you lose!")
elif userchoice> computerchoice:
    print("you win")        
elif computerchoice > userchoice:
    print("you lost")
elif computerchoice== userchoice:
    print(" its a draw ")    




    



































