# Gate 6 — Pandas + JSON/CSV

> Topics: `pd.read_csv`, `pd.read_json`, `DataFrame` creation, `iloc`, `loc`, `dropna`, `fillna`, `df.shape`, `df.dtypes`, `df.describe`, `df.columns`, boolean filtering, `to_csv`, `to_json`

***

## Layer A — Skeleton

### Predict-output drills

**1.**
```python
import pandas as pd

df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
print(df['a'][1])
```

**2.**
```python
import pandas as pd

df = pd.DataFrame({'x': [10, 20, 30]})
print(df.shape)
```

**3.**
```python
import pandas as pd

df = pd.DataFrame({'name': ['Alice', 'Bob'], 'age': [25, 30]})
print(df.columns.tolist())
```

**4.**
```python
import pandas as pd

df = pd.DataFrame({'a': [1, 2, None, 4]})
print(df.dropna())
```

**5.**
```python
import pandas as pd

df = pd.DataFrame({'a': [1, 2, None, 4]})
print(df.fillna(0))
```

**6.**
```python
import pandas as pd

df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
print(df.iloc[1, 1])
```

**7.**
```python
import pandas as pd

df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]}, index=['x', 'y', 'z'])
print(df.loc['y', 'b'])
```

**8.**
```python
import pandas as pd

df = pd.DataFrame({'val': [10, 20, 30, 40]})
print(df[df['val'] > 20])
```

**9.**
```python
import pandas as pd

df = pd.DataFrame({'a': [1, 2, 3]})
print(type(df['a']))
```

**10.**
```python
import pandas as pd

df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
print(df.iloc[0])
```

**11.**
```python
import pandas as pd

df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
print(df.iloc[:, 0].tolist())
```

**12.**
```python
import pandas as pd

df = pd.DataFrame({'a': [1, 2, 3]})
df['b'] = df['a'] * 2
print(df)
```

**13.**
```python
import pandas as pd

df = pd.DataFrame({'a': [1, None, 3], 'b': [None, 2, 3]})
print(df.dropna())
```

**14.**
```python
import pandas as pd

df = pd.DataFrame({'score': [55, 70, 80, 90]})
print(df[df['score'] >= 70]['score'].tolist())
```

**15.**
```python
import pandas as pd
import json

data = '{"name": "Alice", "age": 30}'
d = json.loads(data)
print(d['name'])
```

***

### Answers — Layer A

| # | Answer |
|---|--------|
| 1 | `2` |
| 2 | `(3, 1)` |
| 3 | `['name', 'age']` |
| 4 | `   a\n0  1.0\n1  2.0\n3  4.0` (row 2 dropped) |
| 5 | `     a\n0  1.0\n1  2.0\n2  0.0\n3  4.0` |
| 6 | `5` |
| 7 | `5` |
| 8 | `   val\n2   30\n3   40` |
| 9 | `<class 'pandas.core.series.Series'>` |
| 10 | `a    1\nb    4\nName: 0, dtype: int64` |
| 11 | `[1, 2, 3]` |
| 12 | `   a  b\n0  1  2\n1  2  4\n2  3  6` |
| 13 | `     a    b\n2  3.0  3.0` (only row with no NaN) |
| 14 | `[70, 80, 90]` |
| 15 | `Alice` |

**Pass: 13/15 correct, no running code.**

***

### Coding drills — Layer A

**1.** Create a DataFrame from a dict with columns `name`, `age`, `city` and 3 rows of your choice. Print the shape and column list.

**2.** Create a DataFrame with a column `score` containing `[85, 90, None, 70, None]`. Drop NaN rows. Then separately fill NaN with `0`. Print both results.

**3.** Create a DataFrame with columns `a` and `b`. Use `iloc` to print the value at row 2, column 1. Use `loc` to print the same value using the label.

**4.** Read the following JSON string and create a DataFrame from it. Print the `name` column.
```python
data = '[{"name": "Alice", "score": 90}, {"name": "Bob", "score": 75}]'
```

**5.** Create a DataFrame with column `price` containing `[10, 25, 5, 40, 15]`. Filter and print only rows where `price > 12`.

