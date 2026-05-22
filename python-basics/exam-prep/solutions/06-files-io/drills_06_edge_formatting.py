import datetime

def count_spaces():
    f = open("example1.txt", "r")

    r = f.read()
    spaces = r.count(" ")

    f.close()
    return spaces

#print(count_spaces())

def write_filtered():
    f = open("example1.txt", "r")
    stripped = ""
    for line in f:
        stripped += line.strip('\n')

    f.close()

    stripped += '\n'
    f = open("example1_stripped.txt", "w")
    f.write(stripped)
    f.close()

#write_filtered()

def read_reversed():
    with open("example1.txt", "r") as f:
        lines = f.readlines()

    with open("example1_reversed.txt", "w") as f:
        f.writelines(lines[::-1])

#read_reversed()

def open_csv():
    with open("example1.txt", "r") as f:
        lines = []
        for line in f:
            lines.append([line])
    for line in lines:
        print(line)
#open_csv()

def log_time():
    with open("log_time.txt", "a") as log:
        now = datetime.datetime.now()
        log.write(f"log_time called at: {now}\n")
#log_time()
