print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
else:
    print("Sorry you have to grow taller before you can ride.")

#......or......
# Define Boolean variables based on conditions
can_ride = height >= 150
close_enough = height == 149
not_close_enough = height != 149

# Use Boolean variables in if/else statements
if can_ride is True:
    print('You can ride')
elif close_enough is True:
    print('Close enough! Go enjoy your ride')
else:
    print("You can't ride")
