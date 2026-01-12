"""
Mathematical Utilities with Comprehensive Error Handling

This module provides common mathematical operations with robust error handling
and clear, informative error messages.
"""

import math
from typing import List, Union, Optional


class MathError(Exception):
    """Base exception for mathematical operation errors."""
    pass


class InvalidInputError(MathError):
    """Raised when input validation fails."""
    pass


class DivisionError(MathError):
    """Raised when division operations encounter errors."""
    pass


class DomainError(MathError):
    """Raised when input is outside the valid domain for an operation."""
    pass


def safe_divide(numerator: Union[int, float], denominator: Union[int, float]) -> float:
    """
    Safely divide two numbers with proper error handling.

    Args:
        numerator: The number to be divided
        denominator: The number to divide by

    Returns:
        The result of the division

    Raises:
        InvalidInputError: If inputs are not numeric
        DivisionError: If attempting to divide by zero
    """
    if not isinstance(numerator, (int, float)):
        raise InvalidInputError(
            f"Numerator must be a number, got {type(numerator).__name__}: {numerator}"
        )

    if not isinstance(denominator, (int, float)):
        raise InvalidInputError(
            f"Denominator must be a number, got {type(denominator).__name__}: {denominator}"
        )

    if denominator == 0:
        raise DivisionError(
            "Cannot divide by zero. Division by zero is undefined in mathematics."
        )

    try:
        result = numerator / denominator
        return result
    except Exception as e:
        raise MathError(f"Unexpected error during division: {str(e)}")


def calculate_average(numbers: List[Union[int, float]]) -> float:
    """
    Calculate the average of a list of numbers with error handling.

    Args:
        numbers: A list of numeric values

    Returns:
        The arithmetic mean of the numbers

    Raises:
        InvalidInputError: If input is not a list or contains non-numeric values
        ValueError: If the list is empty
    """
    if not isinstance(numbers, list):
        raise InvalidInputError(
            f"Input must be a list, got {type(numbers).__name__}"
        )

    if len(numbers) == 0:
        raise ValueError(
            "Cannot calculate average of an empty list. Please provide at least one number."
        )

    for i, num in enumerate(numbers):
        if not isinstance(num, (int, float)):
            raise InvalidInputError(
                f"All elements must be numeric. Element at index {i} is {type(num).__name__}: {num}"
            )

    try:
        return sum(numbers) / len(numbers)
    except Exception as e:
        raise MathError(f"Unexpected error calculating average: {str(e)}")


def calculate_square_root(number: Union[int, float]) -> float:
    """
    Calculate the square root of a number with error handling.

    Args:
        number: The number to find the square root of

    Returns:
        The square root of the number

    Raises:
        InvalidInputError: If input is not numeric
        DomainError: If attempting to find square root of a negative number
    """
    if not isinstance(number, (int, float)):
        raise InvalidInputError(
            f"Input must be a number, got {type(number).__name__}: {number}"
        )

    if number < 0:
        raise DomainError(
            f"Cannot calculate square root of negative number: {number}. "
            "For complex results, use cmath.sqrt() instead."
        )

    try:
        return math.sqrt(number)
    except Exception as e:
        raise MathError(f"Unexpected error calculating square root: {str(e)}")


