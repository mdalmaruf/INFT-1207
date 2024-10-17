# Lab 3: Unit Testing - INFT 1207

## Project Overview
This project involves calculating the areas of four shapes:
- **Circle**
- **Trapezium**
- **Ellipse**
- **Rhombus**

Additionally, it contains a **menu-driven test suite** to allow users to select the shape they want to test. The goal is to fix the provided code, add support for new shapes, and implement unit tests using Python’s `unittest` framework.

---

## Instructions and Steps

### 1. Set Up the Project in PyCharm
1. Open **PyCharm** and create a new **Python Project**. Name it `Lab3_GroupN` (replace `N` with your group number).
2. Inside the project folder, create two subdirectories:
   - `app` (to store the application code)
   - `test` (to store the test code)
3. Create the following files:
   - In the **app** folder: `Lab3_firstname1_firstname2.py`
   - In the **test** folder: `test_Lab3_firstname1_firstname2.py`
   - At the project root: `test_suite.py`

---

### 2. Application Code (Lab3_firstname1_firstname2.py)
Place the following code in **`app/Lab3_firstname1_firstname2.py`**:

```python
from math import pi

def circle_area(r):
    if isinstance(r, (int, float)) and r >= 0:
        return pi * (r ** 2)
    else:
        raise ValueError("Invalid radius. Must be a non-negative number.")

def trapezium_area(a, b, h):
    if a > 0 and b > 0 and h > 0:
        return 0.5 * (a + b) * h
    else:
        raise ValueError("Invalid dimensions. All must be positive numbers.")

def ellipse_area(a, b):
    if a > 0 and b > 0:
        return pi * a * b
    else:
        raise ValueError("Invalid dimensions. All must be positive numbers.")

def rhombus_area(d1, d2):
    if d1 > 0 and d2 > 0:
        return 0.5 * d1 * d2
    else:
        raise ValueError("Invalid diagonals. All must be positive numbers.")
```

---

### 3. Unit Test Code (test_Lab3_firstname1_firstname2.py)
Place the following code in **`test/test_Lab3_firstname1_firstname2.py`**:

```python
import unittest
from app.Lab3_firstname1_firstname2 import circle_area, trapezium_area, ellipse_area, rhombus_area

class TestShapes(unittest.TestCase):

    def setUp(self):
        print("Setup: Preparing tests...")

    def tearDown(self):
        print("Teardown: Cleaning up after tests...")

    def test_circle_area_valid(self):
        self.assertAlmostEqual(circle_area(3), 28.274333882308138)

    def test_circle_area_invalid(self):
        with self.assertRaises(ValueError):
            circle_area(-1)

    def test_trapezium_area_valid(self):
        self.assertEqual(trapezium_area(3, 4, 5), 17.5)

    def test_trapezium_area_invalid(self):
        with self.assertRaises(ValueError):
            trapezium_area(-1, 4, 5)

    def test_ellipse_area_valid(self):
        self.assertAlmostEqual(ellipse_area(3, 4), 37.69911184307752)

    def test_ellipse_area_invalid(self):
        with self.assertRaises(ValueError):
            ellipse_area(0, -2)

    def test_rhombus_area_valid(self):
        self.assertEqual(rhombus_area(4, 5), 10.0)

    def test_rhombus_area_invalid(self):
        with self.assertRaises(ValueError):
            rhombus_area(-4, 5)

if __name__ == "__main__":
    unittest.main()
```

---

### 4. Menu-Driven Test Suite (test_suite.py)
Add the following code to **`test_suite.py`**:

```python
import unittest

def run_tests(choice):
    if choice == 'c':
        suite = unittest.defaultTestLoader.loadTestsFromName('test.test_Lab3_firstname1_firstname2.TestShapes.test_circle_area_valid')
    elif choice == 't':
        suite = unittest.defaultTestLoader.loadTestsFromName('test.test_Lab3_firstname1_firstname2.TestShapes.test_trapezium_area_valid')
    elif choice == 'e':
        suite = unittest.defaultTestLoader.loadTestsFromName('test.test_Lab3_firstname1_firstname2.TestShapes.test_ellipse_area_valid')
    elif choice == 'r':
        suite = unittest.defaultTestLoader.loadTestsFromName('test.test_Lab3_firstname1_firstname2.TestShapes.test_rhombus_area_valid')
    else:
        print("Invalid choice. Exiting.")
        return

    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    print("Enter a shape to test ('c' for Circle, 't' for Trapezium, 'e' for Ellipse, 'r' for Rhombus):")
    choice = input().strip().lower()
    run_tests(choice)
```

---

### 5. Project Structure
```
Lab3_GroupN/
│
├── app/
│   └── Lab3_firstname1_firstname2.py  # Application code for area calculations
│
├── test/
│   └── test_Lab3_firstname1_firstname2.py  # Unit tests for shapes
│
├── test_suite.py  # Menu-driven test suite
│
└── README.md  # Project instructions
```

---

### 6. How to Run the Project

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/Lab3_GroupN.git
   cd Lab3_GroupN
   ```

2. **Install dependencies** (if any):
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app/Lab3_firstname1_firstname2.py
   ```

4. **Run the tests**:
   ```bash
   python test/test_Lab3_firstname1_firstname2.py
   ```

5. **Run the menu-driven test suite**:
   ```bash
   python test_suite.py
   ```

---

### 7. Test Case Documentation
Create a **test case design document** that includes:
- **Test case ID**
- **Description**
- **Input values**
- **Expected output**
- **Actual output**
- **Pass/Fail status**

---

### 8. Submission Guidelines

1. **Zip the project folder** containing:
   - Application code
   - Test code
   - Test suite
   - `README.md`
   - Test case document

2. **Submit a video** where each partner explains:
   - Code implementation
   - Test design and results
   - Task distribution

---

### 9. Team Members
- **Student 1**: Firstname1 Lastname1
- **Student 2**: Firstname2 Lastname2

---

### 10. License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



