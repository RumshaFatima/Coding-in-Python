print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")


#Solution using while-true loop:

print("Welcome to the tip calculator!")
total_bill=float(input("What was the total bill?\n $"))
# Loop until a valid tip percentage is provided
while True:
    try:
        tip=int(input("How much tip would you like to give? 10, 12 or 15?\n $"))
        if tip in [10, 12, 15]:
            break
        else:
            print('Please choose a valid tip count from 10, 12 or 15')
    except ValueError:
        print('Invalid input. Please enter a number.')
people=int(input("How many people to split the bill?\n"))
print(tip_percentage:= total_bill+((total_bill*tip)/100))
Final_bill=round((total_bill+((total_bill*tip)/100))/people, 2)
print(f"Each person should pay:${Final_bill}")

