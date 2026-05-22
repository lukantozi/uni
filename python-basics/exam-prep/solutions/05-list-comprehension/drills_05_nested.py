def divisible_any_dig():
    return [x for x in range(1, 1000) if any(x % i == 0 for i in range(2, 10))]

#print(divisible_any_dig())

def numbers_with_six():
    return [x for x in range(6, 97) if '6' in str(x)]

#print(numbers_with_six())

def combine_lists(arr1, arr2):
    return [(x, y) for x in arr1 for y in arr2]

#print(combine_lists([1, 2, 3], ['a', 'b']))

def words_len(sentence):
    return {word.strip("';\",.!?`"): len(word) for word in sentence.split()}

#print(words_len("hello, world! how you doin?"))

def max_len_words(sentence):
    words = sentence.split()
    return max((word.strip(";',.!?") for word in words), key=len)

#print(max_len_words("hello, world! whatsaap, "))


def max_len_words_with_dicts(sentence):
    wrd_dict = {word.strip("';\",.!?`"): len(word) for word in sentence.split()}
    longest = max(wrd_dict.keys(), key=len)
    return longest

#print(max_len_words_with_dicts("hello, world! whatsaap, "))
