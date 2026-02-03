class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty stack")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

def example():
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)

    print(s.pop())
    print(s.peek())
    print(s.size())
    print(s.items)
    print(s.size())
#example()

def exercise_6():
    s = Stack()
    for n in range(1, 6):
        s.push(n)
    print(s.items)
    while not s.is_empty():
        print(f"Popped: {s.pop()}")
    print(s.items)
#exercise_6()

def exercise_7(word):
    lis_wrd = list(word)
    s = Stack()
    while lis_wrd:
        s.push(lis_wrd.pop())
    print(str(s.items))
#exercise_7("hello")

def exercise_20(expr):
    s = Stack()
    oper = ["+", "-", "*", "/"]
    for char in expr:
        if char.isdigit():
            s.push(char)
        elif char in oper:
            b = float(s.pop())
            a = float(s.pop())
            match char:
                case "+":
                    s.push(a + b)
                case "-":
                    s.push(a - b)
                case "*":
                    s.push(a * b)
                case "/":
                    s.push(a / b)
    return s.items[0]
#print(exercise_20("23*54*+9-"))

def exercise_23(expr):
    s = Stack()
    size = len(expr)
    for i in range(size):
        if not s.is_empty() and expr[i] == s.peek():
            s.pop()
        else:
            s.push(expr[i])
    return "".join(s.items)
#print(exercise_23("abbaca"))

def exercise_21(expr):
    s = Stack()
