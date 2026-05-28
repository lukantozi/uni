# Gate 5 — NumPy

## Layer A — Skeleton
**Pass criteria:** 13/15 predict-output, all coding drills run correctly first try.

### Predict-output drills

**Q1**
```python
import numpy as np
a = np.array([1, 2, 3, 4, 5])
print(a[0])
print(a[-1])
```

**Q2**
```python
import numpy as np
a = np.array([10, 20, 30, 40, 50])
print(a[1:4])
```

**Q3**
```python
import numpy as np
a = np.array([1, 2, 3, 4, 5, 6])
print(a[::2])
```

**Q4**
```python
import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.shape)
print(a.ndim)
```

**Q5**
```python
import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a[0][1])
print(a[1, 2])
```

**Q6**
```python
import numpy as np
a = np.array([1, 2, 3, 4, 5, 6])
b = a.reshape(2, 3)
print(b.shape)
print(b[1, 0])
```

**Q7**
```python
import numpy as np
a = np.array([1, 2, 3, 4, 5, 6])
b = a[2:5]
b[0] = 99
print(a)
```

**Q8**
```python
import numpy as np
a = np.array([1, 2, 3, 4, 5, 6])
b = a[2:5].copy()
b[0] = 99
print(a)
```

**Q9**
```python
import numpy as np
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
print(a + b)
```

**Q10**
```python
import numpy as np
a = np.array([1, 2, 3, 4, 5])
print(np.sum(a))
print(np.mean(a))
```

**Q11**
```python
import numpy as np
a = np.array([3, 1, 4, 1, 5, 9, 2, 6])
print(np.sort(a))
print(a)
```

**Q12**
```python
import numpy as np
a = np.array([1, 2, 3, 4, 5])
print(a[a > 3])
```

**Q13**
```python
import numpy as np
a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30])
print(np.concatenate((a[:2], b)))
```

**Q14**
```python
import numpy as np
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
print(np.vstack((a, b)))
```

**Q15**
```python
import numpy as np
a = np.array([1, 2, 3, 4, 5])
result = np.where(a > 3, 1, 0)
print(result)
```

### Answer table

| Q | Answer |
|---|--------|
| 1 | `1` `5` |
| 2 | `[20 30 40]` |
| 3 | `[1 3 5]` |
| 4 | `(2, 3)` `2` |
| 5 | `2` `6` |
| 6 | `(2, 3)` `4` |
| 7 | `[ 1  2 99  4  5  6]` (slice is a view) |
| 8 | `[1 2 3 4 5 6]` (copy breaks the link) |
| 9 | `[11 22 33]` |
| 10 | `15` `3.0` |
| 11 | `[1 1 2 3 4 5 6 9]` then `[3 1 4 1 5 9 2 6]` (sort returns new array) |
| 12 | `[4 5]` |
| 13 | `[ 1  2 10 20 30]` |
| 14 | `[[1 2]` `[3 4]` `[5 6]]` |
| 15 | `[0 0 0 1 1]` |

### Coding drills — Layer A

**Drill 1**
Create a 1D NumPy array of integers from 0 to 9. Print every other element starting from index 1.

**Drill 2**
Create a 2D array of shape (3, 3) filled with zeros using `np.zeros`. Then set the diagonal elements to 1. Print the result.

**Drill 3**
Create two arrays `a = [1, 2, 3]` and `b = [4, 5, 6]`. Stack them vertically and horizontally. Print both results.

**Drill 4**
Create an array of 10 random integers between 0 and 100 using `np.random.randint`. Print only elements greater than 50.

**Drill 5**
Create an array `[5, 3, 8, 1, 9, 2, 7]`. Sort it. Find and print the max, min, and mean.

---

## Layer B — Variants
**Pass criteria:** 12/14 predict-output, all coding drills run correctly first try.

### Predict-output drills

**Q1**
```python
import numpy as np
a = np.array([1, 2, 3, 4, 5, 6])
b = a
b[0] = 99
print(a[0])
```

**Q2**
```python
import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a[:, 1])
```

**Q3**
```python
import numpy as np
a = np.arange(1, 10).reshape(3, 3)
print(a[1:, 1:])
```

**Q4**
```python
import numpy as np
a = np.array([1, 2, 3])
print(a * 3)
```

**Q5**
```python
import numpy as np
a = np.array([[1, 2], [3, 4]])
print(np.sum(a, axis=0))
print(np.sum(a, axis=1))
```

**Q6**
```python
import numpy as np
a = np.array([1, 2, 3, 4, 5, 6])
b = a.reshape(3, 2)
c = b.reshape(6)
c[0] = 99
print(a[0])
```

**Q7**
```python
import numpy as np
a = np.array([1, 2, 3, 4, 5])
b = np.where(a % 2 == 0, a * 10, a)
print(b)
```

**Q8**
```python
import numpy as np
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(np.hstack((a, b)))
```

**Q9**
```python
import numpy as np
a = np.zeros((2, 3), dtype=int)
a[0] = [1, 2, 3]
print(a)
```

**Q10**
```python
import numpy as np
a = np.array([10, 20, 30])
b = np.array([[1], [2], [3]])
print(a + b)
```

**Q11**
```python
import numpy as np
a = np.array([3, 1, 4, 1, 5])
print(np.unique(a))
```

**Q12**
```python
import numpy as np
a = np.arange(12).reshape(4, 3)
print(a.shape)
print(a[2, 1])
```

