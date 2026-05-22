def drill_01():
    total = 0
    with open("example1.txt", "r") as f:
        for _ in range(3):
            nums = [int(num) for num in f.readline().split() if num.isdigit()]
            total += sum(nums)
    return total 

#print(drill_01())

def drill_02():
    import os
    count = 0

    f = open("example1.txt", "r")
    chars = f.read(3)
    f.close()

    f = open("example1.txt", "r")
    for _ in f:
        count += 1
    f.close()

    if os.path.exists("example2.txt"):
        f = open("example2.txt", "a")
    else:
        f = open("example2.txt", "x")

    f.write(f"count: {count}\nfirst three: {chars}\n")
    f.close()

#drill_02()

def drill_03():
    f1 = open("example1.txt", "r")
    f2 = open("example1_won.txt", "w")

    f2.write(f"{''.join([line.strip("\n\t") for line in f1])}\n")
    # for line in f1:
    #    f2.write(line.strip() + '\n')
    
    f1.close()
    f2.close()

#drill_03()

def alphabet_in_lines(n):
    from string import ascii_lowercase 

    iter = 26 // n
    letters = ascii_lowercase
    st = 0
    new = "" 
    with open("letters.txt", "w") as f:
#        for i in range(0, len(letters), n):
#            f.write(letters[i:i+n] + '\n')
        for _ in range(iter+1):
            new += (letters[st:st+n]+'\n')
            st += n
        f.write(new)

#alphabet_in_lines(10)

def combine_files():
    f1 = open("example1.txt", "r")
    f2 = open("example2.txt", "r")
    f3 = open("combine.txt", "w")

    new = ""
    for line in zip(f1.readlines(), f2.readlines()):
        new = new + line[0].replace('\n', ". ") + line[1] + '\n'
    
    f3.write(new)
    f1.close()
    f2.close()
    f3.close()

combine_files()
