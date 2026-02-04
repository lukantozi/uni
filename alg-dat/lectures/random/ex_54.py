import random

coin = random.choice(["h", "t"])
h_t = ["heads", "tails", "head", "tail", "h", "t"]

while True:
    user_choice = input("Heads or Tails?\n~ ").lower()
    if user_choice in h_t:
        break
    print('Please choose from the following options: "heads", "tails", "head", "tail", "h", "t"')

if coin in user_choice:
    print("You win")
else:
    print("Bad luck")