**Q13**
```python
import numpy as np
a = np.array([1, 2, 3, 4, 5])
b = a.copy()
b *= 10
print(a)
print(b)
```

**Q14**
```python
import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.flatten())
print(a.shape)
```

### Answer table

| Q | Answer |
|---|--------|
| 1 | `99` (assignment `b = a` is not a copy — same object) |
| 2 | `[2 5 8]` (all rows, column index 1) |
| 3 | `[[5 6]` `[8 9]]` |
| 4 | `[3 6 9]` |
| 5 | `[4 6]` then `[3 7]` |
| 6 | `99` (reshape returns a view — all linked) |
| 7 | `[ 1 20  3 40  5]` |
| 8 | `[[1 2 5 6]` `[3 4 7 8]]` |
| 9 | `[[1 2 3]` `[0 0 0]]` |
| 10 | `[[11 21 31]` `[12 22 32]` `[13 23 33]]` (broadcasting) |
| 11 | `[1 3 4 5]` |
| 12 | `(4, 3)` then `7` |
| 13 | `[1 2 3 4 5]` then `[10 20 30 40 50]` |
| 14 | `[1 2 3 4 5 6]` then `(2, 3)` (flatten returns copy, shape unchanged) |

### Coding drills — Layer B

**Drill 1**
Create a 3x3 identity matrix using `np.eye`. Multiply it element-wise by a scalar 5. Print the result.

**Drill 2**
Create a 4x4 array using `np.arange(16).reshape(4,4)`. Extract the 2x2 subarray from the bottom-right corner. Modify one element and confirm whether the original changed (view vs copy).

**Drill 3**
Create two 2D arrays of shape (2, 3) and (3, 2). Use `np.dot` to multiply them. Print the shape of the result.

**Drill 4**
Create an array `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`. Replace all even numbers with -1 using `np.where`. Print the result.

---

## Layer C — Speed Run
**Target:** 30 questions in under 20 minutes. No notes, no running code.
**Pass criteria:** 27/30

**Q1** `np.array([1,2,3])[1]` → ?
**Q2** `np.array([1,2,3,4,5])[1:4]` → ?
**Q3** `np.array([1,2,3,4,5,6])[::3]` → ?
**Q4** `np.array([[1,2],[3,4]]).shape` → ?
**Q5** `np.array([[1,2],[3,4]]).ndim` → ?
**Q6** `np.array([[1,2],[3,4]])[1,0]` → ?
**Q7** `np.arange(6).reshape(2,3).shape` → ?
**Q8** slice `a[1:3]` of array — view or copy? → ?
**Q9** `a.copy()` — view or copy? → ?
**Q10** `b = a` — view or copy? → ?
**Q11** `np.array([1,2,3]) + np.array([4,5,6])` → ?
**Q12** `np.array([1,2,3]) * 2` → ?
**Q13** `np.sum(np.array([1,2,3,4,5]))` → ?
**Q14** `np.mean(np.array([1,2,3,4,5]))` → ?
**Q15** `np.max(np.array([3,1,4,1,5,9]))` → ?
**Q16** `np.sort(np.array([3,1,2]))` — does it modify original? → ?
**Q17** `np.array([1,2,3,4,5])[np.array([1,2,3,4,5]) > 3]` → ?
**Q18** `np.where(np.array([1,2,3,4,5]) > 3, 1, 0)` → ?
**Q19** `np.vstack((np.array([1,2]), np.array([3,4]))).shape` → ?
**Q20** `np.hstack((np.array([[1],[2]]), np.array([[3],[4]]))).shape` → ?
**Q21** `np.zeros((2,3)).shape` → ?
**Q22** `np.ones((3,3)).ndim` → ?
**Q23** `np.arange(0, 10, 2)` → ?
**Q24** `np.linspace(0, 1, 5)` → ?
**Q25** `np.array([[1,2,3],[4,5,6]])[:,1]` → ?
**Q26** `np.array([[1,2],[3,4],[5,6]])[1:, 0]` → ?
**Q27** `np.array([1,2,3,4,5,6]).reshape(3,2).flatten()` — modifies original? → ?
**Q28** `np.array([[1,2],[3,4]]).sum(axis=0)` → ?
**Q29** `np.array([[1,2],[3,4]]).sum(axis=1)` → ?
**Q30** `np.unique(np.array([1,1,2,3,3,4]))` → ?

### Answer table

| Q | Answer |
|---|--------|
| 1 | `2` |
| 2 | `[2 3 4]` |
| 3 | `[1 4]` |
| 4 | `(2, 2)` |
| 5 | `2` |
| 6 | `3` |
| 7 | `(2, 3)` |
| 8 | view |
| 9 | copy |
| 10 | same object (not a copy, not a view — identical reference) |
| 11 | `[5 7 9]` |
| 12 | `[2 4 6]` |
| 13 | `15` |
| 14 | `3.0` |
| 15 | `9` |
| 16 | No — `np.sort` returns new array, original unchanged |
| 17 | `[4 5]` |
| 18 | `[0 0 0 1 1]` |
| 19 | `(2, 2)` |
| 20 | `(2, 2)` |
| 21 | `(2, 3)` |
| 22 | `2` |
| 23 | `[0 2 4 6 8]` |
| 24 | `[0.   0.25 0.5  0.75 1.  ]` |
| 25 | `[2 5]` |
| 26 | `[3 5]` |
| 27 | No — flatten returns a copy |
| 28 | `[4 6]` |
| 29 | `[3 7]` |
| 30 | `[1 2 3 4]` |
