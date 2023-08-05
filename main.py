# Introduction
print("Welcome to the tip calculator.")
# Get total bill input
total_bill = float(input("What is the total bill?\n"))
# Get percentage of tip 
percentage_of_tip = int(input("What percentage of tip? 10, 12, or 15\n"))
# Get amount of people paying
people = int(input("How many people to split the bill?\n"))
# Get amount of tip and round to 2 decimals
amount_of_tip = round((percentage_of_tip / 100) * total_bill, 2)
# Work out new amount to pay
amount_with_tip = total_bill + amount_of_tip
# Split bill amongst amount of people
each_to_pay = round(amount_with_tip / people, 2)
print(f"For the amount of people paying, each person should pay: \n £{each_to_pay}")
