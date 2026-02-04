# B4: decimal to binary (15 mins max)
def dec_to_bin(number):
    stack = []
    while number != 0:
        stack.append(number % 2)
        number //= 2
    result = ""
    while stack:
        result += str(stack.pop())
    return result
#print(dec_to_bin(156))

# B5: palidnrome check (15 mins max)
def check_palindrome(seq):
    stack = []
    for char in seq:
        stack.append(char)
     
    for char in seq:
        if char != stack.pop():
            return False
    return True
#print(check_palindrome("madam"))
#print(check_palindrome("racecar"))
#print(check_palindrome("12321"))
#print(check_palindrome("hello"))
#print(check_palindrome("world"))

# B6: remove adjacent dupes (15 mins max)
def rem_adj(seq):
    stack = []
    for char in seq:
        if char not in stack:
            stack.append(char)
        else:
            stack.pop()
    return "".join(stack)

#print(rem_adj("abbaca"))
#print(rem_adj("abba"))

# B3: valid brackets (12.5 mins max)
def valid_brackets(seq):
    stack = []
    match = {'(': ')', '[': ']', '{': '}'}
    if seq[0] not in match:
        return False
    stack.append(seq[0])

    for br in seq[1:]:
        if br in match:
            stack.append(br)
        elif br != match[stack.pop()]:
            return False
    return len(stack) == 0

#print(valid_brackets("()"))
#print(valid_brackets("([])"))
#print(valid_brackets("([{}])"))
#print(valid_brackets("(]"))
#print(valid_brackets("(])]"))
#print(valid_brackets("(["))
#print(valid_brackets("()()(){}{}"))
#print(valid_brackets("{[(])}"))
#print(valid_brackets("((())")) # )))]]]}}}} <- to close

# B7: postfix eval (12.5 mins max)
def eval_postfix(seq):
    stack = []
    for token in seq:
        if token.isdigit():
            stack.append(token)
        else:
            b = int(stack.pop())
            a = int(stack.pop())
            match token:
                case '+':
                    stack.append(a + b)
                case '-':
                    stack.append(a - b)
                case '*':
                    stack.append(a * b)
                case '/':
                    stack.append(a // b)
    return stack[0]


print(eval_postfix("23+"))        # 5
print(eval_postfix("23*54-+"))    # 7
print(eval_postfix("52-"))        # 3
print(eval_postfix("5"))          # 5
print(eval_postfix("142/+"))      # 3
