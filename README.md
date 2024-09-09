
# Python Calculator with Automated Testing

This repository contains a simple Python program that includes two functions:
- `add(a, b)`: Adds two numbers and returns the result.
- `is_even(number)`: Checks if a number is even and returns `True` or `False`.

Automated tests for these functions are implemented using the `unittest` framework. The tests ensure that both the `add()` and `is_even()` functions work as expected.

## Project Structure

├── calculator.py   # Python program with two functions  
├── test_calculator.py   # Unit tests for the functions  
├── README.md   # This file

## Prerequisites

- Python 3.x installed
- A virtual environment is recommended but not required

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```
### 2. Create a virtual environment (optional)

```bash
python -m venv venv
source venv/bin/activate      # On macOS/Linux
venv\Scripts\activate         # On Windows
```

### 3. Install required packages (if any)

This project does not require any external packages, but ensure you have Python installed.

### 4. Running the Program

To run the program, open `calculator.py` and add the necessary function calls, or execute it manually:

```python
# Example usage:
from calculator import add, is_even

print(add(2, 3))          # Output: 5
print(is_even(4))         # Output: True
```

Run the Python file directly:

```bash
python calculator.py
```

### 5. Running Automated Tests

We use the `unittest` module to automate the testing process.

To run the tests, use the following command:

```bash
python -m unittest test_calculator.py
```

Alternatively, you can run tests using PyCharm's built-in test runner.

### Test Output
If all tests pass, you will see something like this:

Ran 2 tests in 0.001s

Ok

If any test fails, you will see a detailed error message indicating what went wrong.

### Tests Overview

- `test_add()`: Ensures that the `add()` function correctly adds two numbers.
- `test_is_even()`: Ensures that the `is_even()` function correctly identifies even numbers.

Example test file: `test_calculator.py`

```python
import unittest
from calculator import add, is_even

class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(5))

if __name__ == "__main__":
    unittest.main()
```
