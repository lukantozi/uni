import csv

with open("books.csv", "w") as file:
    mocking = "To kill A Mockingbird" + "," + "Harper Lee" + "," + "1960" + "\n"
    history = "A Brief History of Time" + "," + "Stephen Hawking" + "," + "1988" + "\n"
    gatsby = "The Great Gatsby" + "," + "F. Scott Fitzgerald" + "," + "1922" + "\n"
    hat = "The Man Who Mistook His Wife for a Hat" + "," + "Oliver Sacks" + "," + "1985" + "\n"
    pride = "Pride and Prejudice" + "," + "Jane Austen" + "," + "1813" + "\n"
    file.write(mocking)
    file.write(history)
    file.write(gatsby)
    file.write(hat)
    file.write(pride)
