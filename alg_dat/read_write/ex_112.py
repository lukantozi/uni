with open("books.csv", "r") as file:
    book = input("Enter a book: ")
    author = input("Enter the author: ")
    year = input("Enter the year: ")
    new_record = book + "," + author + "," + year + "\n"


