# Mathematical Utilities with Comprehensive Error Handling

This project demonstrates best practices for error handling in Python with clear, informative error messages.

## Features

- **Custom Exception Hierarchy**: Specialized exceptions for different error types
- **Input Validation**: All functions validate inputs before processing
- **Clear Error Messages**: Every error includes context about what went wrong and how to fix it
- **Type Safety**: Functions check input types and raise appropriate errors
- **Domain Validation**: Mathematical constraints are validated (e.g., no negative square roots, no division by zero)

## Error Handling Patterns Implemented

### 1. Custom Exception Classes

```python
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
    """Raised when input is outside the valid domain."""
    pass
```

### 2. Input Type Validation

Every function validates input types before processing:

```python
if not isinstance(numerator, (int, float)):
    raise InvalidInputError(
        f"Numerator must be a number, got {type(numerator).__name__}: {numerator}"
    )
```

### 3. Domain-Specific Validation

Functions check mathematical constraints:

```python
if denominator == 0:
    raise DivisionError(
        "Cannot divide by zero. Division by zero is undefined in mathematics."
    )
```

### 4. Clear, Actionable Error Messages

All errors include:
- What went wrong
- What was received
- How to fix it (when applicable)

Example:
```python
raise IndexError(
    f"Index {index} is out of bounds for list of length {len(data)}. "
    f"Valid indices are 0 to {len(data) - 1}."
)
```

### 5. Edge Case Handling

Special cases are explicitly handled:
- 0^0 (mathematically undefined)
- Negative bases with fractional exponents
- Empty lists
- Extremely large values

## Functions

| Function | Purpose | Error Handling |
|----------|---------|----------------|
| `safe_divide()` | Division with zero checking | Validates types, checks for division by zero |
| `calculate_average()` | Calculate mean of numbers | Validates list, checks for empty list, validates all elements |
| `calculate_square_root()` | Square root calculation | Checks for negative numbers, validates types |
| `calculate_factorial()` | Factorial calculation | Validates integer input, checks for negative numbers, limits size |
| `calculate_power()` | Exponentiation | Handles 0^0, negative bases, overflow |
| `find_nth_element()` | Safe list indexing | Validates index bounds, checks for empty lists |
| `calculate_percentage()` | Percentage calculation | Checks for zero denominator, validates positive values |

## Usage Examples

### Successful Operation
```python
result = safe_divide(10, 2)
print(result)  # Output: 5.0
```

### Error Handling
```python
try:
    result = safe_divide(10, 0)
except DivisionError as e:
    print(f"Error: {e}")
    # Output: Error: Cannot divide by zero. Division by zero is undefined in mathematics.
```

## Running Tests

Run the test suite to see error handling in action:

```bash
python test_math_utils.py
```

The test suite demonstrates:
- ✓ Successful operations
- ✓ Expected error conditions being caught
- ✓ Clear error messages being displayed

## Key Benefits of This Approach

1. **Debugging**: Clear error messages make it easy to identify and fix issues
2. **User Experience**: Users understand what went wrong and how to fix it
3. **Maintainability**: Custom exceptions make code easier to maintain
4. **Robustness**: Input validation prevents unexpected behavior
5. **Documentation**: Error messages serve as inline documentation

## Best Practices Applied

- ✅ Always validate inputs before processing
- ✅ Use custom exception classes for different error categories
- ✅ Include context in error messages (what was expected vs. what was received)
- ✅ Provide actionable guidance in error messages
- ✅ Handle edge cases explicitly
- ✅ Use try-except blocks to catch unexpected errors
- ✅ Document expected exceptions in docstrings
- ✅ Fail fast with clear errors rather than producing incorrect results
