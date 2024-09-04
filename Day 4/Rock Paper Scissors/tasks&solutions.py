import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw!")
..........................................

#2nd Method:

#rock is 0, paper is 1, sci is 2
IndexA= [0,1,2]
randomA=random.choice(IndexA)
User1=int(input("What do you choose? Type 0 for paper, 1 for rock and 2 for scissors \n"))

if User1==0:
    print(f"Computer chooses: {randomA}")
    if randomA==0 and User1==0:
            print("It's a draw!")
    elif randomA==1 and User1==0:
            print("You loose! Paper wins!")
    elif randomA==2 and User1==0:
            print("You win! Scissors loose!")
elif User1==1:
    print(f"Computer chooses: {randomA}")
    if randomA==0 and User1==1:
        print("You win! Rock looses")
    elif randomA==1 and User1==1:
        print("It's a draw!")
    elif randomA==2 and User1==1:
        print("You loose! Scissors win!")
elif User1==2:
    print(f"Computer chooses: {randomA}")
    if randomA==0 and User1==2:
        print("You loose! Rock wins")
    elif randomA==1 and User1==2:
        print("You win! Paper looses!")
    elif randomA==2 and User1==2:
        print("It's a draw!")
else:
    print("You have given an invalid input")

..........................................

#3rd Method

import random

# Rock is 0, Paper is 1, Scissors is 2
IndexA = [0, 1, 2]

def get_user_choice():
    while True:
        try:
            User1 = int(input("What do you choose? Type 0 for rock, 1 for paper, and 2 for scissors \n"))
            if User1 in IndexA:
                return User1
            else:
                print("Invalid choice. Please type 0, 1, or 2.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a draw!"
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        return "You win!"
    else:
        return "You lose!"

def main():
    randomA = random.choice(IndexA)
    User1 = get_user_choice()
    
    print(f"Computer chooses: {randomA}")
    
    result = determine_winner(User1, randomA)
    print(result)

if __name__ == "__main__":
    main()

