# Python Quiz

**50 questions** | Generated: 2026-02-12 16:14

---

## Q1 `gate_6_files_io` / `layer_c_speedrun`

```python
with open('f.txt', 'w') as f:
    f.write('a\nb\nc')
with open('f.txt', 'r') as f:
    lines = f.readlines()
print(len(lines))

What prints?
```

### Answer:

```console
3
```
## Q2 `gate_6_files_io` / `layer_b`

```python
# file1.txt: 'a\nb\nc'
# file2.txt: '1\n2\n3'
with open('f1.txt') as f1, open('f2.txt') as f2:
    for line1, line2 in zip(f1, f2):
        print(line1.strip(), line2.strip())

What's the approach?
```

### Answer:

```console
loop will run as long as there are lines left in either of the file and combine them, as long as one file reaches the end the loop will stop
```
## Q3 `gate_6_files_io` / `layer_c_speedrun`

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
## Q4 `gate_8_modules_packages` / `layer_c_speedrun`

```python
from math import pi
print(pi > 3.14)

What prints?
```

### Answer:

```console
True
```
## Q5 `gate_6_files_io` / `layer_b`

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
## Q6 `gate_6_files_io` / `layer_b`

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
## Q7 `gate_7_exceptions` / `layer_c_speedrun`

```python
try:
    x = {'a': 1}['b']
except KeyError as e:
    print(e)

What prints?
```

### Answer:

```console
KeyError (and whatever comes after that)
```
## Q8 `gate_6_files_io` / `layer_c_speedrun`

```python
# file contains 5 lines
with open('f.txt', 'r') as f:
    count = len(f.readlines())
print(count)

What prints?
```

### Answer:

```console
5
```
## Q9 `gate_6_files_io` / `layer_b`

```python
with open('f.txt', 'w') as f:
    f.write('line1')
    f.write('\n')
    f.write('line2')

What's in file?
```

### Answer:

```console
line1\nline2

or

line1
line2
```
## Q10 `gate_7_exceptions` / `layer_c_speedrun`

```python
try:
    x = None
    x.append(1)
except AttributeError:
    print('AttributeError')

What prints?
```

### Answer:

```console
AttributeError
```
## Q11 `gate_7_exceptions` / `layer_c_speedrun`

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
## Q12 `gate_6_files_io` / `layer_c_speedrun`

```python
with open('f.txt', 'w') as f:
    f.write('file')
with open('f.txt') as f:
    print(len(f.read()))

What prints?
```

### Answer:

```console
4
```
## Q13 `gate_7_exceptions` / `layer_a_quiz`

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print('Error')

What prints?
```

### Answer:

```console
Error
```
## Q14 `gate_8_modules_packages` / `layer_b_predict`

```python
from math import sqrt
print(math.sqrt(16))

Does this work?
```

### Answer:

```console
no, math is not reserved in namespace, will raise NameError
```
## Q15 `gate_6_files_io` / `layer_c_speedrun`

```python
with open('f.txt', 'a+') as f:
    f.write('test')

What mode combines append and read?
```

### Answer:

```console
'a+'
```
## Q16 `gate_7_exceptions` / `layer_b_quiz`

```python
try:
    raise ValueError('test')
except ValueError:
    print('V')
else:
    print('E')
finally:
    print('F')

What prints?
```

### Answer:

```console
V
F
```
## Q17 `gate_8_modules_packages` / `layer_b_predict`

```python
import os
print('path' in dir(os))

What prints?
```

### Answer:

```console
True
```
## Q18 `gate_6_files_io` / `layer_c_speedrun`

```python
with open('f.txt', 'w') as f:
    f.write('code')
with open('f.txt') as f:
    print(len(f.read()))

What prints?
```

### Answer:

```console
4
```
## Q19 `gate_8_modules_packages` / `layer_b_predict`

```python
# In main.py
print(__name__)

When run directly, what prints?
```

### Answer:

```console
__main__
```
## Q20 `gate_7_exceptions` / `layer_b_quiz`

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
## Q21 `gate_6_files_io` / `layer_c_speedrun`

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
## Q22 `gate_6_files_io` / `layer_b`

```python
with open('f.txt', 'w') as f1:
    with open('f2.txt', 'w') as f2:
        f1.write('A')
        f2.write('B')

How many files created?
```

### Answer:

```console
two, each containing A and B respectively
```
## Q23 `gate_8_modules_packages` / `layer_c_speedrun`

```python
import math
print(math.sqrt(25))

What prints?
```

### Answer:

```console
5
```
## Q24 `gate_8_modules_packages` / `layer_b_predict`

```python
import os
print(os.path.exists('.'))

What prints?
```

### Answer:

```console
True
```
## Q25 `gate_6_files_io` / `layer_c_speedrun`

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
## Q26 `gate_8_modules_packages` / `layer_b_concept`

```python
How do you check if a module has an attribute?
```

### Answer:

```console
hasattr(module, attribute)
```
## Q27 `gate_6_files_io` / `layer_a`

```python
# file.txt contains:
# 12
# 20 31
# 42
with open('file.txt', 'r') as f:
    lines = f.readlines()

What type is lines?
```

### Answer:

```console
<class 'list'>
```
## Q28 `gate_7_exceptions` / `layer_b_quiz`

```python
def safe_convert(s):
    try:
        return int(s)
    except ValueError:
        return 0

print(safe_convert('123'))

What prints?
```

### Answer:

```console
123
```
## Q29 `gate_6_files_io` / `layer_c_speedrun`

```python
with open('f.txt', 'w') as f:
    f.write(str(2))
with open('f.txt') as f:
    print(f.read())

