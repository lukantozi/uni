tv_programmes = ["the office", "the modern fammily", "got", "mr robot"]
for p in tv_programmes:
    print(p)

show = input("\nEnter the show you want to add to the list: ")
while True:
    try:
        position = int(input("\nEnter the position you want the show to be added at: "))
        break
    except ValueError:
        print("\nPlease enter a number")

tv_programmes.insert(position, show)
print(tv_programmes)
