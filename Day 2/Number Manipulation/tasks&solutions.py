#BMI Calculator

height = 1.65 
weight = 84

# Calculate the bmi using weight and height.
bmi = weight/(height**2)

print(bmi)

bmi = 84 / 1.65 ** 2

# Original Float with decimal places
print(bmi)

# Flooring the number by converting it into int
print(int(bmi))

# Rounding the number into a whole number
print(round(bmi))

# Rounding only to 2 decimal places
print(round(bmi, 2))


## Accumulate
score = 0

# User scores a point
score += 1
print(score)

#Also
score -= 1
score *= 2
score /= 2

# f string use case

score = 0
height = 1.8
is_winning = True

print(f"Your score is = {score}, your height is {height}. You are winning is {is_winning}")


