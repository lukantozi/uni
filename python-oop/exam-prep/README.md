# Python OOP — Exam Prep

## Progress

| Gate | Topic | Layer A | Layer B | Layer C |
|------|-------|---------|---------|---------|
| G1 | OOP Basics | [x] 14/15, drills | [x] 12/14, drills | [x] 27/30 |
| G2 | Inheritance | [x] 15/15, drills | [x] 11/14, drills | [x] 27/30 |
| G3 | Encapsulation | [x] 15/15 | [ ] | [ ] |
| G4 | Unit Testing | [ ] | [ ] | [ ] |
| G5 | NumPy | [ ] | [ ] | [ ] |
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
