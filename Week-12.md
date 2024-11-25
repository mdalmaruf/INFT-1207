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

```python
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class RadioButtonDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    def test_radiobutton(self):
        driver = self.driver
        driver.get("http://demo.guru99.com/test/radio.html")
        time.sleep(5)

        # Select Radio Button 1
        radio_button = driver.find_element(By.ID, "vfb-7-1")
        radio_button.click()
        time.sleep(2)
        print("Radio Button 1 Selected")

        # Assert that the radio button is selected
        self.assertTrue(radio_button.is_selected(), "Radio Button 1 is not selected")

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

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class CheckboxDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

   def test_checkboxes(self):
        driver = self.driver
        driver.get("http://demo.guru99.com/test/radio.html")
        time.sleep(5)
        # Select a Checkbox
        checkbox = driver.find_element(By.ID, "vfb-6-0")
        checkbox.click()
        time.sleep(2)
        print("Checkbox Selected")

        # Assert that the checkbox is selected
        self.assertTrue(checkbox.is_selected(), "Checkbox is not selected")

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

```python
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class DatePickerDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Initialize the Chrome WebDriver
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    def test_datepicker(self):
        driver = self.driver
        # Using a publicly available demo site with a date picker
        driver.get("https://jqueryui.com/datepicker/")

        # Switch to the iframe containing the date picker
        driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "demo-frame"))

        # Wait for the page to load
        time.sleep(5)

        # Interact with the date picker
        date_field = driver.find_element(By.ID, "datepicker")
        date_field.click()
        time.sleep(2)
        
        # Select a specific date (e.g., 15th of the current month)
        date_to_select = driver.find_element(By.XPATH, "//a[text()='15']")
        date_to_select.click()
        time.sleep(2)
       

        # Validate that the correct date is selected
        selected_date = date_field.get_attribute("value")
        expected_date = "11/15/2024"  # Adjust format based on your locale (MM/DD/YYYY)
        self.assertEqual(selected_date, expected_date, "Selected date is not as expected")
        print("Date Selected Successfully")

    @classmethod
    def tearDownClass(cls):
        # Quit the WebDriver
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()

```
### Steps:

   - The date picker on the demo site is inside an iframe. Selenium needs to switch to the iframe to interact with the elements inside:
      ```python
      driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "demo-frame"))
      ```
   - XPath is used to locate the desired date, e.g., the 15th:
      ```python
      date_to_select = driver.find_element(By.XPATH, "//a[text()='15']")
      date_to_select.click()
      ```


This tutorial demonstrates the use of Selenium for automating repetitive tasks like selecting options, checking boxes, and handling calendars. Use this knowledge to test web applications effectively.
