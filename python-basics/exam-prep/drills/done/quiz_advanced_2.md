# Python Quiz

**50 questions** | Generated: 2026-02-12 14:40
**45/50 Qs: 8, 17, 23, 37, 45**

---

## Q1 `gate_7_exceptions` / `layer_c_speedrun`

```python
try:
    assert 2 + 2 == 5
except AssertionError:
    print('Wrong')

What prints?
```

### Answer:

```console
Wrong
```
## Q2 `gate_4_tuples_sets` / `layer_a`

```python
t = (1, 2, 3)
print(t.index(3))

What prints?
```

### Answer:

```console
2
```
## Q3 `gate_8_modules_packages` / `layer_b_predict`

```python
from math import sqrt
from math import floor
print(sqrt(16) + floor(3.9))

What prints?
```

### Answer:

```console
7.0
```
## Q4 `gate_7_exceptions` / `layer_c_speedrun`

```python
What exception for accessing attribute that doesn't exist?
```

### Answer:

```console
AttributeError
```
## Q5 `gate_5_list_comprehensions` / `layer_a`

```python
[x*2 for x in [1, 2, 3]]

What is the result?
```

### Answer:

```console
[2, 4, 6]
```
## Q6 `gate_4_tuples_sets` / `layer_a`

```python
s = {1, 2, 3}
print(min(s))

What prints?
```

### Answer:

```console
1
```
## Q7 `gate_4_tuples_sets` / `layer_b`

```python
s = {}
print(type(s))

What prints?
```

### Answer:

```console
<class 'dict'>
```
## Q8 `gate_6_files_io` / `layer_c_speedrun`

```python
with open('f.txt', 'w') as f:
    f.write('example')
with open('f.txt') as f:
    print(len(f.read()))

What prints?
```

### Answer:

```console
6 -> 7 (wth)
```
## Q9 `gate_5_list_comprehensions` / `layer_a`

```python
[abs(x) for x in [-1, -2, 3]]

What is the result?
```

### Answer:

```console
[1, 2, 3]
```
## Q10 `gate_6_files_io` / `layer_c_speedrun`

```python
# file: 'HELLO'
with open('f.txt') as f:
    print(f.read().lower())

What prints?
```

### Answer:

```console
hello
```
## Q11 `gate_6_files_io` / `layer_c_speedrun`

```python
with open('f.txt', 'w') as f:
    f.write(str(3))
with open('f.txt') as f:
    print(f.read())

What prints?
```

### Answer:

```console
3
```
## Q12 `gate_6_files_io` / `layer_b`

```python
# file contains: 'a\nb\nc\n'
with open('f.txt', 'r') as f:
    lines = [line.strip() for line in f]
print(lines)

What prints?
```

### Answer:

```console
['a', 'b', 'c']
```
## Q13 `gate_7_exceptions` / `layer_b_quiz`

```python
try:
    x = 'hello'[10]
except IndexError:
    print('IndexError')

What prints?
```

### Answer:

```console
IndexError
```
## Q14 `gate_6_files_io` / `layer_c_speedrun`

```python
with open('f.txt', 'w') as f:
    f.write('123')
with open('f.txt') as f:
    print(f.read().upper())

What prints?
```

### Answer:

```console
123
```
## Q15 `gate_7_exceptions` / `layer_c_speedrun`

```python
try:
    f = open('missing.txt')
    f.close()
except FileNotFoundError:
    pass

Is there a problem?
```

### Answer:

```console
not a problem
```
## Q16 `gate_8_modules_packages` / `layer_b_predict`

```python
import math as m
print(m.floor(3.7))

What prints?
```

### Answer:

```console
3
```
## Q17 `gate_3_lists_slicing` / `layer_b_nested`

```python
a = [1, 2, 3]
b = a
a += [4]
print(b)

What prints?
```

### Answer:

```console
[1, 2, 3] -> [1, 2, 3, 4] (a = a + [4] creates a new list, other methods like a += [4] or a.append(4), modifies it in place)
```
## Q18 `gate_6_files_io` / `layer_c_speedrun`

```python
with open('f.txt', 'w') as f:
    f.write('data2')
with open('f.txt') as f:
    print(f.read().upper())

What prints?
```

### Answer:

```console
DATA2
```
## Q19 `gate_5_list_comprehensions` / `layer_a`

```python
[[x] for x in range(3)]

What is the result?
```

### Answer:

```console
[[0], [1], [2]]
```
## Q20 `gate_8_modules_packages` / `layer_b_concept`

