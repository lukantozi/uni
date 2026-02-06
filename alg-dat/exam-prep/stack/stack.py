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
        raise IndexError("peek from the emprt list")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

s = Stack()
print(s.is_empty())
for i in range(2, 10, 2):
    s.push(i*10)
print(s.items)

print(s.peek())
size = s.size()
print(size)

for _ in range(size):
    print(f"popping: {s.peek()}")
    s.pop()
    print(f"after popping: {s.items}")

print(s.is_empty())
