import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# 1st Option
print(random.choice(friends))

# 2nd Option
random_index = random.randint(0, 4)
print(friends[random_index])

#3rd Code Style:
indexes=random.randint(0,4)
if indexes==0:
    print(friends[0])
elif indexes==1:
    print(friends[1])
elif indexes==2:
    print(friends[2])
elif indexes==3:
    print(friends[3])
else:
    print(friends[4])
print(random.choice(friends))
