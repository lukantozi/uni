# Python Quiz

**50 questions** | Generated: 2026-02-12 13:24
**47/50 Qs: 3, 11, 16

---

## Q1 `gate_3_lists_slicing` / `layer_b_nested`

```python
nested = [[1, 2], [3, 4], [5, 6]]
total = 0
for sublist in nested:
    total += len(sublist)
print(total)
```

### Answer:

```console
6
```
## Q2 `gate_8_modules_packages` / `layer_a_quiz`

```python
import math
import math

Does this execute math module twice?
```

### Answer:

```console
no
```
## Q3 `gate_5_list_comprehensions` / `layer_a`

```python
text = "hello"
[c for c in text if c not in "aeiou"]
```

### Answer:

```console
hll
```
## Q4 `gate_4_tuples_sets` / `layer_a`

```python
t = (1, 2, 3)
t[0] = 99
print(t)
```

### Answer:

```console
can't change tuple
```
## Q5 `gate_8_modules_packages` / `layer_a_quiz`

```python
from math import sqrt
print(math.sqrt(16))

Does this work?
```

### Answer:

```console
no, NameErrir
```
## Q6 `gate_3_lists_slicing` / `layer_c_speedrun`

```python
a = [1, 2, 3, 2, 4]
print(a.count(2))
```

### Answer:

```console
2
```
## Q7 `gate_7_exceptions` / `layer_b_quiz`

```python
def check(x):
    if x < 0:
        raise ValueError('Negative')
    return x

try:
    check(5)
except ValueError as e:
    print(e)

What prints?
```

### Answer:

```console
nothing
```
## Q8 `gate_8_modules_packages` / `layer_b_concept`

```python
What's a standard library vs third-party library?
```

### Answer:

```console
std library is built in library that comes with python installation and third-party lib is what is developed outside of the std lib
```
## Q9 `gate_7_exceptions` / `layer_c_speedrun`

```python
Is else block required?
```

### Answer:

```console
no
```
## Q10 `gate_7_exceptions` / `layer_a_quiz`

```python
try:
    raise ValueError('Custom error')
except ValueError as e:
    print(e)

What prints?
```

### Answer:

```console
Custom error
```
## Q11 `gate_3_lists_slicing` / `layer_b_nested`

```python
a = [1, 2, 3]
b = a
c = a[:]
a.append(4)
print(b, c)
```

### Answer:

```console
[1, 2, 3] [1, 2, 3]
```
## Q12 `gate_8_modules_packages` / `layer_b_concept`

```python
What happens when you import a package? Which file runs?
```

### Answer:

```console
__init__.py
```
## Q13 `gate_3_lists_slicing` / `layer_b_nested`

```python
a = [[1, 2], [3, 4]]
b = a[:]
a.append(99)
print(b)
```

### Answer:

```console
[[1, 2], [3, 4]]
```
## Q14 `gate_5_list_comprehensions` / `layer_a`

```python
[(x, y) for x in range(2) for y in range(3)]
```

### Answer:

```console
[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]
```
## Q15 `gate_8_modules_packages` / `layer_a_quiz`

```python
from random import choice
print(choice([1, 2, 3]))

What happens?
```

### Answer:

```console
one of the elements of the list is chosen and printed
```
## Q16 `gate_4_tuples_sets` / `layer_a`

```python
t = (1)
print(type(t))
```

### Answer:

```console
<class 'tuple'>
```
## Q17 `gate_3_lists_slicing` / `layer_c_speedrun`

```python
a = [1, 2, 3, 4, 5]
print(a[2:4])
```

### Answer:

```console
[3, 4]
```
## Q18 `gate_7_exceptions` / `layer_c_speedrun`

```python
Can you catch SyntaxError with try/except in the same file?
```

### Answer:

```console
no
```
## Q19 `gate_8_modules_packages` / `layer_c_speedrun`

```python
What runs when you import a package?
```

### Answer:

```console
__init__.py
```
## Q20 `gate_3_lists_slicing` / `layer_b_nested`

```python
matrix = [[1, 2, 3], [4, 5, 6]]
print(matrix[1][2])
```

