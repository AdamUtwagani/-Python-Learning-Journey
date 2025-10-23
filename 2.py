# two_digit_number= input("Enter two digits number")
# first_digit= two_digit_number[0]
# second_digit =two_digit_number[1]
# print(first_digit)
# print(second_digit)
# result= int(first_digit) + int(second_digit)
# print("the total sum of two digits is " + str(result))

# height=input("what is your height in m ?")
# weight=input("what is your weight in kg ?")
# result=(int(weight)/ int(height))
# print("Your IBM is equal to " + str(result))
# if result==30:
#     print("you are at normal IBM congratulations  ")
# elif result>45:
#     print(" stop eating chips and burgers you are obese")    
# else:
#     print("love yorself eat well you are underweight")


# print(round(8/3,2))

# f-String
# score = 14
# height =1.9
# winning = True
# print(f"your score is {score}, your height is {height} and your winning is {winning}")

# print("welcome to the death calculator app")
# age =  input("what is your current age ?")
# age_numb= int(age)
# years_remaining = 90-age_numb
# months_remaining= years_remaining * 12
# weeks_remaining= years_remaining * 52
# days_remaining= years_remaining * 365
# print(f"You are remained with total of {years_remaining} years, {months_remaining} months, {weeks_remaining} weeks, and {days_remaining} days, Make every day count we only live once.")

print("Welcome to the tip calculator")
total=input("what was the total bill ?")
totally= float(total)
percentage=input("what percentage tip would you like to give 10%, %15 and  20% ?")
perce= float(percentage)
perc= perce / 100 
total_and_tip= totally + perc
people=input("how many people to split the bill")
ppl= int(people)
result= total_and_tip / ppl
print(f"each person should pay: {result}")


