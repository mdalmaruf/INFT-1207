# ICE 5: Selenium Locating Strategies

This assignment involves creating a Selenium test automation script in Python to register and log in a user on the Guru99 demo site. Follow these step-by-step instructions to set up and run the project in PyCharm.

## Project Setup

### Step 1: Create Project and Virtual Environment
1. Open **PyCharm** and create a new project named `ICE5`.
2. In the terminal, set up a virtual environment named `selenium-env` for the project.
   - **Install the virtual environment package** (if not already installed):
     ```bash
     python -m pip install virtualenv
     ```
   - **Create the virtual environment**:
     ```bash
     python -m venv selenium-env
     ```
   - **Activate the environment**:
     - On Windows:
       ```bash
       selenium-env\Scripts\activate
       ```
   - **If already installed**: Simply activate the environment.

### Step 2: Install Required Libraries
1. While the environment is activated, install the necessary libraries:
   ```bash
   pip install selenium pytest
   ```

## Step 2: Create Test Folder and Test File
1. Inside the project folder `ICE5`, create a new folder called `test`.
2. Within the `test` folder, create a Python file named `test_cases.py`.

## Code Implementation

### Step 3: Define Test Cases in `test_cases.py`

#### Register User Test Case:
- Navigate to the registration page at [Guru99 Registration](http://demo.guru99.com/test/newtours/).
- Locate and fill in each input field (e.g., First Name, Last Name, Phone, etc.) using Selenium locators such as ID, Name, XPath, or CSS Selectors.
- Submit the form to create a new user with your first name and password.

#### Login and Assertion Test Case:
- Log in to the site using the credentials created in the registration step.
- Use assertions to verify that the login is successful.

### Example Code Structure for `test_cases.py`

Organize your code into functions for readability and maintainability:

```python

# Importing libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class Guru99Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Or specify the WebDriver path

    def test_register_user(self):
        driver = self.driver
        driver.get("http://demo.guru99.com/test/newtours/register.php")

        # Add registration steps here using locators
        # Example: driver.find_element(By.NAME, "firstName").send_keys("YourFirstName")
        # Add assertion to confirm registration success (customize as needed)

    def test_login_user(self):
        driver = self.driver
        driver.get("http://demo.guru99.com/test/newtours/")

        # Add login steps here and assert successful login
        # Example: driver.find_element(By.NAME, "userName").send_keys("YourFirstName")
        # Add assertion to verify login success (customize as needed)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
```


**Screenshots**: Take screenshots of the running test cases to include in your submission.