What prints?
```

### Answer:

```console
2
```
## Q30 `gate_8_modules_packages` / `layer_a_quiz`

```python
import math
print(math.sqrt(16))

What prints?
```

### Answer:

```console
4.0
```
## Q31 `gate_7_exceptions` / `layer_c_speedrun`

```python
try:
    x = len(None)
except TypeError:
    print('TypeError')

What prints?
```

### Answer:

```console
TypeError
```
## Q32 `gate_8_modules_packages` / `layer_c_speedrun`

```python
import math
print(hasattr(math, 'sqrt'))

What prints?
```

### Answer:

```console
True
```
## Q33 `gate_7_exceptions` / `layer_c_speedrun`

```python
What's the purpose of finally block?
```

### Answer:

```console
do run it anyway
```
## Q34 `gate_6_files_io` / `layer_b`

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
## Q35 `gate_6_files_io` / `layer_c_speedrun`

```python
# file: 'test'
with open('f.txt') as f:
    print(f.read().upper())

What prints?
```

### Answer:

```console
TEST
```
## Q36 `gate_6_files_io` / `layer_c_speedrun`

```python
# file: '1\n2\n3'
with open('f.txt') as f:
    lines = [l.rstrip() for l in f]
print(lines)

What prints?
```

### Answer:

```console
['1', '2', '3']
```
## Q37 `gate_6_files_io` / `layer_c_speedrun`

```python
# file: '123'
with open('f.txt') as f:
    print(f.read().isdigit())

What prints?
```

### Answer:

```console
True
```
## Q38 `gate_6_files_io` / `layer_c_speedrun`

```python
with open('f.txt', 'w') as f:
    f.write('test2')
with open('f.txt') as f:
    print(f.read().upper())

What prints?
```

### Answer:

```console
TEST2
```
## Q39 `gate_6_files_io` / `layer_c_speedrun`

```python
with open('f.txt', 'w') as f:
    print('hello', file=f)

What's in the file?
```

### Answer:

```console
hello
```
## Q40 `gate_6_files_io` / `layer_c_speedrun`

```python
with open('f.txt', 'w') as f:
    f.write('python')
with open('f.txt') as f:
    print(len(f.read()))

What prints?
```

### Answer:

```console
6
```
## Q41 `gate_7_exceptions` / `layer_c_speedrun`

```python
What exception for trying to convert non-numeric string to int?
```

### Answer:

```console
ValueError
```
## Q42 `gate_7_exceptions` / `layer_b_quiz`

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
## Q43 `gate_7_exceptions` / `layer_c_speedrun`

```python
What exception for accessing attribute that doesn't exist?
```

### Answer:

```console
AttributeError
```
## Q44 `gate_8_modules_packages` / `layer_c_speedrun`

```python
from math import sqrt, pow
print(pow(2, 3))

What prints?
```

### Answer:

```console
8.0
```
## Q45 `gate_8_modules_packages` / `layer_b_predict`

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
## Q46 `gate_7_exceptions` / `layer_c_speedrun`

```python
try:
    raise ValueError('test')
except ValueError as e:
    print(type(e))

What prints?
```

### Answer:

```console
<class 'ValueError'>
```
## Q47 `gate_8_modules_packages` / `layer_c_speedrun`

```python
import math
print('pi' in dir(math))

What prints?
```

### Answer:

```console
True
```
## Q48 `gate_6_files_io` / `layer_c_speedrun`

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
## Q49 `gate_6_files_io` / `layer_c_speedrun`

```python
with open('f.txt', 'w') as f:
    f.write('test1')
with open('f.txt') as f:
    print(f.read().upper())

What prints?
```

### Answer:

```console
TEST1
```
## Q50 `gate_7_exceptions` / `layer_c_speedrun`

```python
What's the purpose of else block in try/except?
```

### Answer:

```console
to run the code if there are no errors after trying to catch them
```
---

## Answers

**Q1:** `3`  
**Q2:** `Combines corresponding lines from both files`  
**Q3:** `testdata`  
**Q4:** `True`  
**Q5:** `0`  
**Q6:** `['a', 'b', 'c']`  
**Q7:** `'b'`  
**Q8:** `5`  
**Q9:** `line1\nline2`  
**Q10:** `AttributeError`  
**Q11:** `Wrong`  
**Q12:** `4`  
**Q13:** `Error`  
**Q14:** `No (NameError: math not defined)`  
**Q15:** `a+`  
**Q16:** `V\nF`  
**Q17:** `True`  
**Q18:** `4`  
**Q19:** `__main__`  
**Q20:** `Error`  
**Q21:** `DATA1`  
**Q22:** `2`  
**Q23:** `5.0`  
**Q24:** `True`  
**Q25:** `a\nb\n`  
**Q26:** `hasattr(module, 'attribute_name') or 'attribute_name' in dir(module)`  
**Q27:** `list`  
**Q28:** `123`  
**Q29:** `2`  
**Q30:** `4.0`  
**Q31:** `TypeError`  
**Q32:** `True`  
**Q33:** `Always runs, whether exception occurred or not (cleanup code)`  
**Q34:** `2`  
**Q35:** `TEST`  
**Q36:** `['1', '2', '3']`  
**Q37:** `True`  
**Q38:** `TEST2`  
**Q39:** `hello\n`  
**Q40:** `6`  
**Q41:** `ValueError`  
**Q42:** `ZeroDivisionError`  
**Q43:** `AttributeError`  
**Q44:** `8.0`  
**Q45:** `7.0`  
**Q46:** `<class 'ValueError'>`  
**Q47:** `True`  
**Q48:** `0`  
**Q49:** `TEST1`  
**Q50:** `Runs only if no exception was raised in try block`  
