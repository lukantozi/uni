def count_spaces(word):
    print(word.count(" "))
#count_spaces("mo  ni a")

def remove_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    res = [char for char in word if char not in vowels]
    return "".join(res)
#print(remove_vowels("monia"))
#print(remove_vowels("computer science"))

def fi_la(word):
    return word[0] == word[-1] if len(word) > 0 else ""
#print(fi_la("absa"))
#print(fi_la("abss"))
#print(fi_la(""))