**Pass: All 5 correct first run.**

***

## Layer B — Variants & gotchas

### Predict-output drills

**1.**
```python
import pandas as pd

df = pd.DataFrame({'a': [1, 2, 3]})
print(df['a'][0])
print(type(df['a'][0]))
```

**2.**
```python
import pandas as pd

df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
print(df.iloc[1])
print(df.iloc[1, 0])
```

**3.**
```python
import pandas as pd

df = pd.DataFrame({'a': [1, 2, 3]}, index=[10, 20, 30])
print(df.loc[20])
print(df.iloc[1])
```

**4.**
```python
import pandas as pd

df = pd.DataFrame({'a': [1, None, 3], 'b': [4, 5, None]})
print(df.dropna(axis=1))
```

**5.**
```python
import pandas as pd

df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
print(df[['a']].shape)
print(df['a'].shape)
```

**6.**
```python
import pandas as pd

df = pd.DataFrame({'val': [1, 2, 3, 4, 5]})
df2 = df[df['val'] > 2]
print(df2.reset_index(drop=True)['val'].tolist())
```

**7.**
```python
import pandas as pd

df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
df['c'] = df['a'] + df['b']
print(df['c'].tolist())
```

**8.**
```python
import pandas as pd
import json

data = [{"name": "Alice"}, {"name": "Bob"}]
s = json.dumps(data)
print(type(s))
print(s[0])
```

**9.**
```python
import pandas as pd

df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
print(df.iloc[:2, :1])
```

**10.**
```python
import pandas as pd

df = pd.DataFrame({'score': [40, 70, 85]})
df['pass'] = df['score'] >= 60
print(df['pass'].tolist())
```

**11.**
```python
import pandas as pd

df = pd.DataFrame({'a': [1, 2, 3]})
print(df.iloc[-1, 0])
```

**12.**
```python
import pandas as pd
import json

d = {"x": 1, "y": 2}
s = json.dumps(d)
d2 = json.loads(s)
print(d2['x'] + d2['y'])
```

**13.**
```python
import pandas as pd

df = pd.DataFrame({'a': [None, None, None]})
print(df.fillna(99)['a'].tolist())
```

**14.**
```python
import pandas as pd

df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
print(df.loc[0:1, 'a'])
```

***

### Answers — Layer B

| # | Answer |
|---|--------|
| 1 | `1` then `<class 'numpy.int64'>` (pandas stores ints as numpy types) |
| 2 | `a    2\nb    5\nName: 1, dtype: int64` then `2` |
| 3 | `a    2\nName: 20, dtype: int64` twice — `loc` uses index label, `iloc` uses position, both hit row index 20 / position 1 |
| 4 | drops both columns |
| 5 | `(3, 1)` then `(3,)` — double brackets keep DataFrame shape, single bracket returns Series (1D) |
| 6 | `[3, 4, 5]` |
| 7 | `[5, 7, 9]` |
| 8 | `<class 'str'>` then `[` — `json.dumps` returns a string, `s[0]` is the first character `[` |
| 9 | `   a\n0  1\n1  2` |
| 10 | `[False, True, True]` |
| 11 | `3` |
| 12 | `3` |
| 13 | `[99.0, 99.0, 99.0]` |
| 14 | `0    1\n1    2\nName: a, dtype: int64` — `loc` with integer index is **inclusive** on both ends |

**Pass: 12/14 correct, no notes.**

***

### Coding drills — Layer B

**1.** Create a DataFrame from a CSV string using `pd.read_csv` with `io.StringIO`. The CSV has columns `name` and `grade`. Filter rows where `grade >= 60` and print the result.

**2.** Load this JSON string into a DataFrame. Add a column `passed` that is `True` if `score >= 50`. Print the full DataFrame.
```python
data = '[{"name":"Alice","score":80},{"name":"Bob","score":40},{"name":"Carol","score":55}]'
```

**3.** Create a DataFrame with 3 columns and 4 rows containing some `None` values. Use `dropna(axis=0)` and `dropna(axis=1)` separately. Print the shape of each result and explain the difference in a comment.

