# TypeError
# len(123)

# No TypeError
len("Hello")

# Type Checking

print(str(type("Hello")) + str(type(123)) + str(type(123.44)) + "and" + str(type(False)))

 #...or...

print(type("Hello"))
print(type(123))
print(type(123.44))
print(type(False))

# Type Conversion
str()
int()
float()
bool()

name_of_the_user = input("Enter your name")
length_of_name = len(name_of_the_user)

print(type("Number of letters in your name: "))  # str
print(type(length_of_name))  # int

print("Number of letters in your name: " + str(length_of_name))

#......or.....

print("Number of letters in your name: " + str(len(input("Enter your name"))))
