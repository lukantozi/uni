# capitalize()
# tasks 1, 2
def return_capitalize(txt):
    return txt.capitalize()


def print_capitalize():
    print(return_capitalize("hELLO world"))
    print(return_capitalize("123abc"))
    print(return_capitalize(" leading space"))
    print(return_capitalize("ßtraße"))
    print(return_capitalize("προγραμμα"))
    print(return_capitalize(""))
#print_capitalize()


# casefold()
# task 1
def equal_case_insensitive(a, b):
    a_lower = a.casefold()
    b_lower = b.casefold()
    if a_lower == b_lower:
        return True
    return False
#print(equal_case_insensitive("straße", "STRASSE"))
#print(equal_case_insensitive("İSTANBUL", "istanbul"))


# task 2
def mini_search(needle, haystack):
    if needle.casefold() in haystack.casefold():
        return True
    return False
#print(mini_search("fun", "Python is FUN!"))
#print(mini_search("STRASSE", "ßtraße"))


# center()
# task 1
def center_ex_1(): 
    print("Hello".center(20, '-'))
    print("Hello".center(20, '.'))
    print("Hello".center(3, '-'))


# task 2
def center_ex_2(txt, symbol):
    print(30*symbol)
    print(txt.center(30, symbol))
    print(30*symbol)
#center_ex_2("boxed title", "*")


# count()
# task 1
def encode_ex_1():
    print("café".encode("utf-8"))
    print("café".encode("latin-1"))
    print("café".encode("ascii", "ignore"))
    print("café".encode("ascii", "replace"))
#encode_ex_1()


# task 2
def encode_ex_2(txt_list):
    enc_list = []
    for txt in txt_list:
        enc_list.append(txt.encode())
    return enc_list
#print(encode_ex_2(["hello", "σωκρατης", "⚡"]))


# endswith()
# task 1
def endswith_ex_1():
    print("report.pdf".endswith("pdf"))
    print("archive.tar.gz".endswith((".gz", ".zip")))
#endswith_ex_1()


# task 2
def endswith_ex_2():
    print("unbelievable".endswith("lie", 2, 8))
#endswith_ex_2()
# --> False; --> True for 2, 7


# expandtabs()
# task 1
def expandtabs_ex_1():
    txt = "col1\tcol2\tcol3"
    print(txt.expandtabs())
    print(txt.expandtabs(4))
    print(txt.expandtabs(10))
    print(txt.expandtabs(1))
#expandtabs_ex_1()
# --> i have 4 as default; instead of 10, i get 6 tabs


# task 2
def expandtabs_ex_2():
    table = "name\tage\tcity\nAna\t10\tParis\nBob\t9\tRome"
    print(table.expandtabs())
    print(table.expandtabs(9))
    print(table.expandtabs(10))
    print(table.expandtabs(11))
    print(table.expandtabs(12))
    print(table.expandtabs(16))
#expandtabs_ex_2()


# find()
# task 1
def find_ex_1():
    print("concatination".find("cat"))
    print("concatination".find("cat", 4))
#find_ex_1()


# task 2
def find_ex_2():
    print("aaaa".find("aa"))
    print("aaaa".find("aa", 1))
    print("aaaa".find("aa", 2))
    print("aaaa".find("aa", 3))
    print("aaaa".find("b"))
#find_ex_2()


# format()
# task 1
def format_ex_1():
    txt = "Name: {:<10}, Age: {:d}, Balance: {:.2f}"
    print(txt.format("Luka", 24, 300))
#format_ex_1()


def format_ex_2():
    table_row = "{:<10}|{:^10}|{:>8.2f}"
    print(table_row.format("cola", 2, 3))
#format_ex_2()


# format_map()
# task 1
def format_map_ex_1():
    data = {"name": "Alice", "age": 30}
    txt  = "My name is {name}. I am {age}."
    print(txt.format_map(data))
#format_map_ex_1()


# task 2
class Custom_Mapping:
    def __init__(self):
        pass
# this is to chatGPT: i am not sure what you are asking me here. not that good with classes yet.


# index
# task 1
def index_ex_1():
    print("happy python".index("py"))
    print("banana".index("n"))
    print("banana".index("m"))
#index_ex_1()


# task 2
def index_ex_2(word, subword):
    word_len = len(word)
    subword_len = len(subword)
    i = 0
    while i < word_len:
        try:
            print(word.index(subword, i))
            i += subword_len
        except ValueError:
            i += 1
#index_ex_2("banana", "ana")


# isalnum()
# task 1
def isalnum_ex_1():
    print("abc123".isalnum())
    print("abc 123".isalnum())
    print("abc!".isalnum())
    print("123".isalnum())
#isalnum_ex_1()


# task 2
def isalnum_ex_2(list):
    for str in list:
        if str.isalnum():
            print(str)
#isalnum_ex_2(["", "école", "213moni", "moni 123"])


# isalpha()
# task 1
def isalpha_ex_1():
    print("abc".isalpha())
    print("abc123".isalpha())
    print("ß".isalpha())
    print("你好".isalpha())
#isalpha_ex_1()


# task 2
def isalpha_ex_2(txt):
    word = ""
    words_list = []
    for l in txt:
        if l.isalpha():
            word += l
        else:
            if word:
                words_list.append(word)
                word = ""
    if word:
        words_list.append(word)
    return words_list
