# ICE 2: Fundamentals of Testing

**Course**: INFT 1207-02  
**Instructor**: Md Al Maruf  
**Task Type**: Individual Assignment

---

## Overview

This assignment focuses on writing unit tests using Python's `unittest` module to implement a `find_minimum()` function that finds the minimum element in a list of integers. Your task is to write Python code that passes all the given test cases by correctly handling various input scenarios.

You are required to implement **boundary value analysis** and **robustness testing**.

---

## Instructions

1. **Create a Project Folder**:
   - Create a folder named `ICE2_Project` in your working directory.
   
2. **Inside the `ICE2_Project` Folder**:
   - Create two files: 
     - `main.py` for the source code.
     - `test_minimum.py` for the test cases.
3. **Function to Implement**: You need to implement the `find_minimum()` function in the `main.py` which:
    - Reads a list of elements (split by space).
    - Ensures the input elements are integers.
    - Returns the smallest integer without using Python’s built-in `min()` function.
    - Handles invalid input and raises exceptions where necessary.
4. **Unit Tests**: You will be using the `unittest` framework in `test_minimum.py`. You are provided with a set of test cases that your solution should pass.

---

## Task Breakdown

### Test Cases

The following test cases should be covered:

1. **Test Case 1**: A very short list (1 to 3 elements).
2. **Test Case 2**: An empty list.
3. **Test Case 3**: A list where the minimum element is the first or last element.
4. **Test Case 4**: A list with negative numbers.
5. **Test Case 5**: A list where all elements are negative.
6. **Test Case 6**: A list where some elements are real numbers.
7. **Test Case 7**: A list with alphabetic characters or special characters.
8. **Test Case 8**: A list with duplicate elements.
9. **Test Case 9**: A list with a very large number.

---

## Example Provided  `main.py`

Inside `main.py`, add the following code. It includes the initial structure for the `find_minimum()` function. One test case is already implemented, and you need to modify the function to handle the rest.

```python
# main.py
def find_minimum(elements):
    if not elements:
        raise ValueError("The list is empty")
    
    min_element = None
    # ---------------
    # ---------------
    
    return min_element
```
And the corresponding test:

## Write the Test Cases (`test_minimum.py`)
In `test_minimum.py`, we will write all the test cases using the unittest framework. Initially, only Test Case 1 will pass. Your task is to modify the function in main.py to pass the remaining test cases.

```python
# test_minimum.py
import unittest
from main import find_minimum  # Importing the function from main.py

class TestMinimumFunction(unittest.TestCase):

    def test_case_1(self):
        # Test Case 1: Very short list with 1, 2, or 3 elements (This will pass)
        self.assertEqual(find_minimum(["90"]), 90)  # Single element
        self.assertEqual(find_minimum(["12", "10"]), 10)  # Two elements
        self.assertEqual(find_minimum(["36", "14", "12"]), 12)  # Three elements

    def test_case_2(self):
        # Test Case 2: Empty list
        with self.assertRaises(ValueError):
            find_minimum([])

    def test_case_3(self):
        # Test Case 3: Minimum element is the first or last
        self.assertEqual(find_minimum(["10", "23", "34", "81", "97"]), 10)
        self.assertEqual(find_minimum(["97", "81", "34", "23", "10"]), 10)

    def test_case_4(self):
        # Test Case 4: List with negative elements
        self.assertEqual(find_minimum(["10", "-2", "5", "23"]), -2)
        self.assertEqual(find_minimum(["10", "-2", "-24", "4"]), -24)

    def test_case_5(self):
        # Test Case 5: All elements are negative
        self.assertEqual(find_minimum(["-23", "-31", "-45", "-56"]), -56)
        self.assertEqual(find_minimum(["-6", "-203", "-2", "-78"]), -203)

    def test_case_6(self):
        # Test Case 6: List with some real numbers
        with self.assertRaises(ValueError):
            find_minimum(["23", "34.56", "67", "33"])

    def test_case_7(self):
        # Test Case 7: List with alphabetic and special characters
        with self.assertRaises(ValueError):
            find_minimum(["23", "hi", "32", "1"])
        with self.assertRaises(ValueError):
            find_minimum(["12", "&", "*", "34m", "!"])

    def test_case_8(self):
        # Test Case 8: List with duplicate elements
        self.assertEqual(find_minimum(["3", "4", "6", "9", "6"]), 3)
        self.assertEqual(find_minimum(["13", "6", "6", "9", "15"]), 6)

    def test_case_9(self):
        # Test Case 9: List with one large number
        self.assertEqual(find_minimum(["530", "429449672", "97", "23", "46", "59"]), 23)

if __name__ == "__main__":
    unittest.main()

               
```

Now, Run Your Test Cases file `test_minimum.py`. You will find only one test is passed and the remaining is failed.
               
```
Traceback (most recent call last):
...
----------------------------------------------------------------------
Ran 9 tests, 1 passed, 8 failed.
```
## Your Task:
- Modify find_minimum() in main.py to pass the remaining test cases.
- Handle edge cases like:
    - Negative numbers
    - Invalid inputs (real numbers, alphabetic characters)
    - Empty lists
    - Duplicates
- Rerun your tests after each change until all tests pass.
               
## Submission Guideline:
- Submit your code: Upload main.py and test_minimum.py to DC Connect Dropbox
- Screenshots: Submit screenshots of your terminal or IDE showing all test cases passing.
- Deadline: Ensure to submit by the due date as mentioned in your course outline.

  
                                        
