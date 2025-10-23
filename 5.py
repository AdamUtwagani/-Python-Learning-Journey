# fruits= ["apple", "mango", "pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")
#     print(fruits)

# studentheights= input("write the list of students heights").split(",")
# for n in range(0, len(studentheights)):
#     studentheights[n] = int(studentheights[n])
# print(studentheights)    

# totalheight= 0
# for height in studentheights:
#     totalheight+= height
# print(totalheight) 

# numberofstudents= 0
# for student in studentheights:
#     numberofstudents+=1
# print(numberofstudents)  

# averageheight= round(totalheight / numberofstudents)
# print(averageheight)

# student_scores= input("input a list of students scores").split(",")
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)
# highestscores= 0
# for score in student_scores:
#     if score > highestscores:
#         highestscores = score
# print(f" the highest score in the class is:{highestscores}")

# for number in range(0, 101, 2): #start, stop, step
#     print(number)

# total=0
# for number in range (1, 101):
#     total+= number
# print(total)

# even= 0
# for number in range (1, 101, 2):
#     even+= number 
# print(even)   

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("fizzbuzz") 
#     elif number % 3 == 0:
#         print("fizz")
#     elif number % 5 == 0:
#         print("buzz") 
#     else:
#         print(number)

#password generator 
# import random
# letters=("w,e,r,t,y,u,i,o,p,a,s,d,f,g,h,j,k,l,z,x,c,v,b,n,m").split(",")
# numbers= (("1,2,3,4,5,6,7,8,9,0")).split(",")
# symbols=("@,#,$,%,&").split(",")
# print("Welcome to the Pypassword generator1")
# lettersn=int(input("how many symbols would you like "))
# symbolsn=int(input("how many symbols would you like "))
# numbersn=int(input("how many numbers would you like "))

# passwoord=""
# for char in range(1, numbersn +1):
#     passwoord+= random.choice(numbers)

# for char in range(1, symbolsn +1):
#     passwoord+= random.choice(symbols) 

# for char in range(1, lettersn +1):
#     passwoord+= random.choice(letters)
#     random.shuffle(passwoord)
#     print(f"your password is {passwoord}")
# passwoord = ""
# for char in passwoord:
#     passwoord+= char
#     print(passwoord)

import random

# Define characters
letters = list("wertyuiopasdfghjklzxcvbnm")
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
symbols = ["@", "#", "$", "%", "&"]

print("Welcome to the PyPassword Generator!")

# Get user input
lettersn = int(input("How many letters would you like? "))
symbolsn = int(input("How many symbols would you like? "))
numbersn = int(input("How many numbers would you like? "))

# Generate password
passwoord = []
for _ in range(lettersn):
    passwoord.append(random.choice(letters))

for _ in range(symbolsn):
    passwoord.append(random.choice(symbols))

for _ in range(numbersn):
    passwoord.append(random.choice(numbers))

# Shuffle the password list and convert back to string
random.shuffle(passwoord)
password = "".join(passwoord)

# Display the generated password
print(f"Your password is: {password}")













 








  
















