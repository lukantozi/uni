# Python Quiz

**25 questions** | Generated: 2026-02-12 16:03

---

## Q1 `gate_4_tuples_sets` / `layer_a`

```python
s = {1, 2, 3}
print(2 in s)

What prints?
```

### Answer:

```console
True
```
## Q2 `gate_3_lists_slicing` / `layer_b_nested`

```python
a = [1, 2, 3]
b = a[:]
a.append(4)
print(b)

What prints?
```

### Answer:

```console
[1, 2, 3]
```
## Q3 `gate_6_files_io` / `layer_c_speedrun`

```python
with open('f.txt', 'w') as f:
    f.write('world')
with open('f.txt') as f:
    print(len(f.read()))

What prints?
```

### Answer:

```console
5
```
## Q4 `gate_8_modules_packages` / `layer_c_speedrun`

```python
from math import floor, ceil
print(floor(3.9), ceil(2.1))

What prints?
```

### Answer:

```console
3 3
```
## Q5 `gate_4_tuples_sets` / `layer_c_speedrun`

```python
s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1 - s2)

What prints?
```

### Answer:

```console
{1}
```
## Q6 `gate_5_list_comprehensions` / `layer_a`

```python
{x: x**2 for x in range(4)}

What is the result?
```

### Answer:

```console
{0: 0, 1: 1, 2: 4, 3: 9}
```
## Q7 `gate_7_exceptions` / `layer_b_quiz`

```python
try:
    x = int(input())  # user enters 'abc'
    y = 10 / x
except (ValueError, ZeroDivisionError):
    print('Error')

What prints?
```

### Answer:

```console
Error
```
## Q8 `gate_6_files_io` / `layer_c_speedrun`

```python
with open('f.txt', 'w') as f:
    f.write('data1')
with open('f.txt') as f:
    print(f.read().upper())

What prints?
```

### Answer:

```console
DATA1
```
## Q9 `gate_7_exceptions` / `layer_b_quiz`

```python
try:
    x = int('5')
    y = 10 / 0
except ValueError:
    print('ValueError')
except ZeroDivisionError:
    print('ZeroDivisionError')

What prints?
```

### Answer:

```console
ZeroDivisionError
```
## Q10 `gate_3_lists_slicing` / `layer_c_speedrun`

```python
a = [1, 2, 3]
print(5 in a)

What prints?
```

### Answer:

```console
False
```
## Q11 `gate_3_lists_slicing` / `layer_a`

```python
a = [1, 2, 3]
a.insert(1, 99)
print(a)

What prints?
```

### Answer:

```console
[1, 99, 2, 3]
```
## Q12 `gate_6_files_io` / `layer_c_speedrun`

```python
with open('f.txt', 'w') as f:
    f.writelines(['a\n', 'b\n'])

What's in file?
```

### Answer:

```console
a
b

```
## Q13 `gate_6_files_io` / `layer_c_speedrun`

```python
with open('f.txt', 'w') as f:
    f.write(str(0))
with open('f.txt') as f:
    print(f.read())

What prints?
```

### Answer:

```console
0
```
## Q14 `gate_8_modules_packages` / `layer_b_predict`

```python
from math import sqrt
print(math.sqrt(16))

Does this work?
```

### Answer:

```console
no, math is not in the namespace
```
## Q15 `gate_8_modules_packages` / `layer_c_speedrun`

```python
import os
print(type(os.path))

What prints?
```

### Answer:

```console
<class 'list'>
```
## Q16 `gate_8_modules_packages` / `layer_b_predict`

```python
import random
random.seed(42)
a = random.randint(1, 10)
random.seed(42)
b = random.randint(1, 10)
print(a == b)

What prints?
```

### Answer:

```console
True
```
## Q17 `gate_7_exceptions` / `layer_c_speedrun`

```python
Can you have try/finally without except?
```

### Answer:

```console
yes
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
## Q19 `gate_8_modules_packages` / `layer_b_predict`

```python
import math as m
print(m.floor(3.7))

What prints?
```

### Answer:

```console
3
```
## Q20 `gate_7_exceptions` / `layer_b_quiz`

```python
data = [1, 2, 'three']
errors = 0
for item in data:
    try:
        int(item)
    except ValueError:
        errors += 1
print(errors)

What prints?
```

### Answer:

```console
1
```
## Q21 `gate_3_lists_slicing` / `layer_a`

```python
a = [1, 2, 3]
a.insert(len(a), 4)
print(a)

What prints?
```

### Answer:

```console
[1, 2, 3, 4]
```
## Q22 `gate_8_modules_packages` / `layer_b_predict`

```python
# In main.py
print(__name__)

When run directly, what prints?
```

### Answer:

```console
main
```
## Q23 `gate_7_exceptions` / `layer_c_speedrun`

```python
try:
    raise ValueError('test')
except ValueError as e:
    print(type(e))

What prints?
```

### Answer:

```console
test
```
## Q24 `gate_3_lists_slicing` / `layer_c_speedrun`

```python
a = [1, 2, 3]
print(2 in a)

What prints?
```

### Answer:

```console
True
```
## Q25 `gate_4_tuples_sets` / `layer_c_speedrun`

```python
a, *b = (1, 2, 3)
print(a, b)

What prints?
```

### Answer:

```console
1 [2, 3]
```
---

## Answers

**Q1:** `True`  
**Q2:** `[1, 2, 3]`  
**Q3:** `5`  
**Q4:** `3 3`  
**Q5:** `{1}`  
**Q6:** `{0: 0, 1: 1, 2: 4, 3: 9}`  
**Q7:** `Error`  
**Q8:** `DATA1`  
**Q9:** `ZeroDivisionError`  
**Q10:** `False`  
**Q11:** `[1, 99, 2, 3]`  
**Q12:** `a\nb\n`  
**Q13:** `0`  
**Q14:** `No (NameError: math not defined)`  
**Q15:** `<class 'module'>`  
**Q16:** `True`  
**Q17:** `Yes (for cleanup code without catching exceptions)`  
**Q18:** `DATA2`  
**Q19:** `3`  
**Q20:** `1`  
**Q21:** `[1, 2, 3, 4]`  
**Q22:** `__main__`  
**Q23:** `<class 'ValueError'>`  
**Q24:** `True`  
**Q25:** `1 [2, 3]`  
