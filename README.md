# Python Programming Assessment: Numbers & Basic Logic

**Full Name:** Atharv Jadhav
**Submission Date:** 03/08/2026
**Role Applied For:** Python Developer Intern — Embed Square Solutions

## Overview

This repository contains my solution to the "Python Programming Assessment: Numbers & Basic Logic" screening assignment. It implements two functions as specified:

1. `even_or_odd(n: int) -> str`
2. `add_all(numbers: list) -> int`

## Repository Structure

```
.
├── es-python-assessment-numbers-basic-logic.ipynb   # Jupyter notebook with explanations, code, and executed test outputs
├── solutions.py                                       # Plain .py file with both functions (importable / runnable standalone)
├── test_solutions.py                                  # Unit tests (Python unittest) covering normal and edge cases
└── README.md                                          # This file
```

## Approach

### Question 1 — Even or Odd
- Uses the modulo operator (`n % 2 == 0`) to decide even vs. odd — the standard, most readable approach.
- **Edge cases handled:**
  - Negative integers (Python's `%` operator handles these correctly, e.g. `-4 % 2 == 0`).
  - `0` is treated as even.
  - Whole-number floats (e.g. `2.0`) are accepted and converted to `int`.
  - Non-numeric or invalid input (strings, `None`, booleans, non-integer floats) raises a clear `TypeError`/`ValueError` rather than failing silently or producing a wrong answer.

### Question 2 — Sum of a List
- Uses a `for` loop with an accumulator variable (`total`) to sum the list manually, as intended by the assignment ("Looping constructs" and "Accumulator variables"), instead of the built-in `sum()`.
- **Edge cases handled:**
  - An empty list returns `0` instead of raising an error.
  - Non-list input (e.g. a string) raises a `TypeError`.
  - A list containing non-numeric elements raises a `TypeError` that identifies the offending index/value.
  - Mixed `int`/`float` lists are summed correctly.

## How to Run

### Option 1: Jupyter Notebook
Open `es-python-assessment-numbers-basic-logic.ipynb` in Jupyter (or JupyterLab / VS Code / Google Colab) and run all cells. The notebook is already executed and includes sample outputs for review without needing to re-run it.

```bash
jupyter notebook es-python-assessment-numbers-basic-logic.ipynb
```

### Option 2: Plain Python script
```bash
python solutions.py
```

### Running the tests
```bash
python -m unittest test_solutions.py -v
```