def calculate_factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer with error handling.

    Args:
        n: A non-negative integer

    Returns:
        The factorial of n (n!)

    Raises:
        InvalidInputError: If input is not an integer
        DomainError: If n is negative
        ValueError: If n is too large to compute
    """
    if not isinstance(n, int):
        raise InvalidInputError(
            f"Factorial requires an integer input, got {type(n).__name__}: {n}"
        )

    if n < 0:
        raise DomainError(
            f"Factorial is not defined for negative numbers: {n}. "
            "Please provide a non-negative integer."
        )

    if n > 10000:
        raise ValueError(
            f"Factorial of {n} is too large to compute efficiently. "
            "Please provide a number less than or equal to 10000."
        )

    try:
        return math.factorial(n)
    except OverflowError:
        raise ValueError(
            f"Result of factorial({n}) is too large to represent."
        )
    except Exception as e:
        raise MathError(f"Unexpected error calculating factorial: {str(e)}")


def calculate_power(base: Union[int, float], exponent: Union[int, float]) -> float:
    """
    Calculate base raised to the power of exponent with error handling.

    Args:
        base: The base number
        exponent: The exponent to raise the base to

    Returns:
        The result of base^exponent

    Raises:
        InvalidInputError: If inputs are not numeric
        DomainError: If operation results in undefined value (e.g., 0^0)
        OverflowError: If result is too large
    """
    if not isinstance(base, (int, float)):
        raise InvalidInputError(
            f"Base must be a number, got {type(base).__name__}: {base}"
        )

    if not isinstance(exponent, (int, float)):
        raise InvalidInputError(
            f"Exponent must be a number, got {type(exponent).__name__}: {exponent}"
        )

    # Handle special case: 0^0 is mathematically undefined
    if base == 0 and exponent == 0:
        raise DomainError(
            "0^0 is undefined in mathematics. Please provide different values."
        )

    # Handle negative base with fractional exponent
    if base < 0 and not isinstance(exponent, int) and exponent != int(exponent):
        raise DomainError(
            f"Cannot raise negative base {base} to fractional exponent {exponent}. "
            "This would result in a complex number."
        )

    try:
        result = base ** exponent

        # Check for overflow
        if math.isinf(result):
            raise OverflowError(
                f"Result of {base}^{exponent} is too large to represent."
            )

        return result
    except OverflowError:
        raise OverflowError(
            f"Result of {base}^{exponent} exceeds maximum representable value."
        )
    except Exception as e:
        raise MathError(f"Unexpected error calculating power: {str(e)}")


def find_nth_element(data: List, index: int) -> any:
    """
    Safely retrieve the nth element from a list with error handling.

    Args:
        data: The list to retrieve from
        index: The index of the element to retrieve

    Returns:
        The element at the specified index

    Raises:
        InvalidInputError: If data is not a list or index is not an integer
        IndexError: If index is out of bounds
    """
    if not isinstance(data, list):
        raise InvalidInputError(
            f"Data must be a list, got {type(data).__name__}"
        )

    if not isinstance(index, int):
        raise InvalidInputError(
            f"Index must be an integer, got {type(index).__name__}: {index}"
        )

    if len(data) == 0:
        raise IndexError(
            "Cannot retrieve element from empty list."
        )

    if index < 0 or index >= len(data):
        raise IndexError(
            f"Index {index} is out of bounds for list of length {len(data)}. "
            f"Valid indices are 0 to {len(data) - 1}."
        )

    try:
        return data[index]
    except Exception as e:
        raise MathError(f"Unexpected error retrieving element: {str(e)}")


def calculate_percentage(part: Union[int, float], whole: Union[int, float]) -> float:
    """
    Calculate what percentage 'part' is of 'whole' with error handling.

    Args:
        part: The partial value
        whole: The total value

    Returns:
        The percentage (0-100)

    Raises:
        InvalidInputError: If inputs are not numeric
        DivisionError: If whole is zero
        ValueError: If whole is negative
    """
    if not isinstance(part, (int, float)):
        raise InvalidInputError(
            f"Part must be a number, got {type(part).__name__}: {part}"
        )

    if not isinstance(whole, (int, float)):
        raise InvalidInputError(
            f"Whole must be a number, got {type(whole).__name__}: {whole}"
        )

    if whole == 0:
        raise DivisionError(
            "Cannot calculate percentage when whole is zero. "
            "The denominator must be a non-zero value."
        )

    if whole < 0:
        raise ValueError(
            f"The 'whole' value should be positive, got {whole}. "
            "Percentage calculations typically use positive denominators."
        )

    try:
        percentage = (part / whole) * 100
        return percentage
    except Exception as e:
        raise MathError(f"Unexpected error calculating percentage: {str(e)}")