```python
import math
import math

Does Python load math module twice?
```

### Answer:

```console
no
```
## Q21 `gate_6_files_io` / `layer_b`

```python
# file contains: 'a\nb\nc'
with open('f.txt', 'r') as f:
    lines = [line.rstrip('\n') for line in f]
print(lines)

What prints?
```

### Answer:

```console
['a', 'b', 'c']
```
## Q22 `gate_7_exceptions` / `layer_b_quiz`

```python
try:
    x = 'hello' + 5
except TypeError:
    print('Cannot add')

What prints?
```

### Answer:

```console
Cannot add
```
## Q23 `gate_3_lists_slicing` / `layer_c_speedrun`

```python
a = [1, 2, 3, 4, 5]
print(a[1:-1])

What prints?
```

### Answer:

```console
[2, 1] -> [2, 3, 4] (gotta be more careful)
```
## Q24 `gate_3_lists_slicing` / `layer_c_speedrun`

```python
a = [1, 2, 3, 4, 5]
print(a[::3])

What prints?
```

### Answer:

```console
[1, 4]
```
## Q25 `gate_5_list_comprehensions` / `layer_a`

```python
[x**2 for x in range(5)]

What is the result?
```

### Answer:

```console
[0, 1, 4, 9, 16]
```
## Q26 `gate_6_files_io` / `layer_c_speedrun`

```python
# file: 'ABC'
with open('f.txt') as f:
    print(f.read().islower())

What prints?
```

### Answer:

```console
False
```
## Q27 `gate_6_files_io` / `layer_c_speedrun`

```python
with open('f.txt', 'w') as f:
    f.write('abc')
with open('f.txt') as f:
    print(f.read().upper())

What prints?
```

### Answer:

```console
ABC
```
## Q28 `gate_3_lists_slicing` / `layer_c_speedrun`

```python
a = [5, 2, 8, 1]
print(min(a))

What prints?
```

### Answer:

```console
1
```
## Q29 `gate_3_lists_slicing` / `layer_b_nested`

```python
a = [1, 2, 3]
b = [a] * 2
a.append(4)
print(b)

What prints?
```

### Answer:

```console
[1, 2, 3, 1, 2, 3, 4] -> [[1, 2, 3, 4], [1, 2, 3, 4]]
```
## Q30 `gate_3_lists_slicing` / `layer_c_speedrun`

```python
a = [1, -2, 3]
print(all(x > 0 for x in a))

What prints?
```

### Answer:

```console
False
```
## Q31 `gate_3_lists_slicing` / `layer_c_speedrun`

```python
a = [1, 2, 3]
print(len(a))

What prints?
```

### Answer:

```console
3
```
## Q32 `gate_8_modules_packages` / `layer_c_speedrun`

```python
import math
print(math.pow(2, 3))

What prints?
```

### Answer:

```console
8 -> 8.0
```
## Q33 `gate_3_lists_slicing` / `layer_c_speedrun`

```python
a = [1, 2, 3]
a.append([4, 5])
print(a)

What prints?
```

### Answer:

```console
[1, 2, 3, [4, 5]]
```
## Q34 `gate_4_tuples_sets` / `layer_a`

```python
s = {1, 2}
s.update([3, 4])
print(s)

What prints?
```

### Answer:

```console
{1, 2, 3, 4}
```
## Q35 `gate_3_lists_slicing` / `layer_c_speedrun`

```python
a = [1, 2, 3, 4]
print(a[1:3])

What prints?
```

### Answer:

```console
[2, 3]
```
## Q36 `gate_6_files_io` / `layer_b`

```python
with open('f.txt', 'w') as f:
    f.write('hello')
with open('f.txt', 'r') as f:
    a = f.read(2)
    b = f.read(3)
print(a, b)

What prints?
```

### Answer:

```console
he llo
```
## Q37 `gate_3_lists_slicing` / `layer_b_nested`

```python
a = [1, 2, 3, 4, 5]
print(a[:10])

What prints?
```

### Answer:

```console
IndexError -> all the elements (slicing is forgiving i guess)
```
## Q38 `gate_6_files_io` / `layer_c_speedrun`

```python
with open('f.txt', 'w') as f:
    f.write('data')
with open('f.txt') as f:
    print(len(f.read()))

What prints?
```

### Answer:

```console
4
```
## Q39 `gate_8_modules_packages` / `layer_b_predict`

```python
# In mymodule.py:
print(__name__)

# In main.py:
import mymodule

What does mymodule.py print?
```

### Answer:

```console
mymodule
```
## Q40 `gate_5_list_comprehensions` / `layer_a`

```python
[x.lower() for x in ['A', 'B', 'C']]

What is the result?
```

### Answer:

```console
['a', 'b', 'c']
```
## Q41 `gate_5_list_comprehensions` / `layer_a`

```python
[len(x) for x in ['a', 'bb', 'ccc']]

What is the result?
```

### Answer:

```console
[1, 2, 3]
```
## Q42 `gate_4_tuples_sets` / `layer_b`

```python
s = {3, 1, 2}
print(sorted(s))

What prints?
```

### Answer:

```console
[1, 2, 3]
```
## Q43 `gate_4_tuples_sets` / `layer_b`

```python
s = {1, 2, 3}
s.discard(5)
print(s)

What prints?
```

### Answer:

```console
{1, 2, 3}
```
## Q44 `gate_6_files_io` / `layer_c_speedrun`

```python
# file: 'python'
with open('f.txt') as f:
    content = f.read()
print(len(content))

What prints?
```

### Answer:

```console
6
```
## Q45 `gate_3_lists_slicing` / `layer_c_speedrun`

```python
a = [1, 2, 3]
print(a * 0)

What prints?
```

### Answer:

```console
0 -> []
```
## Q46 `gate_6_files_io` / `layer_b`

```python
with open('f.txt', 'w') as f:
    f.write('test')
with open('f.txt', 'r') as f:
    content = f.read()
    again = f.read()
print(len(again))

What prints?
```

### Answer:

```console
0
```
## Q47 `gate_6_files_io` / `layer_c_speedrun`

```python
with open('f.txt', 'w') as f:
    f.write('text')
with open('f.txt') as f:
    print(len(f.read()))

What prints?
```

### Answer:

```console
4
```
## Q48 `gate_4_tuples_sets` / `layer_a`

```python
s = {1, 2, 3, 2, 1}
print(s)

What prints?
```

### Answer:

```console
{1, 2, 3}
```
## Q49 `gate_4_tuples_sets` / `layer_b`

```python
t = (5, 2, 8, 1)
print(max(t))

What prints?
```

### Answer:

```console
8
```
## Q50 `gate_6_files_io` / `layer_b`

```python
# Two files: a.txt and b.txt
with open('a.txt', 'w') as f:
    f.write('hello')
with open('b.txt', 'w') as f:
    f.write('world')

How many files created?
```

### Answer:

```console
2
```
---

## Answers

**Q1:** `Wrong`  
**Q2:** `2`  
**Q3:** `7.0`  
**Q4:** `AttributeError`  
**Q5:** `[2, 4, 6]`  
**Q6:** `1`  
**Q7:** `<class 'dict'>`  
**Q8:** `7`  
**Q9:** `[1, 2, 3]`  
**Q10:** `hello`  
**Q11:** `3`  
**Q12:** `['a', 'b', 'c']`  
**Q13:** `IndexError`  
**Q14:** `123`  
**Q15:** `No (exception prevents f.close() from running, which is fine)`  
**Q16:** `3`  
**Q17:** `[1, 2, 3, 4]`  
**Q18:** `DATA2`  
**Q19:** `[[0], [1], [2]]`  
**Q20:** `No (modules are cached after first import)`  
**Q21:** `['a', 'b', 'c']`  
**Q22:** `Cannot add`  
**Q23:** `[2, 3, 4]`  
**Q24:** `[1, 4]`  
**Q25:** `[0, 1, 4, 9, 16]`  
**Q26:** `False`  
**Q27:** `ABC`  
**Q28:** `1`  
**Q29:** `[[1, 2, 3, 4], [1, 2, 3, 4]]`  
**Q30:** `False`  
**Q31:** `3`  
**Q32:** `8.0`  
**Q33:** `[1, 2, 3, [4, 5]]`  
**Q34:** `{1, 2, 3, 4}`  
**Q35:** `[2, 3]`  
**Q36:** `he llo`  
**Q37:** `[1, 2, 3, 4, 5]`  
**Q38:** `4`  
**Q39:** `mymodule`  
**Q40:** `['a', 'b', 'c']`  
**Q41:** `[1, 2, 3]`  
**Q42:** `[1, 2, 3]`  
**Q43:** `{1, 2, 3}`  
**Q44:** `6`  
**Q45:** `[]`  
**Q46:** `0`  
**Q47:** `4`  
**Q48:** `{1, 2, 3}`  
**Q49:** `8`  
**Q50:** `2`  