**4.** Demonstrate the `loc` vs `iloc` difference: create a DataFrame with a custom string index `['a', 'b', 'c']`. Show that `iloc[0]` and `loc['a']` return the same row, but `loc[0]` raises a `KeyError`.

**Pass: All 4 correct first run.**

***

## Layer C — Speed Run

Target: 30 questions in under 20 minutes. No notes, no running code. Pass: 27/30.

**Q1** `pd.DataFrame({'a': [1,2,3]}).shape` → ?
**Q2** `df.iloc[0, 0]` — uses row/col position or label? → ?
**Q3** `df.loc['x', 'a']` — uses row/col position or label? → ?
**Q4** `df.dropna()` — drops rows or columns by default? → ?
**Q5** `df.fillna(0)` — modifies original? → ?
**Q6** `df['a']` returns what type? → ?
**Q7** `df[['a']]` returns what type? → ?
**Q8** `df.shape` returns what type? → ?
**Q9** `json.loads('{"x": 1}')` returns what type? → ?
**Q10** `json.dumps({"x": 1})` returns what type? → ?
**Q11** `pd.DataFrame({'a': [1,2,3]}).iloc[-1, 0]` → ?
**Q12** `df.dropna(axis=1)` — drops rows or columns? → ?
**Q13** `df.columns` returns what type? → ?
**Q14** `df.loc[0:2]` — is endpoint inclusive? → ?
**Q15** `df.iloc[0:2]` — is endpoint inclusive? → ?
**Q16** `pd.DataFrame({'a':[1,None,3]}).fillna(0)['a'].tolist()` → ?
**Q17** `type(df['a'][0])` for integer column → ?
**Q18** `json.dumps([1,2,3])` → ?
**Q19** `json.loads('[1,2,3]')` returns what type? → ?
**Q20** `pd.DataFrame({'a':[1,2],'b':[3,4]}).iloc[:, 1].tolist()` → ?
**Q21** `df.dropna()` returns new DataFrame or modifies in place? → ?
**Q22** `pd.DataFrame({'a': [1,2,3]}).iloc[1, 0]` → ?
**Q23** double bracket `df[['a']]` vs single `df['a']` — which is DataFrame? → ?
**Q24** `pd.read_csv` reads from what? → ?
**Q25** `df.to_csv('file.csv', index=False)` — what does `index=False` do? → ?
**Q26** `pd.DataFrame({'a':[1,2,3],'b':[4,5,6]}).loc[1:2, 'b'].tolist()` → ?
**Q27** `pd.DataFrame({'a':[None,None]}).dropna().shape` → ?
**Q28** `json.loads(json.dumps({"k": "v"}))['k']` → ?
**Q29** `df[df['a'] > 2]` — what does this return? → ?
**Q30** `pd.DataFrame({'a':[1,2,3]}).iloc[0:2].shape` → ?

***

### Answers — Layer C

| # | Answer |
|---|--------|
| 1 | `(3, 1)` |
| 2 | position |
| 3 | label |
| 4 | rows (`axis=0` default) |
| 5 | No — returns new DataFrame |
| 6 | `Series` |
| 7 | `DataFrame` |
| 8 | `tuple` |
| 9 | `dict` |
| 10 | `str` |
| 11 | `3` |
| 12 | columns |
| 13 | `Index` (pandas Index object) |
| 14 | Yes — `loc` is inclusive on both ends |
| 15 | No — `iloc` excludes end (like Python slicing) |
| 16 | `[1.0, 0.0, 3.0]` |
| 17 | `numpy.int64` |
| 18 | `'[1, 2, 3]'` (a string) |
| 19 | `list` |
| 20 | `[3, 4]` |
| 21 | returns new DataFrame |
| 22 | `2` |
| 23 | double bracket `df[['a']]` is DataFrame |
| 24 | file path or file-like object (e.g. `StringIO`) |
| 25 | omits the row index column from the CSV |
| 26 | `[5, 6]` |
| 27 | `(0, 1)` |
| 28 | `'v'` |
| 29 | filtered DataFrame (boolean indexing) |
| 30 | `(2, 1)` |

**Pass: 27/30 correct, under 20 minutes, no notes.**
