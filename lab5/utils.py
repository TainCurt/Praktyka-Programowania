"""
Utility functions for basic arithmetic operations.
"""

def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b

def subtract(a: int, b: int) -> int:
    """Return the difference of two integers."""
    return a - b

def multiply(a: int, b: int) -> int:
    """Return the product of two integers."""
    return a * b

def divide(a: int, b: int) -> float:
    """Return the division of two integers as a float."""
    return a / b

def binary(n: int) -> str:
    """
    Convert a natural number (0–100) to binary (5-bit format).
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")

    if n < 0 or n > 100:
        raise ValueError("Number out of range (0–100)")

    return format(n, '05b')