foods = {}

for i in range(1, 5):
    foods[i] = input("Enter the food you like: ").lower()

remove_food = int(input(f"Which one would you like to remove [1-5]: {foods}\n~ "))
del foods[remove_food]
#foods = dict(sorted(foods.items(), key=lambda item: item[1]))
sorted = sorted(foods.values())
#print(foods)
print(sorted)
