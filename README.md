# OOP Practice Assignment
### Classes, Objects, and Python Data Types

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![OOP](https://img.shields.io/badge/Paradigm-Object--Oriented-green)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

---

## Overview

This project demonstrates core **Object-Oriented Programming (OOP)** concepts in Python, including class definition, object creation, and working with Python's built-in data types: lists, tuples, sets, and dictionaries.

---

## Project Structure

```
OOP_Assignment/
├── OOP_Assignment.py   # Main script with all parts
└── README.md           # This file
```

---

## What It Covers

| Part | Topic |
|------|-------|
| Part 1 | Class definition — `Student` class with attributes and methods |
| Part 2 | Creating and using objects |
| Part 3 | Dictionary and set integration |
| Part 4 | Tuple immutability demonstration |
| Part 5 | List operations (`.pop()`, indexing, `len()`) |
| Part 6 | Bonus — email validation with regex, grade counting |

---

## How to Run

1. Make sure you have **Python 3.x** installed. You can check by running:
```bash
python --version
```

2. Clone or download this repository.

3. Navigate to the project folder and run:
```bash
python OOP_Assignment.py
```

---

## Sample Output

```
========================================
PART 2: Student Objects
========================================
Name:    Kathy Booth
Email:   kathy@school.com
Grades:  [99, 92, 95, 94, 98]
Average: 95.60

...

========================================
PART 6: Bonus
========================================
Email validation:
  kathy@school.com — valid
  andrea@school.com — valid
  nayoungatschool.com — invalid

Total grades above 90 across all students: 8
```

---

## Key Concepts Demonstrated

- **Classes & Objects** — defining a `Student` blueprint and creating instances from it
- **Methods** — `add_grade()`, `average_grade()`, `display_info()`, `grades_tuple()`
- **Dictionary** — mapping student emails to Student objects, safe lookup with `.get()`
- **Set** — collecting all unique grades using a set comprehension
- **Tuple** — converting grades to a tuple and demonstrating immutability with `try/except`
- **List Operations** — `.append()`, `.pop()`, indexing with `[0]` and `[-1]`, `len()`
- **Regex** — validating email format using the `re` module

---

## Author

Kathy Booth
with a little help from Claude, LLM
Coding Temple — Python OOP Assignment
