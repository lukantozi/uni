import random

def main():
    color = random.choice(["green", "blue", "red", "orange", "purple"])

    while True:
        user_choice = input('Guess the color: "green", "blue", "red", "orange", "purple": ').lower()
        if user_choice == color:
            print("\nWell done")
            break
        else:
            match color:
                case "green":
                    print("\nI bet you are GREEN with envy\n")
                case "blue":
                    print("\nYou are probably feeling BLUE right now\n")
                case "red":
                    print("\nWhy did the tomato turn RED? Because it saw the salad dressing\n")
                case "orange":
                    print("\nORANGE you glad we're friends?\n")
                case "purple":
                    print("\nWhat color is a happy cat? Purrrr-ple!\n")


if "__main__" == __name__:
    main()
