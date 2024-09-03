print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# todo: work out how much they need to pay based on their size choice.

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You have chosen an invalid size.")

# todo: work out how much to add to their bill based on their pepperoni choice.
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# todo: work out their final amount based on whether if they want extra cheese.
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")



#..............OR.............

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill=0
if size=="S":
    if pepperoni=="Y":
        bill+=17
        print(f"Here is your bill for Small/Pepp Pizza ${bill}")
    if pepperoni=="N":
        bill+=15
        print(f"Here is your bill for Small Pizza ${bill}")
elif size=="M":
    if pepperoni=="Y":
        bill+=23
        print(f"Here is your bill for Medium/Pepp Pizza ${bill}")
    if pepperoni=="N":
        bill+=20
        print(f"Here is your bill for Medium Pizza ${bill}")

elif size=="L":
    if pepperoni=="Y":
        bill+=28
        print(f"Here is your bill for Large/Pepp Pizza ${bill}")
    if pepperoni=="N":
        bill+=25
        print(f"Here is your bill for Large Pizza ${bill}")
if extra_cheese=="Y":
    bill+=1
    print(f"Here is your final bill with extra cheese ${bill}")
else:
    print(f"Here is your final bill without extra cheese ${bill}")