### Answer:

```console
6
```
## Q21 `gate_3_lists_slicing` / `layer_a`

```python
a = [1, 2, 3, 4, 5]
print(a[3:1])
```

### Answer:

```console
[]
```
## Q22 `gate_8_modules_packages` / `layer_c_speedrun`

```python
Can a package contain other packages?
```

### Answer:

```console
yes
```
## Q23 `gate_3_lists_slicing` / `layer_c_speedrun`

```python
a = [5, 2, 8, 1]
print(max(a), min(a))
```

### Answer:

```console
8 1
```
## Q24 `gate_7_exceptions` / `layer_a_quiz`

```python
try:
    x = int('10')
except ValueError:
    print('Error')
else:
    print('Success')

What prints?
```

### Answer:

```console
Success
```
## Q25 `gate_3_lists_slicing` / `layer_a`

```python
a = [1, 2, 3, 4, 5]
print(a[1])
```

### Answer:

```console
2
```
## Q26 `gate_7_exceptions` / `layer_c_speedrun`

```python
try:
    x = 5 / 2
except:
    print('A')
else:
    print('B')

What prints?
```

### Answer:

```console
B
```
## Q27 `gate_3_lists_slicing` / `layer_a`

```python
a = [1, 2, 3, 4, 5]
print(a[:2])
```

### Answer:

```console
[1, 2]
```
## Q28 `gate_4_tuples_sets` / `layer_c_speedrun`

```python
s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s2 - s1)
```

### Answer:

```console
{4}
```
## Q29 `gate_8_modules_packages` / `layer_b_predict`

```python
# mymodule.py
def greet():
    print('Hello')

# main.py
from mymodule import greet
greet()

What prints?
```

### Answer:

```console
Hello
```
## Q30 `gate_7_exceptions` / `layer_c_speedrun`

```python
What exception for list index out of range?
```

### Answer:

```console
IndexError
```
## Q31 `gate_8_modules_packages` / `layer_a_quiz`

```python
import random
print(random.randint(1, 10))

What type of value?
```

### Answer:

```console
<class 'int'>
```
## Q32 `gate_7_exceptions` / `layer_c_speedrun`

```python
What exception for calling method on None?
```

### Answer:

```console
AttributeError
```
## Q33 `gate_5_list_comprehensions` / `layer_a`

```python
[[i for i in range(3)] for j in range(2)]
```

### Answer:

```console
[[0, 1, 2], [0, 1, 2]]
```
## Q34 `gate_4_tuples_sets` / `layer_a`

```python
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1 | s2)
```

### Answer:

```console
{1, 2, 3, 4, 5}
```
## Q35 `gate_8_modules_packages` / `layer_c_speedrun`

```python
How to import with alias?
```

### Answer:

```console
import math as m
```
## Q36 `gate_5_list_comprehensions` / `layer_a`

```python
[x if x > 0 else 0 for x in [1, -2, 3, -4]]
```

### Answer:

```console
[1, 0, 3, 0]
```
## Q37 `gate_8_modules_packages` / `layer_a_quiz`

```python
from math import sqrt
print(sqrt(16))

What prints?
```

### Answer:

```console
4.0
```
## Q38 `gate_8_modules_packages` / `layer_b_concept`

```python
Can you use import *? Is it recommended?
```

### Answer:

```console
you can, not recommended
```
## Q39 `gate_3_lists_slicing` / `layer_b_nested`

```python
a = [1, 2, 3]
b = [a[:], a[:]]
a[0] = 99
print(b)
```

### Answer:

```console
[[1, 2, 3], [1, 2, 3]]
```
## Q40 `gate_7_exceptions` / `layer_b_quiz`

```python
try:
    x = int('abc')
except ValueError:
    print('ValueError')
except Exception:
    print('Exception')

What prints?
```

### Answer:

```console
ValueError
```
## Q41 `gate_3_lists_slicing` / `layer_b_nested`

```python
a = [[1, 2], [3, 4]]
print(a)
```

### Answer:

```console
[[1, 2], [3, 4]]
```
## Q42 `gate_3_lists_slicing` / `layer_c_speedrun`

