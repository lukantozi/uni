# Python Quiz

**50 questions** | Generated: 2026-02-12 14:13
**45/50 Qs: 1, 22, 28, 29, 30

---

## Q1 `gate_7_exceptions` / `layer_c_speedrun`

```python
try:
    raise ValueError('test')
except ValueError as e:
    print(type(e))

What prints?
```

### Answer:

```console
Exception -> wrong. correction: <class 'ValueError'>
```
## Q2 `gate_6_files_io` / `layer_b`

```python
# file: 'a\nb\nc\n'
with open('f.txt') as f:
    count = 0
    for line in f:
        count += 1
print(count)

What prints?
```

### Answer:

```console
3
```
## Q3 `gate_3_lists_slicing` / `layer_c_speedrun`

```python
a = [1, 2, 3]
x = a.pop()
y = a.pop(0)
print(a, x, y)

What prints?
```

### Answer:

```console
[2] 3 1
```
## Q4 `gate_7_exceptions` / `layer_c_speedrun`

```python
try:
    x = []
    x.nonexistent()
except AttributeError:
    print('AttributeError')

What prints?
```

### Answer:

```console
AttributeError
```
## Q5 `gate_6_files_io` / `layer_c_speedrun`

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
## Q6 `gate_6_files_io` / `layer_b`

```python
with open('f.txt', 'w') as f:
    pass

What's in file?
```

### Answer:

```console
nothing -> better way to say is Empty file (according to claude, but question asks what's in file, and i believe the answer is nothing, as the file is empty)
```
## Q7 `gate_4_tuples_sets` / `layer_a`

```python
t = tuple('abc')
print(t)

What prints?
```

### Answer:

```console
('a', 'b', 'c')
```
## Q8 `gate_3_lists_slicing` / `layer_b_nested`

```python
a = [1, 2, 3]
b = a
a = a + [4]
print(b)

What prints?
```

### Answer:

```console
[1, 2, 3]
```
## Q9 `gate_8_modules_packages` / `layer_a_quiz`

```python
import math
print(math.sqrt(16))

What prints?
```

### Answer:

```console
4.0
```
## Q10 `gate_6_files_io` / `layer_c_speedrun`

```python
with open('f.txt', 'w') as f:
    f.write('test')
    f.write('data')

What's in the file?
```

### Answer:

```console
testdata
```
## Q11 `gate_7_exceptions` / `layer_b_quiz`

```python
numbers = ['1', '2', 'three']
for n in numbers:
    try:
        print(int(n))
    except ValueError:
        print('Skip')

What prints?
```

### Answer:

```console
1
2
Skip
```
## Q12 `gate_7_exceptions` / `layer_a_quiz`

```python
try:
    x = int('abc')
except ValueError:
    print('Invalid')

What prints?
```

### Answer:

```console
Invalid
```
## Q13 `gate_4_tuples_sets` / `layer_a`

```python
s1 = {1, 2, 3}
s2 = {1, 2, 3}
print(s1 == s2)

What prints?
```

### Answer:

```console
True
```
## Q14 `gate_4_tuples_sets` / `layer_b`

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
## Q15 `gate_5_list_comprehensions` / `layer_a`

```python
[[i for i in range(3)] for j in range(2)]

What is the result?
```

### Answer:

```console
[[0, 1, 2], [0, 1, 2]]
```
## Q16 `gate_4_tuples_sets` / `layer_b`

```python
t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)

What prints?
```

### Answer:

```console
(1, 2, 3, 4)
```
## Q17 `gate_3_lists_slicing` / `layer_c_speedrun`

```python
a = [1, 2]
b = [3, 4]
print(a + b)

What prints?
```

### Answer:

```console
[1, 2, 3, 4]
```
## Q18 `gate_6_files_io` / `layer_c_speedrun`

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
## Q19 `gate_7_exceptions` / `layer_b_quiz`

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
## Q20 `gate_5_list_comprehensions` / `layer_a`

```python
[len(x) for x in ['a', 'bb', 'ccc']]

What is the result?
```

### Answer:

```console
[1, 2, 3]
```
## Q21 `gate_7_exceptions` / `layer_b_quiz`

```python
try:
    x = []
    x[0]
except (IndexError, KeyError) as e:
    print('Caught')

What prints?
```

### Answer:

```console
Caught
```
## Q22 `gate_6_files_io` / `layer_a`

```python
f = open('missing.txt', 'r')

What exception is raised?
```

### Answer:

```console
FileNotFound -> wrong. correction: FileNotFoundError
```
## Q23 `gate_6_files_io` / `layer_c_speedrun`

```python
with open('f.txt', 'w') as f:
    f.write('hello')
with open('f.txt') as f:
    print(len(f.read()))

What prints?
```

### Answer:

```console
5
```
## Q24 `gate_8_modules_packages` / `layer_c_speedrun`

```python
import math
print('pi' in dir(math))

What prints?
```

### Answer:

```console
True
```
## Q25 `gate_8_modules_packages` / `layer_c_speedrun`

```python
import sys
print(type(sys.path))

What prints?
```

### Answer:

```console
<class 'list'>
```
## Q26 `gate_5_list_comprehensions` / `layer_a`

```python
sentence = 'hello world'
[len(w) for w in sentence.split()]

What is the result?
```

### Answer:

```console
[5, 5]
```
## Q27 `gate_8_modules_packages` / `layer_b_predict`

```python
import random
print(random.random() >= 0 and random.random() <= 1)

What prints?
```

### Answer:

```console
True
```
## Q28 `gate_5_list_comprehensions` / `layer_a`

```python
[x % 2 for x in [1, 2, 3, 4]]

What is the result?
```

### Answer:

```console
[0, 0, 1, 0] -> [1, 0, 1, 0]
```
## Q29 `gate_4_tuples_sets` / `layer_a`

```python
s = {1, 2}
s.update([3, 4])
print(s)

What prints?
```

### Answer:

```console
{3, 4} # -> checked and it's {1, 2, 3, 4} (i got this wrong)
```
## Q30 `gate_3_lists_slicing` / `layer_a`

```python
a = [1, 2, 3]
a.insert(len(a), 4)
print(a)

What prints?
```

### Answer:

```console
IndexError (len(a) is 3, and index 3 is out of range) -> wrong. correction: [1, 2, 3, 4]
```
## Q31 `gate_6_files_io` / `layer_c_speedrun`

```python
with open('f.txt', 'w') as f:
    f.write('example')
with open('f.txt') as f:
    print(len(f.read()))

What prints?
```

### Answer:

```console
7
```
## Q32 `gate_3_lists_slicing` / `layer_a`

```python
a = [1, 2, 3, 4, 5]
print(a[::2])

What prints?
```

### Answer:

```console
[1, 3, 5]
```
## Q33 `gate_4_tuples_sets` / `layer_a`

```python
s = set([1, 2, 3])
print(s)

What prints?
```

### Answer:

```console
{1, 2, 3}
```
## Q34 `gate_3_lists_slicing` / `layer_c_speedrun`

```python
a = [1, 2, 3]
print(a + a)

What prints?
```

### Answer:

```console
[1, 2, 3, 1, 2, 3]
```
## Q35 `gate_6_files_io` / `layer_b`

```python
with open('f.txt', 'w') as f:
    f.write('first')
with open('f.txt', 'a') as f:
    f.write('second')

What's in the file?
```

### Answer:

```console
firstsecond
```
## Q36 `gate_7_exceptions` / `layer_b_quiz`

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
Error (because of ValueError)
```
## Q37 `gate_3_lists_slicing` / `layer_c_speedrun`

```python
a = [3, 1, 4, 1, 5]
a.sort()
print(a)

What prints?
```

### Answer:

```console
[1, 1, 3, 4, 5]
```
## Q38 `gate_3_lists_slicing` / `layer_c_speedrun`

```python
a = [1, 2]
print(a * 2)

What prints?
```

### Answer:

```console
[1, 2, 1, 2]
```
## Q39 `gate_4_tuples_sets` / `layer_a`

```python
s = {1, 2, 3}
s.add(4)
print(s)

