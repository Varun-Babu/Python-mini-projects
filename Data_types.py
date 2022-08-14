#BAND NAME GENERATOR

print("Welcome to band name generator")
name = input("Enter the name of your city").capitalize()
animal = input("Enter the name of an animal").capitalize()
print(f'Your Band Name is  {name + " " + animal}')

#TIP CALCULATOR

print("Welcome to tip calculator")
total_bill = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give? 10,12 or 15?"))
split = int(input("How many people to split the bill?"))

tip = total_bill * (tip_percent/100)
bill_plus_tip = total_bill + tip
bill_split = bill_plus_tip / split

print(f"Each person should pay: {bill_split}")


