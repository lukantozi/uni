# Python Quiz

**50 questions** | Generated: 2026-02-12 12:37
**43/50 Qs: 1, 4, 8, 9, 19, 20, 43**

---

## Q1 `gate_7_exceptions` / `layer_b_quiz`

```python
try:
    x = [1, 2, 3]
    print(x[2])
except (IndexError, KeyError):
    print('Caught')

What prints?
```

### Answer:

```console
Caught -> 3
```
## Q2 `gate_7_exceptions` / `layer_a_quiz`

```python
try:
    x = 10 / 0
except:
    print('Caught')

What prints?
```

### Answer:

```console
Caught
```
## Q3 `gate_7_exceptions` / `layer_c_speedrun`

```python
try:
    raise ValueError('test')
except ValueError:
    print('Caught')

What prints?
```

### Answer:

```console
Caught
```
## Q4 `gate_4_tuples_sets` / `layer_b`

```python
t = (1, 2, 3, 4, 5)
a, b, c = t
print(a, b, c)
```

### Answer:

```console
too many items to unpack -> ValueError
```
## Q5 `gate_5_list_comprehensions` / `layer_a`

```python
[x**2 for x in range(5)]
```

### Answer:

```console
[0, 1, 4, 9, 16]
```
## Q6 `gate_3_lists_slicing` / `layer_b_nested`

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
## Q7 `gate_3_lists_slicing` / `layer_c_speedrun`

```python
a = [1, 2, 3]
b = a
a = a + [4]
print(b)
```

### Answer:

```console
[1, 2, 3]
```
## Q8 `gate_4_tuples_sets` / `layer_c_speedrun`

```python
a, *b, c = [1, 2, 3, 4, 5]
print(a, b, c)
```

### Answer:

```console
1, [2, 3, 4], 5 -> 1 [2, 3, 4] 5
```
## Q9 `gate_8_modules_packages` / `layer_c_speedrun`

```python
What's __name__ when module is imported?
```

### Answer:

```console
__main__ -> wrong, it is modules name
```
## Q10 `gate_3_lists_slicing` / `layer_c_speedrun`

```python
a = [1, 2, 3, 4, 5]
print(a[1::-1])
```

### Answer:

```console
[2, 1]
```
## Q11 `gate_7_exceptions` / `layer_a_quiz`

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
## Q12 `gate_8_modules_packages` / `layer_b_concept`

```python
What's a standard library vs third-party library?
```

### Answer:

```console
standard library is a built in library, and third-part is outside library developed by other devs outside of official python libs
```
## Q13 `gate_4_tuples_sets` / `layer_c_speedrun`

```python
*a, b = [1, 2, 3, 4]
print(a, b)
```

### Answer:

```console
[1, 2, 3] 4
```
## Q14 `gate_8_modules_packages` / `layer_b_concept`

```python
What's the difference between a module and a package?
```

### Answer:

```console
module is a file of methods/items and package is a folder consisting of modules
```
## Q15 `gate_7_exceptions` / `layer_b_quiz`

```python
try:
    pass
finally:
    print('Finally runs')

What prints?
```

### Answer:

```console
Finally runs
```
## Q16 `gate_8_modules_packages` / `layer_b_predict`

```python
import sys
print(type(sys.path))

What prints?
```

### Answer:

```console
<class 'list'>
```
## Q17 `gate_5_list_comprehensions` / `layer_a`

```python
[x if x > 0 else 0 for x in [1, -2, 3, -4]]
```

### Answer:

```console
[1, 0, 3, 0]
```
## Q18 `gate_7_exceptions` / `layer_a_quiz`

```python
try:
    x = [1, 2, 3]
    print(x[5])
except IndexError:
    print('Out of range')

What prints?
```

### Answer:

```console
Out of range
```
## Q19 `gate_7_exceptions` / `layer_b_quiz`

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
5 -> wrong. correct: nothing, as 5 is just returned but not printed
```
## Q20 `gate_3_lists_slicing` / `layer_b_nested`

```python
a = [[1, 2], [3, 4]]
a[0] = 99
print(a)
```

### Answer:

```console
[[99], [3, 4]] -> [99, [3, 4]] 
```
## Q21 `gate_3_lists_slicing` / `layer_a`

```python
a = [1, 2, 3]
a.insert(1, 99)
print(a)
```

### Answer:

```console
[1, 99, 2, 3]
```
## Q22 `gate_8_modules_packages` / `layer_b_concept`

```python
Can you import a module multiple times? Does it re-execute?
```

### Answer:

```console
you can; it does not
```
## Q23 `gate_3_lists_slicing` / `layer_a`

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
## Q24 `gate_8_modules_packages` / `layer_b_predict`

```python
import os
print(os.getcwd())

What does this return?
```

### Answer:

```console
current directory path
```
## Q25 `gate_4_tuples_sets` / `layer_a`

```python
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1 & s2)
```

### Answer:

```console
{3}
```
## Q26 `gate_3_lists_slicing` / `layer_b_nested`

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
## Q27 `gate_3_lists_slicing` / `layer_a`

```python
a = [1, 2, 3, 4, 5]
a.append(6)
print(a)
```

### Answer:

```console
[1, 2, 3, 4, 5, 6]
```
## Q28 `gate_8_modules_packages` / `layer_c_speedrun`

```python
What's __init__.py for?
```

### Answer:

```console
do initialize the directory it is in as a package
```
## Q29 `gate_3_lists_slicing` / `layer_b_nested`

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
## Q30 `gate_4_tuples_sets` / `layer_b`

```python
s = {1, 2, 3}
print(len(s))
```

### Answer:

```console
3
```
## Q31 `gate_8_modules_packages` / `layer_a_quiz`

```python
import math as m
print(m.sqrt(16))

What prints?
```

### Answer:

```console
4.0
```
## Q32 `gate_3_lists_slicing` / `layer_c_speedrun`

```python
a = [1, [2, 3], 4]
print(a[1][1])
```

### Answer:

```console
3
```
## Q33 `gate_3_lists_slicing` / `layer_a`

```python
a = [1, 2, 3, 4, 5]
x = a.pop(2)
print(a, x)
```

### Answer:

```console
[1, 2, 4, 5] 3
```
## Q34 `gate_8_modules_packages` / `layer_b_concept`

```python
What's the difference between import math and from math import sqrt in terms of namespace?
```

### Answer:

```console
in the first example math is reserved in the namespace and in the second one sqrt
```
## Q35 `gate_4_tuples_sets` / `layer_a`

```python
t = (1, 2, 3)
print(t.index(2))
```

### Answer:

```console
1
```
## Q36 `gate_5_list_comprehensions` / `layer_a`

```python
[str(i) for i in range(5)]
```

### Answer:

```console
['0', '1', '2', '3', '4']
```
## Q37 `gate_3_lists_slicing` / `layer_a`

```python
a = [1, 2, 3, 4, 5]
print(a)
```

### Answer:

```console
[1, 2, 3, 4, 5]
```
## Q38 `gate_3_lists_slicing` / `layer_b_nested`

```python
a = [1, 2, 3]
b = [a, a]
a[0] = 99
print(b)
```

### Answer:

```console
[[99, 2, 3], [99, 2, 3]]
```
## Q39 `gate_8_modules_packages` / `layer_c_speedrun`

```python
What's from package import module syntax?
```

### Answer:

```console
from package import module
```
## Q40 `gate_4_tuples_sets` / `layer_b`

```python
t = ((1, 2), (3, 4))
print(t[1])
```

### Answer:

```console
(3, 4)
```
## Q41 `gate_5_list_comprehensions` / `layer_a`

```python
nums = [1, 2, 3, 4]
[x for x in nums if x >= 0]
```

### Answer:

```console
[1, 2, 3, 4]
```
## Q42 `gate_8_modules_packages` / `layer_a_quiz`

```python
from math import floor, ceil
print(floor(3.7), ceil(3.2))