```python
a = [[1], [2], [3]]
b = a[:]
b.append(99)
print(a)
```

### Answer:

```console
[[1], [2], [3]]
```
## Q43 `gate_8_modules_packages` / `layer_a_quiz`

```python
import math
print(math.sqrt(16))

What prints?
```

### Answer:

```console
4.0
```
## Q44 `gate_7_exceptions` / `layer_c_speedrun`

```python
try:
    x = 5 / 0
except:
    print('A')
finally:
    print('B')

What prints?
```

### Answer:

```console
A
B
```
## Q45 `gate_3_lists_slicing` / `layer_a`

```python
a = [1, 2, 3, 4, 5]
b = a[:]
b[0] = 99
print(a)
```

### Answer:

```console
[1, 2, 3, 4, 5]
```
## Q46 `gate_4_tuples_sets` / `layer_b`

```python
t = (5, 2, 8, 1)
print(max(t), min(t))
```

### Answer:

```console
8 1
```
## Q47 `gate_3_lists_slicing` / `layer_a`

```python
a = [1, 2, 3, 4, 5]
x = a.pop()
print(a, x)
```

### Answer:

```console
[1, 2, 3, 4] 5
```
## Q48 `gate_6_files_io` / `layer_a`

```python
f = open("nonexistent.txt", "r")
```

### Answer:

```console
FileNotFoundError
```
## Q49 `gate_3_lists_slicing` / `layer_c_speedrun`

```python
a = [1, 2, 3, 4, 5]
del a[2]
print(a)
```

### Answer:

```console
[1, 2, 4, 5]
```
## Q50 `gate_8_modules_packages` / `layer_a_quiz`

```python
import math
print(math.pi)

What prints?
```

### Answer:

```console
3.14159
```
---

## Answers

**Q1:** `6`  
**Q2:** `No (cached in sys.modules)`  
**Q3:** `['h', 'l', 'l']`  
**Q4:** `TypeError (tuples immutable)`  
**Q5:** `No (NameError: math not defined)`  
**Q6:** `2`  
**Q7:** `Nothing (no exception)`  
**Q8:** `Standard: built-in with Python; third-party: external packages (pip install)`  
**Q9:** `No`  
**Q10:** `Custom error`  
**Q11:** `[1, 2, 3, 4] [1, 2, 3]`  
**Q12:** `__init__.py runs`  
**Q13:** `[[1, 2], [3, 4]]`  
**Q14:** `[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]`  
**Q15:** `Prints random element from list`  
**Q16:** `<class 'int'>`  
**Q17:** `[3, 4]`  
**Q18:** `No`  
**Q19:** `__init__.py and top-level code`  
**Q20:** `6`  
**Q21:** `[]`  
**Q22:** `Yes (subpackages)`  
**Q23:** `8 1`  
**Q24:** `Success`  
**Q25:** `2`  
**Q26:** `B`  
**Q27:** `[1, 2]`  
**Q28:** `{4}`  
**Q29:** `Hello`  
**Q30:** `IndexError`  
**Q31:** `int (between 1 and 10 inclusive)`  
**Q32:** `AttributeError`  
**Q33:** `[[0, 1, 2], [0, 1, 2]]`  
**Q34:** `{1, 2, 3, 4, 5}`  
**Q35:** `import something as alias`  
**Q36:** `[1, 0, 3, 0]`  
**Q37:** `4.0`  
**Q38:** `Yes, but not recommended (pollutes namespace with all public names)`  
**Q39:** `[[1, 2, 3], [1, 2, 3]]`  
**Q40:** `ValueError`  
**Q41:** `[[1, 2], [3, 4]]`  
**Q42:** `[[1], [2], [3]]`  
**Q43:** `4.0`  
**Q44:** `A\nB`  
**Q45:** `[1, 2, 3, 4, 5]`  
**Q46:** `8 1`  
**Q47:** `[1, 2, 3, 4] 5`  
**Q48:** `FileNotFoundError`  
**Q49:** `[1, 2, 4, 5]`  
**Q50:** `3.14159...`  
