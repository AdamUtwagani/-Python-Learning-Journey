#functions with Outputs

# def format_name(fname, lname):
#     if fname== "" or lname=="":
#         return "You didnt prvide your names"
#     formated_fname= fname.title()
#     formated_lname= lname.title()
#     return f"{formated_fname} {formated_lname}"
#     # print(f"{fname} {lname}")

# formatedstring=format_name(input("what is your first name?"), input("what is your last name ?"))
# print(formatedstring)


# Function to check leap year
# def leapyear(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False

# # Function to get days in a month
# def days_in_months(year, month):
#     #docstrings example 
#     """total days in a certain month depends if the year is leap or not"""
#     months_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if leapyear(year) and month == 2:
#         return 29
#     return months_days[month - 1]

# # Main program
# year = int(input("Enter a year: "))
# month = int(input("Enter a month (1-12): "))
# days = days_in_months(year, month)
# print(f"{days} days in month {month} of year {year}")

#Calculator App 

#addition 
def add(n1, n2):
    return n1 + n2 

#substraction 
def sub(n1, n2):
    return n1 - n2

#multiplication 
def multi(n1, n2):
    return n1 * n2

#division 
def div(n1, n2):
    return n1/n2

operations={
    "+": add,
    "-": sub,
    "/": div,
    "*": multi,
}

def calculator():
    n1= float(input("what is the first number: "))

    for sign in operations:
            print(sign)

    shouldcontinue= True

    while shouldcontinue:
            operationsign= input("pick up the operation you want from the shown list above")
            n2= float(input("what is the next number: "))
            calculation_functoion=operations[operationsign]
            answer= calculation_functoion(n1, n2)

            print(f"{n1} {sign} {n2} = {answer}")
    if  input(f" type 'y' to continue operation with {answer} or type 'n' to start a fresh \n ")=="y":
            n1= answer 
    else:
          shouldcontinue= False
          calculator()

calculator()                 
         

# for sign in operations:
#     print(sign)
# operationsign= input("choose another operation above")
# n3= int(input("what is the another number: "))
# calculation_functoion=operations[operationsign]
# answer2= calculation_functoion(answer, n3)
# print(answer2)




