def user_inp():
    flag = False
    num = 0
    while flag == False:
        try:
            num = int(input("Please enter a number: "))
            flag = True
        except ValueError:
            print("Only numeric characters are allowed!")
    return num


def count_to_num(num):
    for i in range(num):
        print(f"{i+1} ", end="")
    print()

def main():
    to_count = user_inp()
    count_to_num(to_count)

main()
