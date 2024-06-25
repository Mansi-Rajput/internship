###### Project 1 Band Name Generator #####
# print("Welcome to Band Name Generator")
# name = input("What's the name of the city you grew up in?\n")
# city = input("What's your pet name?\n")
# band_name = name +""+ city
# print(band_name)

##### Coding Exercise #####
# two_digit_number = input("Type a two digit number: ")
# first_digit = two_digit_number[0]
# second_digit = two_digit_number[1]
# result = int(first_digit) + int(second_digit)
# print(result)

##### Coding Exercise #####
# height = input("Enter your height in m: ")
# weight = input("Enter your weight in kl: ")

# bmi_calc = int(weight) / float(height) ** 2
# print(int(bmi_calc))

##### Coding Exercise ####
# current_age = int(input("what's your current age? "))
# years = 90 - current_age
# days = years * 365
# weeks = years * 52
# months = years * 12
# print(f"You have {days} days, {weeks} weeks, and {months} months left.")

##### Tip Calculator #####
#(bill/people) * percentage

print("Welcome to the Tip Calculator!")
bill = float(input("What was the total bill? $"))
tip_num = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
peolpe_splitting = int(input("How many people to split the bill? "))

tip_perc = tip_num / 100 * bill
print(tip_perc)
total_bill = bill + tip_perc
print(total_bill)
bill_divided = total_bill / peolpe_splitting
final_amount = round(bill_divided, 2)
print(f"Each person should pay: ${final_amount}")
