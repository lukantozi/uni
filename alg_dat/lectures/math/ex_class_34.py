while True:
    resp = int(input("1) Square\n2) Triangle\n\nEnter a number: "))
    if resp == 1:
        square_side = int(input("Enter the length of the square side: "))
        print(f"The area of the square is {square_side*4}")
        break
    elif resp == 2:
        trianlge_height = int(input("Enter the length of the triangle height: "))
        trianlge_base = int(input("Enter the length of the triangle base: "))
        print(f"The area of the square is {trianlge_base * trianlge_height}")
        break
    else:
        print("Please enter 1 to choose square and 2 to choose triangle")
