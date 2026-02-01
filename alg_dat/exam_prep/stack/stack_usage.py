class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from the empty list")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from the empty list")

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

# B1: reverse a string
def reverse_string(word):
    stack = []
    for char in word:
        stack.append(char)

    result = ""
    while stack:
        result += stack.pop()

    return result
#print(reverse_string("ainom"))

# B2: balanced parentheses
def balanced_paren(seq):
    stack = Stack()
    for char in seq:
        if char == '(':
            stack.push(char)
        elif char == ')':
            if stack.is_empty():
                return False
            stack.pop()
    return stack.size() == 0
#print(balanced_paren("(())")) # -> True
#print(balanced_paren("(()")) # -> False )
#print(balanced_paren("(())()"))
#print(balanced_paren("(())()")) # -> True 

# B3: valid brackets for (), {}, []
def valid_brackets(seq):
    if len(seq) % 2 != 0:
        return False

    if len(seq) == 0:
        return ""

    stack = Stack()
    match = {'(': ')', '{': '}', '[': ']'}

    if seq[0] in match.values():
        return False
    stack.push(seq[0])

    for br in seq[1:]:
        if br in match:
            stack.push(br)
        else:
            if br != match[stack.pop()]:
                return False

    return stack.size() == 0

#print(valid_brackets("()"))
#print(valid_brackets("([])"))
#print(valid_brackets("([{}])"))
#print(valid_brackets("(]"))
#print(valid_brackets("(])]"))
#print(valid_brackets("(["))
#print(valid_brackets("()()(){}{}"))
#print(valid_brackets("{[(])}"))
#print(valid_brackets("((())")) # )))]]]}}}} <- to close

# B4: decimal to binary
def dec_to_bin(number):
    binary_rev = Stack()
    while number != 0:
        binary_rev.push(number % 2)
        number //= 2
     
    binary = ""
    while not binary_rev.is_empty():
        binary += str(binary_rev.pop())
    return binary
#print(dec_to_bin(156))

# B5: palindrome check
def check_palindrome(seq):
    stack = Stack()
    for char in seq:
        stack.push(char)

    for char in seq:
        if char != stack.pop():
            return False
    return True
#print(check_palindrome("madam"))
#print(check_palindrome("racecar"))
#print(check_palindrome("12321"))
#print(check_palindrome("hello"))
#print(check_palindrome("world"))

# B6: remove adjacent duplicated
def rem_adj(seq):
    stack = Stack()
    for char in seq:
        if char not in stack.items:
            stack.push(char)
        else:
            stack.pop()
    return "".join(stack.items)
#print(rem_adj("abbaca"))
#print(rem_adj("abba"))

# B7: evaluate postfix (RPN) 
def eval_postfix(seq):
    stack = Stack()
    for char in seq:
        if char.isdigit():
            stack.push(char)
        else:
            b = int(stack.pop())
            a = int(stack.pop())
            match char:
                case '+':
                    stack.push(a + b)
                case '-':
                    stack.push(a - b)
                case '*':
                    stack.push(a * b)
                case '/':
                    stack.push(a / b)
    return stack.items[0]
#print(eval_postfix("23+"))        # 5
#print(eval_postfix("23*54-+"))    # 7
#print(eval_postfix("52-"))        # 3
#print(eval_postfix("4135/+"))     # 6 -> i have no idea how this should work; input is wrong
#print(eval_postfix("5"))          # 5

# B8: sort a stack using a helper stack
def sort_stack(arr):
    temp_arr = Stack()
    while len(arr) != 0:
        tmp = arr.pop()
        while not temp_arr.is_empty() and int(temp_arr.peek()) > int(tmp):
            arr.append(temp_arr.pop())

        temp_arr.push(tmp)
    return temp_arr.items 
#print(sort_stack([4, 5, 1, 2, 5]))