What prints?
```

### Answer:

```console
{1, 2, 3, 4}
```
## Q40 `gate_7_exceptions` / `layer_b_quiz`

```python
try:
    x = int('100')
    y = x / 0
except ValueError:
    print('V')
except ZeroDivisionError:
    print('Z')

What prints?
```

### Answer:

```console
Z
```
## Q41 `gate_3_lists_slicing` / `layer_a`

```python
a = [0, 1, 2, 3, 4]
print(a[-2])

What prints?
```

### Answer:

```console
3
```
## Q42 `gate_4_tuples_sets` / `layer_c_speedrun`

```python
t = (1, 2, 3)
print(1 in t)

What prints?
```

### Answer:

```console
True
```
## Q43 `gate_6_files_io` / `layer_c_speedrun`

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
## Q44 `gate_8_modules_packages` / `layer_c_speedrun`

```python
import math
print(math.ceil(5.1))

What prints?
```

### Answer:

```console
6
```
## Q45 `gate_6_files_io` / `layer_b`

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
## Q46 `gate_3_lists_slicing` / `layer_b_nested`

```python
a = [[1, 2], [3, 4]]
b = a[:]
a.append([5, 6])
print(b)

What prints?
```

### Answer:

```console
[[1, 2], [3, 4]]
```
## Q47 `gate_8_modules_packages` / `layer_b_predict`

```python
from random import choice
data = [1, 2, 3]
print(choice(data) in data)

What prints?
```

### Answer:

```console
True
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
## Q49 `gate_8_modules_packages` / `layer_c_speedrun`

```python
from math import pi
print(pi > 3.14)

What prints?
```

### Answer:

```console
True
```
## Q50 `gate_4_tuples_sets` / `layer_a`

```python
s = {1, 2, 3}
print(len(s))

What prints?
```

### Answer:

```console
3
```
---

## Answers

**Q1:** `<class 'ValueError'>`  
**Q2:** `3`  
**Q3:** `[2] 3 1`  
**Q4:** `AttributeError`  
**Q5:** `DATA1`  
**Q6:** `Empty file`  
**Q7:** `('a', 'b', 'c')`  
**Q8:** `[1, 2, 3]`  
**Q9:** `4.0`  
**Q10:** `testdata`  
**Q11:** `1\n2\nSkip`  
**Q12:** `Invalid`  
**Q13:** `True`  
**Q14:** `{1, 2, 3}`  
**Q15:** `[[0, 1, 2], [0, 1, 2]]`  
**Q16:** `(1, 2, 3, 4)`  
**Q17:** `[1, 2, 3, 4]`  
**Q18:** `a\nb\n`  
**Q19:** `ZeroDivisionError`  
**Q20:** `[1, 2, 3]`  
**Q21:** `Caught`  
**Q22:** `FileNotFoundError`  
**Q23:** `5`  
**Q24:** `True`  
**Q25:** `<class 'list'>`  
**Q26:** `[5, 5]`  
**Q27:** `True`  
**Q28:** `[1, 0, 1, 0]`  
**Q29:** `{1, 2, 3, 4}`  
**Q30:** `[1, 2, 3, 4]`  
**Q31:** `7`  
**Q32:** `[1, 3, 5]`  
**Q33:** `{1, 2, 3}`  
**Q34:** `[1, 2, 3, 1, 2, 3]`  
**Q35:** `firstsecond`  
**Q36:** `Error`  
**Q37:** `[1, 1, 3, 4, 5]`  
**Q38:** `[1, 2, 1, 2]`  
**Q39:** `{1, 2, 3, 4}`  
**Q40:** `Z`  
**Q41:** `3`  
**Q42:** `True`  
**Q43:** `ABC`  
**Q44:** `6`  
**Q45:** `['a', 'b', 'c']`  
**Q46:** `[[1, 2], [3, 4]]`  
**Q47:** `True`  
**Q48:** `{1, 2, 3}`  
**Q49:** `True`  
**Q50:** `3`  
