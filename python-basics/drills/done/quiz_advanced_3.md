# Python Quiz

**25 questions** | Generated: 2026-02-12 15:52

---

## Q1 `gate_4_tuples_sets` / `layer_a`

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
## Q2 `gate_8_modules_packages` / `layer_c_speedrun`

```python
import math
print(math.sqrt(25))

What prints?
```

### Answer:

```console
5
```
## Q3 `gate_6_files_io` / `layer_a`

```python
# file.txt contains:
# line1
# line2
with open('file.txt', 'r') as f:
    line = f.readline()

What does line contain?
```

### Answer:

```console
line1 -> line1\n
```
## Q4 `gate_5_list_comprehensions` / `layer_a`

```python
[[i for i in range(3)] for j in range(2)]

What is the result?
```

### Answer:

```console
[[0, 1, 2], [0, 1, 2]]
```
## Q5 `gate_4_tuples_sets` / `layer_b`

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
## Q6 `gate_4_tuples_sets` / `layer_b`

```python
a, b, c = 'abc'
print(a, b, c)

What prints?
```

### Answer:

```console
a b c
```
## Q7 `gate_7_exceptions` / `layer_c_speedrun`

```python
What exception for accessing attribute that doesn't exist?
```

### Answer:

```console
AttributeError
```
## Q8 `gate_8_modules_packages` / `layer_b_concept`

```python
from module import *

Is this recommended?
```

### Answer:

```console
no
```
## Q9 `gate_5_list_comprehensions` / `layer_a`

```python
[x*2 for x in [1, 2, 3]]

What is the result?
```

### Answer:

```console
[2, 4, 6]
```
## Q10 `gate_7_exceptions` / `layer_c_speedrun`

```python
What's the purpose of finally block?
```

### Answer:

```console
to run the code in the block regardless of what happens in above blocks
```
## Q11 `gate_6_files_io` / `layer_c_speedrun`

```python
# file: '1\n2\n3'
with open('f.txt') as f:
    lines = [l.rstrip() for l in f]
print(lines)

What prints?
```

### Answer:

```console
['1\n', '2\n', '3']
```
## Q12 `gate_6_files_io` / `layer_a`

```python
with open('test.txt', 'w') as f:
    f.write('hello')

Do you need to call f.close()?
```

### Answer:

```console
no
```
## Q13 `gate_3_lists_slicing` / `layer_c_speedrun`

```python
a = [1, 2, 3]
a.extend([4, 5])
print(a)

What prints?
```

### Answer:

```console
[1, 2, 3, 4, 5]
```
## Q14 `gate_6_files_io` / `layer_c_speedrun`

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
## Q15 `gate_8_modules_packages` / `layer_b_predict`

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
## Q16 `gate_8_modules_packages` / `layer_b_concept`

```python
Can you import the same module with different names?
```

### Answer:

```console
no -> checked and we can (counts as wrong)
```
## Q17 `gate_7_exceptions` / `layer_b_quiz`

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
## Q18 `gate_3_lists_slicing` / `layer_c_speedrun`

```python
a = [1, 2, 3, 4, 5]
print(a[::1])

What prints?
```

### Answer:

```console
[1, 2, 3, 4, 5]
```
## Q19 `gate_4_tuples_sets` / `layer_a`

```python
s = {1, 2, 3}
print(2 in s)

What prints?
```

### Answer:

```console
True
```
## Q20 `gate_5_list_comprehensions` / `layer_a`

```python
[x for x in range(10) if x % 3 == 0]

What is the result?
```

### Answer:

```console
[0, 3, 6, 9]
```
## Q21 `gate_7_exceptions` / `layer_b_quiz`

```python
try:
    x = 5
except:
    print('E')
else:
    print('OK')
finally:
    print('F')

What prints?
```

### Answer:

```console
OK
F
```
## Q22 `gate_6_files_io` / `layer_c_speedrun`

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
## Q23 `gate_4_tuples_sets` / `layer_a`

```python
t = (1)
print(type(t))

What prints?
```

### Answer:

```console
<class 'int'>
```
## Q24 `gate_3_lists_slicing` / `layer_c_speedrun`

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

## Q25 `gate_6_files_io` / `layer_c_speedrun`

```python
with open('f.txt', 'w') as f:
    f.write('hello world')
with open('f.txt', 'r') as f:
    chars = f.read(3)
print(chars)

What prints?
```

### Answer:

```console
hel
```
---

## Answers

**Q1:** `{1, 2, 3, 4}`  
**Q2:** `5.0`  
**Q3:** `First line including newline character (if present)`  
**Q4:** `[[0, 1, 2], [0, 1, 2]]`  
**Q5:** `{1, 2, 3}`  
**Q6:** `a b c`  
**Q7:** `AttributeError`  
**Q8:** `No (pollutes namespace; unclear what names are imported)`  
**Q9:** `[2, 4, 6]`  
**Q10:** `Always runs, whether exception occurred or not (cleanup code)`  
**Q11:** `['1', '2', '3']`  
**Q12:** `No (with statement handles it automatically)`  
**Q13:** `[1, 2, 3, 4, 5]`  
**Q14:** `TEST1`  
**Q15:** `True`  
**Q16:** `Yes (import math; import math as m)`  
**Q17:** `1`  
**Q18:** `[1, 2, 3, 4, 5]`  
**Q19:** `True`  
**Q20:** `[0, 3, 6, 9]`  
**Q21:** `OK\nF`  
**Q22:** `0`  
**Q23:** `<class 'int'>`  
**Q24:** `[1, 2, 3, 4]`  
**Q25:** `hel`  
