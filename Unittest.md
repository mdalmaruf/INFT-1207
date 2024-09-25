
# Activity 1: Python Calculator with Automated Testing

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
```bash
python -m venv venv
source venv/bin/activate      # On macOS/Linux
venv\Scripts\activate         # On Windows
```

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```
### Alternatively you can create from the scratch
#### Create a New Python Project in PyCharm

1. Open PyCharm.
2. Click on `File > New Project`.
3. Choose a location for your project.
4. Click **Create**.

#### Write a Simple Python Program

We'll create a simple program that has two functions: one to add two numbers and another to check if a number is even.

In the PyCharm project, create a new Python file:

1. Right-click the project folder, choose `New > Python File`.
2. Name the file `calculator.py`.
3. Add the following code to `calculator.py`:

```python
# calculator.py

def add(a, b):
    """
    Returns the sum of two numbers.
    """
    return a + b

def is_even(number):
    """
    Returns True if the number is even, False otherwise.
    """
    return number % 2 == 0
```

### 2. Writing Automated Test Cases

Now, let's write some tests to automatically verify that the `add()` and `is_even()` functions work correctly.

Create a new Python file for the tests:

1. Right-click the project folder, choose `New > Python File`.
2. Name the file `test_calculator.py`.
3. Add the following test cases to `test_calculator.py`:

Alternatively, you can hover on the function name and right click of you mouse to generate the test cases for each of the function. The function should look like the followings:

```python
# test_calculator.py

import unittest
from calculator import add, is_even

class TestCalculator(unittest.TestCase):

    def test_add(self):
        """
        Test if add() returns the correct sum.
        """
        self.assertEqual(add(2, 3), 5)   # 2 + 3 should equal 5
        self.assertEqual(add(-1, 1), 0)  # -1 + 1 should equal 0

    def test_is_even(self):
        """
        Test if is_even() correctly identifies even numbers.
        """
        self.assertTrue(is_even(4))    # 4 is even
        self.assertFalse(is_even(5))   # 5 is not even

# This is needed for command-line execution, not required for PyCharm's inbuilt test runner.
if __name__ == "__main__":
    unittest.main()

```

### 3. Running the Program

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

### 4. Running Automated Tests

We use the `unittest` module to automate the testing process.

To run the tests, use the following command:

```bash
python -m unittest test_calculator.py
```

Alternatively, you can run tests using PyCharm's built-in test runner.

### 5. Test Output
If all tests pass, you will see something like this:

Ran 2 tests in 0.001s

Ok

If any test fails, you will see a detailed error message indicating what went wrong.

### 6. Tests Overview

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

