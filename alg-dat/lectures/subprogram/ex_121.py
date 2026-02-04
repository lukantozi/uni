def add_name(lst):
    name = (input("Enter the name you wish to add to the list: "))
    lst.append(name.capitalize())


def change_name(lst):
    flag = False
    while flag == False:
        print(lst)
        name = (input("Enter the name you wish to modify [enter q to exit]: ")).capitalize()
        if name in lst:
            new_name = input("Enter a modified name: ")
            lst[(lst.index(name))] = new_name 
            flag = True
        elif name == "Q":
            flag = True
            continue
        else:
            print("No match. Enter a correct name or 'q' to cancel the request")
        

def delete_name(lst):
    flag = False
    while flag == False:
        print(lst)
        name = (input("Enter the name you wish to remove [enter q to exit]: ")).capitalize()
        if name in lst:
            lst.remove(name)
            flag = True
        elif name == "Q":
            flag = True
            continue
        else:
            print("No match. Enter a new name or 'q' to cancel the request")


def display_names(lst):
    print(lst)


def main():
    names = []
    flag = False
    choice = 0
    while flag == False:
        try:
            choice = int(input("1) Add a name to the list\n2) Modify existing name in the list\n3) Delete a name from the list\n4) Display names\n5) Exit\n~"))
            if choice == 5:
                flag = True
                continue
        except ValueError:
            print("Pick numbers from 1 to 5")
        if choice == 1:
            add_name(names)
        elif choice == 2:
            change_name(names)
        elif choice == 3:
            delete_name(names)
        else:
            display_names(names)

main()