What prints?
```

### Answer:

```console
3 4
```
## Q43 `gate_8_modules_packages` / `layer_c_speedrun`

```python
Can you import from a subdirectory?
```

### Answer:

```console
yes, as long as it's in the __init__.py -> wrong. correct: you can import if the package is on sys.path and the subdirectory is a package
```
## Q44 `gate_5_list_comprehensions` / `layer_a`

```python
[x for x in range(20) if x % 5 == 0]
```

### Answer:

```console
[0, 5, 10, 15]
```
## Q45 `gate_5_list_comprehensions` / `layer_a`

```python
[x*2 for x in [1, 2, 3]]
```

### Answer:

```console
[2, 4, 6]
```
## Q46 `gate_7_exceptions` / `layer_c_speedrun`

```python
What exception for invalid int conversion?
```

### Answer:

```console
ValueError
```
## Q47 `gate_4_tuples_sets` / `layer_b`

```python
s1 = {1, 2}
s2 = {2, 3}
print(s1 * s2)
```

### Answer:

```console
not possible # TypeError
```
## Q48 `gate_5_list_comprehensions` / `layer_a`

```python
[x for x in range(20) if x % 2 == 0]
```

### Answer:

```console
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```
## Q49 `gate_4_tuples_sets` / `layer_a`

```python
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1 | s2)
```

### Answer:

```console
{1, 2, 3, 4, 5}
```
## Q50 `gate_7_exceptions` / `layer_b_quiz`

```python
try:
    x = 10 / 0
except Exception:
    print('Exception')
except ZeroDivisionError:
    print('ZeroDivisionError')

What prints? (Order matters!)
```

### Answer:

```console
Exception
```
---

## Answers

**Q1:** `3`  
**Q2:** `Caught`  
**Q3:** `Caught`  
**Q4:** `ValueError (too many values to unpack)`  
**Q5:** `[0, 1, 4, 9, 16]`  
**Q6:** `[[1, 2], [3, 4]]`  
**Q7:** `[1, 2, 3]`  
**Q8:** `1 [2, 3, 4] 5`  
**Q9:** `Module name (e.g., 'mymodule')`  
**Q10:** `[2, 1]`  
**Q11:** `Invalid`  
**Q12:** `Standard: built-in with Python; third-party: external packages (pip install)`  
**Q13:** `[1, 2, 3] 4`  
**Q14:** `Module is a .py file; package is a directory with __init__.py`  
**Q15:** `Finally runs`  
**Q16:** `<class 'list'>`  
**Q17:** `[1, 0, 3, 0]`  
**Q18:** `Out of range`  
**Q19:** `Nothing (no exception)`  
**Q20:** `[99, [3, 4]]`  
**Q21:** `[1, 99, 2, 3]`  
**Q22:** `Yes you can import multiple times, but it doesn't re-execute (cached)`  
**Q23:** `[1, 2, 3, 4, 5]`  
**Q24:** `Current working directory path`  
**Q25:** `{3}`  
**Q26:** `[[1, 2, 3], [1, 2, 3]]`  
**Q27:** `[1, 2, 3, 4, 5, 6]`  
**Q28:** `Makes directory a package, runs on package import`  
**Q29:** `6`  
**Q30:** `3`  
**Q31:** `4.0`  
**Q32:** `3`  
**Q33:** `[1, 2, 4, 5] 3`  
**Q34:** `import math reserves 'math' namespace; from math import sqrt only reserves 'sqrt'`  
**Q35:** `1`  
**Q36:** `['0', '1', '2', '3', '4']`  
**Q37:** `[1, 2, 3, 4, 5]`  
**Q38:** `[[99, 2, 3], [99, 2, 3]]`  
**Q39:** `Imports specific module from package`  
**Q40:** `(3, 4)`  
**Q41:** `[1, 2, 3, 4]`  
**Q42:** `3 4`  
**Q43:** `Yes, if it has __init__.py (is a package)`  
**Q44:** `[0, 5, 10, 15]`  
**Q45:** `[2, 4, 6]`  
**Q46:** `ValueError`  
**Q47:** `TypeError`  
**Q48:** `[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]`  
**Q49:** `{1, 2, 3, 4, 5}`  
**Q50:** `Exception`  
