# def greet ():
#     print("hello!")
#     print("how are you doing today?")
#     print("Tell me something am here to help")

# greet()  

#functions that allow inputs
# def greetname(name):
#     print(f"hello! {name}")
#     print(f"how are you doing today {name}?")
#     print(f"{name} Tell me something am here to help")
# greetname("adam")    

#functions with multiple inputs by positional arguments

# def greetwith(name, location):
#     print(f"hello {name}")
#     print(f"what is it like in {location}")
# greetwith("Adam","Arusha") 

#functions with keywords arguments
# def greetwith(name, location, condition):
#     print(f"hello {name}")
#     print(f"i know you are from {location}")
#     print(f"what is it like today sunny or rainy? {condition}")
# greetwith(location="arusha", name="John", condition="Rainy")

#wallPaintings cans calculator
# import math
# def paintcalculator(height, width, cover):
#     area= height*width
#     cans= math.ceil(area/cover)
#     print(f"you will need {cans} cans to paint whole wall")
    

# testh= int(input("height of the wall:"))
# testw= int(input("width of the wall:"))
# coverage=5

# paintcalculator(height=testh, width=testw, cover=coverage)

#prime number checker
# def primechecker(number):
#     isprime= True
#     for i in range(2, number):
#         if number % i == 0:
#             isprime= False
#     if isprime == True:
#         print("its prime number ")
#     else:
#         print("its not a prime number")            

# n= int(input("check this number:"))
# primechecker(number=n)


#Caesar Cipher 
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



#First approach but long
# def encrypt(text, shift):
#     ciphertext=""
#     for letter in text:
#         position = alphabet.index(letter)
#         newposition = position + shift
#         newletter= alphabet[newposition]
#         ciphertext+= newletter
#     print(f" the encoded text is {ciphertext}")



# def decrypt(ciphertext, shiftamount):
#     plaintext=""
#     for letter in ciphertext:
#         position = alphabet.index(letter)
#         newposition= position - shift
#         plaintext+= alphabet[newposition]
#     print(f"the decoded text is {plaintext}")

# if direction== "encode":
#     encrypt(text,shift)
# if direction== "decode":
#     decrypt(ciphertext=text, shiftamount=shift)    

#alternative and short way
shouldcontinue= True
while shouldcontinue:
    direction = input("type 'encode' to encrypt, type 'decode' tp decrypt\n")
    text= input("type your message\n").lower()
    shift = int(input("type the shift number;\n"))

    def caesar(starttext, shiftamount,cipherdirection):
        endtext=""
        if cipherdirection== "decode":
                shiftamount= shiftamount * -1
        for char in starttext:
            if char in alphabet:
                position = alphabet.index(char)
                newposition = position + shiftamount
                endtext+= alphabet[newposition]
            else:
             endtext+= char
                
        print(f"the {cipherdirection}d text is {endtext}")

    shift = shift % 26

    caesar(starttext=text, shiftamount=shift, cipherdirection=direction)
    response= input("type 'yes' if you want go again or type 'no' to quit\n").lower()
    print(response)
    if response=="no":
        shouldcontinue= False
        print("See you next time")
        









        












