#Day 1 - Python Tasks Solutions 

#TASK 01: Printing in Python
#Task Description: Print out the words "Hello world!" with Python code.

print("Hello world!")

#TASK 02: String Manipulation in Python
#Task Description: String concatenation, word spacing and the new line escape sequence to format strings in Python.

print("Hello world!\nHello world\nHello world") #\n for line escape
print('Hello'+" "+'Rumsha') # + sign for string concatenation , " " for word spacing
print("Hello "+"Angela") # One space after the first word

#TASK 03: Inputs in Python
#Task Description: Use the Python input() function to collect user input and use it within your code

print('Hello '+ input('What is your name?')+'!') # one line code...... or.....

name= input("What is your name?")
print("Hello"+ " "+ name+"!")

#TASK 04 & 05: Variables or Containers in Python
#Task Description: Store values in containers & learn variable naming rules

# Learn the rules of variable naming in Python.

# Rules
# Make sure your variable names are descriptive
# Don't have spaces between words
# Don't start with numbers
# Don't use special words like print or input
# Choose simple words that are less likely to become typos
# Check the company style guidelines if you start work at a company

user_name = input("What is your name?")
new_name=user_name.replace(" ", "")
length_name=len(new_name)
print(length_name, new_name)

print(len((name := input("What is your name?")).replace(" ", "")), name.replace(" ", "")) # one line code which uses the walrus operator (:=) to both assign and use the name variable in the same line.

#TASK 06: Brand Name Generator Project 
# Task Description:
# -Create a greeting for your program.
# -Ask the user for the city that they grew up in and store it in a variable.
# -Ask the user for the name of a pet and store it in a variable.
# -Combine the name of their city and pet and show them their band name.


name=input("Hey there, what is your good name?\n")
City=input("Which city do you live in," + " " + name + "?\n")
Pet=input("What is the name of your pet?\n")
Brand_Name=print(City+" "+Pet+" is a good name for your future brand," +" "+ name)

#Using f-string method 

name=input("Hey there, what is your good name?\n")
City=input(f"Which city do you live in, {name}?\n")
Pet=input("What is the name of your pet?\n")
Brand_Name=print(f"{City} {Pet} is a good name for your future brand, {name}")

