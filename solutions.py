"""
Python Programming Assessment: Numbers & Basic Logic
Role: Python Developer Intern

Contains the two required functions:
    1. even_or_odd(n)
    2. add_all(numbers)
"""


def even_or_odd(n: int) -> str:
    """
    Determine whether a number is even or odd.

    Parameters
    ----------
    n : int
        The integer to check.

    Returns
    -------
    str
        "Even" if n is divisible by 2, otherwise "Odd".

    Raises
    ------
    TypeError
        If n is not an integer (or a whole-number float).
    """
    if isinstance(n, bool):
        # bool is a subclass of int in Python; explicitly reject it
        raise TypeError("Boolean values are not valid numeric input.")
    if isinstance(n, float):
        if not n.is_integer():
            raise ValueError("Only whole numbers are supported (got a non-integer float).")
        n = int(n)
    if not isinstance(n, int):
        raise TypeError(f"Expected an int, got {type(n).__name__}.")

    return "Even" if n % 2 == 0 else "Odd"


def add_all(numbers: list) -> int:
    """
    Calculate the total sum of a list of numbers.

    Parameters
    ----------
    numbers : list
        A list of numeric values (int or float).

    Returns
    -------
    int (or float, if any element is a float)
        The sum of all elements in the list. Returns 0 for an empty list.

    Raises
    ------
    TypeError
        If `numbers` is not a list, or if it contains non-numeric elements.
    """
    if not isinstance(numbers, list):
        raise TypeError(f"Expected a list, got {type(numbers).__name__}.")

    total = 0
    for index, value in enumerate(numbers):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError(f"Element at index {index} is not a number: {value!r}")
        total += value

    return total


if __name__ == "__main__":
    # Quick manual smoke test when running this file directly
    print(even_or_odd(4))   # Even
    print(even_or_odd(7))   # Odd
    print(add_all([1, 2, 3, 4, 5]))  # 15
