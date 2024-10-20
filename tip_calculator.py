print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

final_payment = bill + (bill * (tip/100))

split = float(final_payment / people)
each_payment = round(split, 2)
print(f"Each person should pay: ${each_payment:.2f}")