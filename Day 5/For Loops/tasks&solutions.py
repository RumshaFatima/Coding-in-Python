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

#.........or............

fruits = [["Apple", "Peach", "Pear"],["Apple", "Peach", "Pear"]]
fruits[1][2]="banana"
fruits.append("strawberry")
for fruit in fruits:
    print(f"{fruit[0]} pie, {fruit[1]} pie, {fruit[2]} pie & {fruit}")
print(fruits)

#............or......................

fruits = [["Apple", "Peach", "Pear"],["Apple", "Peach", "Pear"]]
fruits[1][2]="banana"
fruits.append(["strawberry"])
for fruit_list in fruits:
    print(pie_fruit:=[f"{fruit} pie" for fruit in fruit_list ])
    print(", ".join(pie_fruit[:-1]) + " & " + pie_fruit[-1])
print(fruits)
