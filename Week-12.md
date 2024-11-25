# Selenium Python Testing Tutorial

This tutorial demonstrates the use of Selenium WebDriver for automating web application testing. Students will use PyTest and Unittest frameworks for test execution. The examples handle elements such as radio buttons, checkboxes, and date pickers.

---

## Prerequisites

1. **Python**: Version 3.8 or above installed.
2. **PyCharm IDE**: Installed for development.
3. **Required Libraries**: Install the following in your terminal:
```bash
   pip install selenium webdriver-manager pytest
```
# Project Setup

Follow the steps below to set up the project:

## 1. Create a New Project
- Open **PyCharm** and create a new project.

## 2. Create a Folder for Selenium Tests
- Inside the project folder, create a new folder named `selenium_tests`.

## 3. Add Python Files
- Under the `selenium_tests` folder, create the following Python files:
  - `handling_radiobutton.py`
  - `handling_checkbox.py`
  - `handling_dates.py`

## 4. Install Dependencies
- Open the terminal inside PyCharm and run the following command:

```bash
pip install selenium webdriver-manager pytest
```

# Files in the Repository

- **`handling_radiobutton.py`**: Demonstrates how to interact with radio buttons.
- **`handling_checkbox.py`**: Illustrates checkbox interactions.
- **`handling_dates.py`**: Handles date selection in calendar widgets.

# Running the Tests

# Using Unittest
The `unittest.main()` function automatically detects and runs all test cases defined in the script when you execute the file using python filename.py.
For example, to run `handling_radiobutton.py`, you simply use:

```bash
python selenium_tests/handling_radiobutton.py
```
## Alternatively when Using PyTest
1. Open the terminal in the project directory.
2. Run the following command:
```bash
   pytest selenium_tests/handling_radiobutton.py
```

# Code Explanation

## Handling Radio Buttons (`handling_radiobutton.py`)

### Code:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class RadioButtonDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.maximize_window()

    def test_radiobutton(self):
        driver = self.driver
        driver.get("http://demo.guru99.com/test/radio.html")

        # Select Radio Button 1
        driver.find_element(By.ID, "vfb-7-1").click()
        print("Radio Button 1 Selected")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
```
### Steps:

1. Use `webdriver_manager` to manage the Chrome driver.
2. Open a test site for radio buttons.
3. Interact with a radio button using its ID.

## Handling Checkboxes (`handling_checkbox.py`)

### Code:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class CheckboxDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.maximize_window()

    def test_checkboxes(self):
        driver = self.driver
        driver.get("http://demo.guru99.com/test/radio.html")

        # Select a Checkbox
        checkbox = driver.find_element(By.ID, "vfb-6-0")
        checkbox.click()
        print("Checkbox Selected")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
```
### Steps:
1. Navigate to a site with checkboxes.
2. Select and print the checkbox interaction.

   ## Handling Dates (`handling_dates.py`)

### Code:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class DatePickerDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.maximize_window()

    def test_datepicker(self):
        driver = self.driver
        driver.get("https://example.com/date-picker")

        # Select a date
        date_field = driver.find_element(By.ID, "datepicker")
        date_field.click()
        date_to_select = driver.find_element(By.XPATH, "//td[@data-day='15']")
        date_to_select.click()
        print("Date Selected")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
```
### Steps:

1. Automate date selection from a calendar.
2. Use XPath to identify and click a specific date.

This tutorial demonstrates the use of Selenium for automating repetitive tasks like selecting options, checking boxes, and handling calendars. Use this knowledge to test web applications effectively.
