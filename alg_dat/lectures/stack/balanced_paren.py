def exercise_8(paren):
    stack = []
    brack = {")": "(", "]": "[", "}": "{"}
    for char in paren:
        if char in "([{":
            stack.append(char)
        elif char in "]})":
            if not stack or stack[-1] != brack[char]:
                return False
            stack.pop()

    return len(stack) == 0
#print(exercise_8("(())"))
#print(exercise_8("(()"))
#print(exercise_8("({[]})"))
