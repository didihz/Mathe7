"""
Test suite for math_utils module demonstrating error handling.

This file shows how the error handling works in practice.
"""

import math_utils


def test_safe_divide():
    """Test safe division with error handling."""
    print("=" * 60)
    print("Testing safe_divide()")
    print("=" * 60)

    # Valid division
    try:
        result = math_utils.safe_divide(10, 2)
        print(f"✓ 10 / 2 = {result}")
    except Exception as e:
        print(f"✗ Error: {e}")

    # Division by zero
    try:
        result = math_utils.safe_divide(10, 0)
        print(f"✓ 10 / 0 = {result}")
    except math_utils.DivisionError as e:
        print(f"✓ Caught expected error: {e}")

    # Invalid input type
    try:
        result = math_utils.safe_divide("10", 2)
        print(f"✓ '10' / 2 = {result}")
    except math_utils.InvalidInputError as e:
        print(f"✓ Caught expected error: {e}")

    print()


def test_calculate_average():
    """Test average calculation with error handling."""
    print("=" * 60)
    print("Testing calculate_average()")
    print("=" * 60)

    # Valid average
    try:
        result = math_utils.calculate_average([1, 2, 3, 4, 5])
        print(f"✓ Average of [1, 2, 3, 4, 5] = {result}")
    except Exception as e:
        print(f"✗ Error: {e}")

    # Empty list
    try:
        result = math_utils.calculate_average([])
        print(f"✓ Average of [] = {result}")
    except ValueError as e:
        print(f"✓ Caught expected error: {e}")

    # Non-numeric element
    try:
        result = math_utils.calculate_average([1, 2, "three", 4])
        print(f"✓ Average with non-numeric = {result}")
    except math_utils.InvalidInputError as e:
        print(f"✓ Caught expected error: {e}")

    print()


def test_calculate_square_root():
    """Test square root calculation with error handling."""
    print("=" * 60)
    print("Testing calculate_square_root()")
    print("=" * 60)

    # Valid square root
    try:
        result = math_utils.calculate_square_root(16)
        print(f"✓ √16 = {result}")
    except Exception as e:
        print(f"✗ Error: {e}")

    # Negative number
    try:
        result = math_utils.calculate_square_root(-4)
        print(f"✓ √(-4) = {result}")
    except math_utils.DomainError as e:
        print(f"✓ Caught expected error: {e}")

    # Invalid input type
    try:
        result = math_utils.calculate_square_root("16")
        print(f"✓ √'16' = {result}")
    except math_utils.InvalidInputError as e:
        print(f"✓ Caught expected error: {e}")

    print()


def test_calculate_factorial():
    """Test factorial calculation with error handling."""
    print("=" * 60)
    print("Testing calculate_factorial()")
    print("=" * 60)

    # Valid factorial
    try:
        result = math_utils.calculate_factorial(5)
        print(f"✓ 5! = {result}")
    except Exception as e:
        print(f"✗ Error: {e}")

    # Negative number
    try:
        result = math_utils.calculate_factorial(-5)
        print(f"✓ (-5)! = {result}")
    except math_utils.DomainError as e:
        print(f"✓ Caught expected error: {e}")

    # Non-integer input
    try:
        result = math_utils.calculate_factorial(5.5)
        print(f"✓ (5.5)! = {result}")
    except math_utils.InvalidInputError as e:
        print(f"✓ Caught expected error: {e}")

    # Too large number
    try:
        result = math_utils.calculate_factorial(50000)
        print(f"✓ 50000! = {result}")
    except ValueError as e:
        print(f"✓ Caught expected error: {e}")

    print()


def test_calculate_power():
    """Test power calculation with error handling."""
    print("=" * 60)
    print("Testing calculate_power()")
    print("=" * 60)

    # Valid power
    try:
        result = math_utils.calculate_power(2, 3)
        print(f"✓ 2^3 = {result}")
    except Exception as e:
        print(f"✗ Error: {e}")

    # 0^0 (undefined)
    try:
        result = math_utils.calculate_power(0, 0)
        print(f"✓ 0^0 = {result}")
    except math_utils.DomainError as e:
        print(f"✓ Caught expected error: {e}")

    # Negative base with fractional exponent
    try:
        result = math_utils.calculate_power(-4, 0.5)
        print(f"✓ (-4)^0.5 = {result}")
    except math_utils.DomainError as e:
        print(f"✓ Caught expected error: {e}")

    print()


def test_find_nth_element():
    """Test element retrieval with error handling."""
    print("=" * 60)
    print("Testing find_nth_element()")
    print("=" * 60)

    # Valid retrieval
    try:
        result = math_utils.find_nth_element([10, 20, 30, 40], 2)
        print(f"✓ Element at index 2 in [10, 20, 30, 40] = {result}")
    except Exception as e:
        print(f"✗ Error: {e}")

    # Index out of bounds
    try:
        result = math_utils.find_nth_element([10, 20, 30], 5)
        print(f"✓ Element at index 5 = {result}")
    except IndexError as e:
        print(f"✓ Caught expected error: {e}")

    # Empty list
    try:
        result = math_utils.find_nth_element([], 0)
        print(f"✓ Element from empty list = {result}")
    except IndexError as e:
        print(f"✓ Caught expected error: {e}")

    print()


def test_calculate_percentage():
    """Test percentage calculation with error handling."""
    print("=" * 60)
    print("Testing calculate_percentage()")
    print("=" * 60)

    # Valid percentage
    try:
        result = math_utils.calculate_percentage(25, 100)
        print(f"✓ 25 is {result}% of 100")
    except Exception as e:
        print(f"✗ Error: {e}")

    # Division by zero
    try:
        result = math_utils.calculate_percentage(25, 0)
        print(f"✓ 25 / 0 = {result}%")
    except math_utils.DivisionError as e:
        print(f"✓ Caught expected error: {e}")

    # Negative whole
    try:
        result = math_utils.calculate_percentage(25, -100)
        print(f"✓ 25 / -100 = {result}%")
    except ValueError as e:
        print(f"✓ Caught expected error: {e}")

    print()


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("MATH UTILS ERROR HANDLING TEST SUITE")
    print("=" * 60 + "\n")

    test_safe_divide()
    test_calculate_average()
    test_calculate_square_root()
    test_calculate_factorial()
    test_calculate_power()
    test_find_nth_element()
    test_calculate_percentage()

    print("=" * 60)
    print("TEST SUITE COMPLETED")
    print("=" * 60)
