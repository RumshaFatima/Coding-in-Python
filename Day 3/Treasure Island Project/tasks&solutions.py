print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a crossroad, where do you want to go? '
                'Type "left" or "right".\n').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a lake. '
                    'There is an island in the middle of the lake. '
                    'Type "wait" to wait for a boat. '
                    'Type "swim" to swim across.\n').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. "
                        "There is house with 3 doors. One red, "
                        "one yellow and one blue. "
                        "Which colour do you choose?\n").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over")
        elif choice3 == "yellow":
            print("You found the treasure. You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")

else:
    print("You fell in to a hole. Game Over.")


#.................or...............................

print("Welcome to treasure island!")
print(menu:=input("Type S to start the game. M for menu and E for exiting the game terminal.\n").upper())
if menu=="S":
    print(choice1:=input("There are two narrow alleys. Type L to go to left alley or R to go to right alley.\n").upper())
    if choice1=="L":
        print(choice2:=input("On left alley you see three signs: Earth, Fire & Water. Choose one color from 'red' for Fire, 'yellow' for Earth or 'blue' for Water.\n").lower())
        if choice2=="red":
            print("If you found the treasure you can use fire to mould it. Lets see if this fire sign will be useful for you or not")
        elif choice2=="yellow":
            print("If you found the treasure you can use Earth to recreate it into a new morph. Lets see if this earth sign will be useful for you or not")
        elif choice2 == "blue":
            print("If you found the treasure you can use Water to multiply the treasure by dispersing it. Lets see if this water sign will be useful for you or not")
        print(choice3:=input("Choose one treasure option from T1, T2 or T3.\n").upper())
        if choice3=="T1":
            print(f"Oops! You have found a snake hole. Now use the power of  {choice2} to multiply your snakes. ")
        elif choice3=="T2":
            print(f"Oops! You have found a rabbit hole. Now use the power of {choice2} to multiply your rabit. ")
        else:
            print(f"Hurray! You have found a treasure core of diamonds. Now use the power of  {choice2} to multiply your diamonds. ")
    else:
        print("Oops! You fell into the black hole in space. Game is Over!")

elif menu=="M":
    print("Here are the rules for the game:\n 1. You can only make a choice once. You can't change your choices later.\n 2. If you exit you can't continue from where you left.")
else:
    print("See you again.")

................or.....................

def start_game():
    print("There are two narrow alleys. Type L to go to the left alley or R to go to the right alley.")
    choice1 = input().upper()
    
    if choice1 == "L":
        print("On the left alley you see three signs: Earth, Fire & Water. Choose one color from 'red' for Fire, 'yellow' for Earth or 'blue' for Water.")
        choice2 = input().lower()
        
        if choice2 == "red":
            print("If you found the treasure you can use fire to mold it. Let's see if this fire sign will be useful for you or not.")
        elif choice2 == "yellow":
            print("If you found the treasure you can use Earth to recreate it into a new form. Let's see if this Earth sign will be useful for you or not.")
        elif choice2 == "blue":
            print("If you found the treasure you can use Water to multiply the treasure by dispersing it. Let's see if this Water sign will be useful for you or not.")
        else:
            print("Invalid choice. Let's start over.")
            return
        
        print("Choose one treasure option from T1, T2 or T3.")
        choice3 = input().upper()
        
        if choice3 == "T1":
            print(f"Oops! You have found a snake hole. Now use the power of {choice2} to handle your snakes.")
        elif choice3 == "T2":
            print(f"Oops! You have found a rabbit hole. Now use the power of {choice2} to handle your rabbits.")
        elif choice3 == "T3":
            print(f"Hurray! You have found a treasure core of diamonds. Now use the power of {choice2} to handle your diamonds.")
        else:
            print("Invalid choice. Let's start over.")
            return
        
    else:
        print("Oops! You fell into the black hole in space. Game is Over!")

def show_menu():
    print("Here are the rules for the game:")
    print("1. You can only make a choice once. You can't change your choices later.")
    print("2. If you exit, you can't continue from where you left.")
    
def main():
    print("Welcome to Treasure Island!")
    
    while True:
        menu = input("Type S to start the game, M for menu, or E to exit the game terminal.\n").upper()
        
        if menu == "S":
            start_game()
        elif menu == "M":
            show_menu()
        elif menu == "E":
            exit_game = input("Are you sure you want to exit the game? Y or N ").upper()
            if exit_game == "Y":
                print("We hope you enjoyed the game. See you next time.")
                break
            elif exit_game == "N":
                continue
            else:
                print("Invalid input. Please type Y or N.")
        else:
            print("Invalid choice. Please type S to start, M for menu, or E to exit.")
            
if __name__ == "__main__":
    main()