#print(isalpha_ex_2("pure alphabetica2l, words$  should work"))


# isdecimal()
# task 1
def isdecimal_ex_1():
    print("123".isdecimal())
    print("①②".isdecimal())
    print("⅓".isdecimal())
    print("٢٣".isdecimal())
#isdecimal_ex_1()


# task 2
def isdecimal_ex_2():
    while True:
        deci = input("Enter a decimal number: ")
        if deci.isdecimal():
            return "Accepted"
        elif deci == "q":
            return 0
#print(isdecimal_ex_2())


# isdigit()
# task 1
def isdigit_ex_1():
    print("isdecimal(): ")
    print("123".isdecimal())
    print("²³".isdecimal())
    print("①②".isdecimal())
    print()
    print("isdigit(): ")
    print("123".isdigit())
    print("²³".isdigit())
    print("①②".isdigit())
#isdigit_ex_1()


# task 2
def isdigit_ex_2():
    print("123".isdigit())
    print("²³".isdigit())
    print("⅓".isdigit())
#isdigit_ex_2()
## chatGPT this is to you. i don't know what you meant by to write a function to find out if the input is digit but not necessarily a decimal. is not that the main idea of isdigit? i am not sure


# islower()
# task 1
def islower_ex_1():
    print("hello".islower())
    print("Hello".islower())
    print("hello!".islower())
    print("123abc".islower())
#islower_ex_1()


# task 2
def islower_ex_2(word):
    for letter in word:
        if letter.isalpha():
            return word.islower()
    return "no letter in the word"
#print(islower_ex_2("hellO"))
#print(islower_ex_2("hello"))
#print(islower_ex_2("1234"))
#print(islower_ex_2("1234@"))

# isnumeric()
# task 1
def isnumeric_ex_1():
    print("insmueric: ")
    print("123".isnumeric())
    print("⅓".isnumeric())
    print("١٢٣".isnumeric())
    print("四".isnumeric())
    print()
    print("isdigit(): ")
    print("123".isdigit())
    print("⅓".isdigit())
    print("١٢٣".isdigit())
    print("四".isdigit())
    print()
    print("isdecimal(): ")
    print("123".isdecimal())
    print("⅓".isdecimal())
    print("١٢٣".isdecimal())
    print("四".isdecimal())
#isnumeric_ex_1()


# task 2
def isnumeric_ex_2():
    while True:
        string = input("Enter a numeric string: ")
        if string.isnumeric():
            return "Accepted"
        elif string == "q":
            return "Cancelled"
#print(isnumeric_ex_2())


# isprintable()
# task 1
def isprintable_ex_1():
    print("Hello\nWorld".isprintable())
    print("Hello World".isprintable())
    print("Hello\tWorld".isprintable())
    print("Hello\x00World".isprintable())
#isprintable_ex_1()


# task 2
def isprintable_ex_2(txt):
    printable = ""
    for l in txt:
        if l.isprintable():
            printable += l
        else:
            printable += "?"
    return printable
#print(isprintable_ex_2("hello\nworld"))


# isspace()
# task 1
def isspace_ex_1():
    print(" ".isspace())
    print("\t".isspace())
    print("\n".isspace())
    print(" \t".isspace())
    print(" a ".isspace())
#isspace_ex_1()


# task 2
# not necessary


# istitle()
# task 1
def istitle_ex_1():
    print("This Is A Title".istitle())
    print("This Is NOT".istitle())
    print("This is Not".istitle())
    print("Hello-World".istitle())
    print("I'm A Title".istitle())
#istitle_ex_1()


# task 2
def istitle_ex_2(sentence):
    word = ""
    words_list = []
    for l in sentence:
        if l.isalnum():
            word += l
        else:
            if word:
                words_list.append(word)
                word = ""

    if word:
        words_list.append(word)
    non_title_list = []

    for w in words_list:
        if not w.istitle():
            non_title_list.append(w)
    return non_title_list
#print(istitle_ex_2("This function, 12, only RETURns, noN, Title-Words , tiTLe, WORds"))


# isupper()
# task 1
def isupper_ex_1():
    print("HELLO".isupper())
    print("HELLO!".isupper())
    print("Hello".isupper())
    print("123ABC".isupper())
#isupper_ex_1()


# task 2
def isupper_ex_2(txt):
    for l in txt:
        if l.isalpha():
            if txt.isupper():
                return True
        else:
            return "no letter in the string"
    return False
#print(isupper_ex_2("HELLO"))
#print(isupper_ex_2("HELLO!"))
#print(isupper_ex_2("Hello"))
#print(isupper_ex_2("123ABC"))
#print(isupper_ex_2("123"))


# join()
# task 1
def join_ex_1():
    print(",".join(["a", "b", "c"]))
    print(",".join([]))
    print(",".join(["one"]))
#join_ex_1()


# task 2
def join_ex_2(l):
    return " - ".join(l)
#print(join_ex_2(["a", "am", "the"]))
#print(join_ex_2(["a", 1, "b"])) # --> error: has to be list of strings


# ljust()
# task 1
def ljust_ex_1():
    print("Hi".ljust(10, "."))
#ljust_ex_1()


# task 2
def ljust_ex_2():
    pass
