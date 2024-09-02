# Subscripting
print("Hello"[0])

#1. Using Slicing
#If you want to print a range of indices, you can use slicing. For example, if you want to print indices 0 to 3:
x = input("What is your age?\n")
print("Hello", x[0:3])  # This will print characters from index 0 to 2

#2. Using Individual Indexing
#If you want to print specific, non-consecutive indices, you can access each index individually. For example, if you want to print indices 0, 2, and 4:
x = input("What is your age?\n")
print("Hello", x[0], x[2], x[4])

#3. Using a Loop
#If you have a list of indices and you want to print the characters at those indices, you can use a loop:
x = input("What is your age?\n")
indices = [0, 2, 4]  # List of specific indices
print("Hello", end=" ")
for i in indices:
    if i < len(x):  # Ensure the index is within the range of the string
        print(x[i], end=" ")
print()  # For a new line after the output

#4. Using List Comprehension
#If you prefer a more compact solution and the indices are stored in a list, you can use list comprehension and join to print them:
x = input("What is your age?\n")
indices = [0, 2, 4]  # List of specific indices
print("Hello", ''.join(x[i] for i in indices if i < len(x)))

# String
print("123" + "345")

# Integer = Whole number
print(123 + 345)

# Large Integers
print(123_456_789)

# Float = Floating Point Number
print(3.14159)

# Boolean
print(True)
print(False)
