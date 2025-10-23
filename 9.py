#Pythondictionaries
#{key:value}
#{"Hello:"greeeting"}
#{"happy":"the feeling of excitement", "sad": "the feeling of depression "}

# feelingdictionary={
#     "Happy":"the feeling of excitement",
#     "sad":" the feeling of depression",
# }
# feelingdictionary["sick"]="the feeling of unwell"                                    

#uses of empty dictionary then add keys 
#emptydictionary{}
#emptydictionary["key"]="value"
#the above method can be used for Editing the item in the dictionary

#wiping the existing dictionary
#feelingdictionary={}

#looping through the dictionary
# for thing in feelingdictionary:
#     print(thing)
#     print(feelingdictionary [thing])

# studentscores= {
#     "john":80,
#     "asha":60,
#     "adam":90,
#     "zakia":50,
# }

# studentgrades= {}

# for student in studentscores:
#     score= studentscores[student]
#     if score > 70:
#         studentgrades[student]="Outstanding"
#     elif score < 70:
#         studentgrades[student]="Accepted"

# print(studentgrades)

#nesting in dictionaries

# countrycapitals={
#     "tanzania":"dodoma",
#     "kenya":"nairobi",
#     "uganda":"kampala",
# }

# travelog= {
#     "tanzania":["dodoma","Dar","arusha"],#list within a dictionary
#     "kenya":["nairobi","nakuru","meru"],
# }

# #nesting a dictionary in a dictionary
# plan= {
#     "southafrica": {"visited":["johanersburg","george","soweto"], "frequency":2},
#     "spain":{"visited":["barcelona","madrid"],"frequency":2},
# }

#nesting a dictionary inside a list
# nguo=[
# {
#     "machimbo":["kariakoo","buguruni","mbagala","tandika"],
#     "michosho":["mabibo","sinza","ubungo"],
# },
# {
#     "wakishua":["masaki","kigamboni","madale"],
#     "ngomanagwa":["mbagala","yombo","tandale","mburahati"],    
# }]

# travellog=[{
#     "country":"france",
#     "visits":12,
#     "cities": ["paris", "lille", "Lyon"]
# },
# {
#     "country": "germany",
#     "visits": 10,
#     "cities": ["munich","Berlin", "stuggart"]        
# }]

# def add_country (countryvisited, frequency, citiesvisited):
#     newcountry= {}
#     newcountry["country"] =countryvisited
#     newcountry["visits"]= frequency
#     newcountry["cities"]= citiesvisited
#     travellog.append(newcountry)

# add_country=("russia", 2, ["moscow","saint petesburg"])
# print(travellog)

#silent bid auction what i thought
# auctiondictionary= {
#     "bid":"bidamount",
#     "names":"name",  
# }
    
# print("Welcome to the silent Auction")
# name=input("what is your name ?\n").lower()
# bidamount= float(input("what is your bid in $ ?\n"))
# def auctiondictionary (name, bidamount):
#     newdictionary={}
#     newdictionary["bid"]= bidamount
#     newdictionary["names"]= name
#     auctiondictionary.append(newdictionary)

# continuestatus= input("is there any other bidder? type 'yes' or 'no'\n").lower()
# if continuestatus=="yes":
#     print("pass the ipad to the next bidder")
# elif continuestatus== "no":

#silent auction the solution 
# import os
# def clear():
#     os.system('cls' if os.name == 'nt' else 'clear')  # Windows -> 'cls', Linux/macOS -> 'clear'

# bids={}
# biddingfinish= False
# highestbid=0
# winner=""

# def findwinner(biddingrecord):
#     for bidder in biddingrecord:
#         bidamount= biddingrecord[bidder]
#         if bidamount > highestbid:
#             highestbid = bidamount
#             winner= bidder
#     print(f"The winner is {winner} with a bid of ${highestbid}") 

# while not biddingfinish:
#     name = input("what is your name ?:" )
#     price = int(input("what is your bid? $"))
#     bids[name]= price
#     continuestatus=input("are there any other bidder? type 'yes' or 'no' ")
#     if continuestatus=="no":
#         biddingfinish= True
#         findwinner(bids)    
#     elif continuestatus=="yes":
#         clear()


#chatgpt debugging        
import os

# Function to clear the screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')  # Windows -> 'cls', Linux/macOS -> 'clear'

# Dictionary to store bids
bids = {}
biddingfinish = False
highestbid = 0
winner = ""

# Function to find the highest bidder
def findwinner(biddingrecord):
    global highestbid, winner  # Use global variables
    for bidder in biddingrecord:
        bidamount = biddingrecord[bidder]
        if bidamount > highestbid:
            highestbid = bidamount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highestbid}") 

# Auction loop
while not biddingfinish:
    name = input("What is your name?: ")
    price = int(input("What is your bid? $"))
    bids[name] = price

    continuestatus = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    
    if continuestatus == "no":
        biddingfinish = True
        findwinner(bids)    
    elif continuestatus == "yes":
        clear()  # Clear the screen







