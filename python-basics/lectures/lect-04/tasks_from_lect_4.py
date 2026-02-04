#Task 1

def sum_digit(x, y, z):
    return x, y, z, x+y+z


a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
sum_dig = sum_digit(a, b, c)
print(f"{sum_dig[0]} + {sum_dig[1]} + {sum_dig[2]} = {sum_dig[3]}")

#Task 2

def max_abs(x, y, z, t):
    max = 0
    if abs(x) > abs(y):
        max = x
    if abs(y) > abs(z):
        max = y
    if abs(z) > abs(t):
        max = z
    else:
        max = t
    return max

print(max_abs(4,-3,15,-9))


#Task 3

def biggest_power_two(n):
    m = 0
    while n >= 2**m:
        m += 1
    return 2**(m-1)

print(biggest_power_two(int(input("num: "))))

#Task 4

def first_x_digit(n, x):
    while n > 10**x:
        n = n//10
    return n

print(first_x_digit((int(input("Number: "))), int(input("Number of first digits: "))))


#Task 5 

#(a)
def sum_while(n):
    m = 0
    while n > 0:
        m += n%10 
        n //= 10
    return m

print(sum_while(int(input("Num: "))))


#(b)
def sum_for(n):
    num_str = str(n)
    m = 0
    for i in num_str:
        m += int(i)
    return m

print(sum_for(int(input("Num: "))))


#Task 6

def pyramid(n):
    for i in range(1, n+1):
        for _ in range(i):
            print(i, end="")
        print()

pyramid(int(input("Num: ")))


#Task 7

def palindrome(num):
    length = 0
    num_to_count = num
    num_to_compare = num
    while num_to_count > 0:
        num_to_count = num_to_count // 10
        length += 1

    reverse_num = 0
    for i in range(0, length+1):
        reverse_num += (num%10)*(10**(length-i-1))
        num = num//10

    if num_to_compare == reverse_num:
        return True
    return False

print(palindrome(int(input("Num: "))))
