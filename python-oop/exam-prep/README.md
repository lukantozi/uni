# Python OOP — Exam Prep

## Progress

| Gate | Topic | Layer A | Layer B | Layer C |
|------|-------|---------|---------|---------|
| G1 | OOP Basics | [x] 14/15, drills | [x] 12/14, drills | [x] 27/30 |
| G2 | Inheritance | [x] 15/15, drills | [x] 11/14, drills | [x] 27/30 |
| G3 | Encapsulation | [x] 15/15, drills | [x] 11/14, drills | [x] 29/30 |
| G4 | Unit Testing | [x] 14/15, drills | [x] 13/14, drills | [x] 30/30 |
| G5 | NumPy | [x] 10/15, drills | [x] 11/15, drills | [x] 27/30 |
| G6 | Pandas + JSON/CSV | [ ] | [ ] | [ ] |
| G7 | Tkinter / GUI | [ ] | [ ] | [ ] |
| G8 | Mixed Mocks | [ ] | [ ] | [ ] |

## Mistakes Log

| Gate | Layer | Question | What I wrote | Correct |
|------|-------|----------|--------------|---------|
| G1 | A | Q7 `type(p)` | `<type "class">` | `<class '__main__.Person'>` |
| G1 | A | Drill 5 'Vehicle.wheels' predict | `4` | `6` |
| G1 | B | Q1 mutable class attr | `sit` | `['sit']` |
| G1 | B | Q11 type(f) vs type(Foo) | `False, True` | `True, False` |
| G1 | C | Q25 del a.val | `AttributeError` | `0` |
| G1 | C | Q26 a1 == a2 | `True` | `False` (identity comparison) |
| G1 | C | Q30 class vs instance| `class instance instance` | `class instance class` |
| G2 | B | Q1 missing `super()` `b.x` | `"A"` | `AttributeError` (parent `__init__` not run) |
| G2 | B | Q5 polymorphic `setup()` call | `AttributeError` for `y` | `1` then `2` |
| G2 | B | Q13 `self.default()` in `A.__init__` | `0` | `42` (`B.default` used via runtime dispatch) |
| G2 | C | Q11 greet `type(self).__name__` | `I'm type B` | `I am B` |
| G2 | C | Q27 mutable class attr in subclass | `[]` | `[1]` |
| G2 | C | Q28 float print formatting | `Alice 4.` | `Alice 4.0` |
| G3 | B | Q1 `a.__x = 99` outside class body   | `AttributeError` | `99` then `10` (mangling only inside class body) |
| G3 | B | Q12 setter in `__init__` vs property  | `6` then `10` | `3` then `10` (`__init__` sets `_n` directly, no doubling) |
| G3 | B | Q13 `vars()` output format | `_A__x` | `{'_A__x': 10}` (full dict with key and value) |
| G3 | C | Q6 `@property` no setter vs `__x` outside class | created new attr | `AttributeError: can't set attribute` (property descriptor blocks it) |
| G4 | A | Q11 `assertRaises(ValueError)` when `'a' + 1` raises `TypeError` | `True` | `False` (wrong exception type → test fails) |
| G4 | B | Q13 `tearDown` with class variable `results` | `0\nTrue` | `2\nTrue` (class var persists across tests, tearDown appends after each) |
| G5 | B | Q8 print variable after modify | `[99 4 5]` | printed `a`, not `b` |
| G5 | B | Q10 division result dtype | `3` | `3.0` (float dtype) |
| G5 | B | Q11 two `print()` calls | missed second `print()` | original array also printed |
| G5 | B | Q13 `concatenate` `axis=0` | `[3 4 5 10 20 30]` | stacks rows, doesn't flatten |
| G5 | B | Q14 `vstack` on 2D array | `Error` | adds new row below existing 2D array |
| G5 | A | Q1 `arange` slice | `[1]` | `[99]` (assigns in-place, knew the rule) |
| G5 | A | Q5 `np.sum(arr, axis=0)` | reversed axes | `axis=0` sums down **columns**, not across rows |
| G5 | A | Q10 reshape to column vector | `[11, 22, 33]` | `[[11 21 31] [12 22 32] [13 23 33]]` didn't know broadcasting rules |
| G5 | C | Q17 boolean indexing vs `np.where` | `[0 0 0 1 1]` | `[4 5]` - confused boolean mask with np.where output |
| G5 | C | Q20 hstack shape on column vectors | `[[1 3] [2 4]]` | `(2, 2)` - gave values instead of shape |
| G5 | C | Q26 2D slice `[1:, 0]` | `[2 4]` | `[3 5]` - off by one on row index |
