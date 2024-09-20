# This is my official submission for day 2 of the 100 days of python boot camp, we are totally on a roll!

# Provided code from the project files 
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

# calculating the tip percentage
tip_percentage = 1 + (tip / 100)

# calculating the amount all members should pay (bill cost divided by the amount of people multiplied by 1 added to the tip_percentage_decimal_value
# and then round the amount to 2 decimal places
amount = round((bill / people) * tip_percentage, 2)

# printing the final out put by use of F strings
print(f"Each Person Should Pay ${amount}")