fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")

print(fruits)

#.................or...................

fruits = ["Apple", "Peach", "Pear"]
fruits[2]="banana"
fruits.append("strawberry")
for fruit in fruits:
    print(f"{fruit} & {fruit}+ pie")
    #print(fruit + " pie")
