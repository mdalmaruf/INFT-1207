
# Selenium WebDriver Guide

This guide provides an overview of essential Selenium WebDriver commands, including navigating web pages, locating web elements, and using the ChroPath extension for efficient locator strategies.

---

## Table of Contents
1. [Introduction to Selenium WebDriver](#introduction)
2. [ChroPath Extension](#chropath-extension)
3. [WebElement Commands](#webelement-commands)
4. [Browser and Navigation Commands](#browser-and-navigation-commands)
5. [Locator Strategies](#locator-strategies)
6. [Sample Script](#sample-script)
7. [Resources](#resources)
8. [Conclusion](#conclusion)

---

### Introduction

Selenium WebDriver is a powerful tool for automating web application testing. It allows testers to perform various actions on web elements and navigate through applications for end-to-end testing.

---

### ChroPath Extension

[ChroPath](https://chrome.google.com/webstore/category/extensions?hl=en) is a browser extension that assists in quickly identifying and verifying XPath and CSS selectors. This tool supports both Chrome and Firefox and provides an interface for editing, inspecting, and generating selectors for web elements.

**Usage:**
1. Install ChroPath from the Chrome Web Store.
2. Inspect elements and obtain their unique locators efficiently.

---

### WebElement Commands

Web elements in Selenium are HTML elements on a web page. Below are some commonly used commands with examples.

- **`get(url)`**: Launches an application by loading the specified URL.
  ```python
  driver.get("https://www.example.com")
  ```

- **`current_url`**: Retrieves the current URL of the page.
  ```python
  url = driver.current_url
  print("Current URL:", url)
  ```

- **`title`**: Retrieves the page title.
  ```python
  title = driver.title
  print("Page Title:", title)
  ```

- **`back()`**: Navigates to the previous page.
  ```python
  driver.back()
  ```

- **`forward()`**: Navigates to the next page if available.
  ```python
  driver.forward()
  ```

- **`refresh()`**: Reloads the page.
  ```python
  driver.refresh()
  ```

- **`maximize_window()`**: Maximizes the browser window.
  ```python
  driver.maximize_window()
  ```

- **`minimize_window()`**: Minimizes the browser window.
  ```python
  driver.minimize_window()
  ```

- **`close()`**: Closes the current window in focus.
  ```python
  driver.close()
  ```

- **`quit()`**: Closes all browser windows and ends the session.
  ```python
  driver.quit()
  ```

---

### Browser and Navigation Commands

Browser and navigation commands enable interaction with the browser itself, such as page refresh and window management.

| Command               | Description                                              | Example                                 |
|-----------------------|----------------------------------------------------------|-----------------------------------------|
| `refresh()`           | Reloads the current page.                                | `driver.refresh()`                      |
| `maximize_window()`   | Maximizes the current browser window.                    | `driver.maximize_window()`              |
| `minimize_window()`   | Minimizes the current browser window.                    | `driver.minimize_window()`              |
| `close()`             | Closes the active browser window.                        | `driver.close()`                        |
| `quit()`              | Closes all browser windows and ends the session.         | `driver.quit()`                         |

---

### Locator Strategies

Locators help identify elements on a web page, crucial for interaction. Selenium supports several locator strategies:

1. **CSS ID**: Locates an element by the unique ID.
   ```python
   element = driver.find_element(By.ID, "unique_id")
   ```

2. **Name Attribute**: Locates an element by the name attribute.
   ```python
   element = driver.find_element(By.NAME, "name_attribute")
   ```

3. **Link Text**: Locates an element by the exact link text.
   ```python
   element = driver.find_element(By.LINK_TEXT, "Full Link Text")
   ```

4. **Partial Link Text**: Locates an element by a partial match of the link text.
   ```python
   element = driver.find_element(By.PARTIAL_LINK_TEXT, "Partial Text")
   ```

5. **Class Name**: Locates an element by the class name.
   ```python
   element = driver.find_element(By.CLASS_NAME, "class_name")
   ```

6. **Tag Name**: Locates an element by the HTML tag.
   ```python
   element = driver.find_element(By.TAG_NAME, "tag_name")
   ```

7. **XPath**: Locates an element by an XPath expression.
   ```python
   element = driver.find_element(By.XPATH, "//div[@id='example']")
   ```

8. **CSS Selector**: Locates an element by a CSS selector.
   ```python
   element = driver.find_element(By.CSS_SELECTOR, "div.example")
   ```

---

### Sample Script

Here’s a basic Selenium script that utilizes WebDriver commands and locators:

```python
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class GoogleSearchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Initialize WebDriver (using Chrome in this example)
        cls.driver = webdriver.Chrome()
        
        # Maximize the browser window for better visibility of the test
        cls.driver.maximize_window()

    def test_google_search(self):
        # Step 1: Navigate to Google's homepage
        self.driver.get("https://www.google.com")
        sleep(5)  # Wait to ensure the page loads completely

        # Step 2: Locate the search box using the 'name' attribute and input the search term "Quantum Computing"
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys("Quantum Computing")
        sleep(5)  # Wait to observe the input being entered

        # Step 3: Locate the Google Search button by its 'name' and click it to perform the search
        search_button = self.driver.find_element(By.NAME, "btnK")
        search_button.click()
        sleep(5)  # Wait for the search results page to load

        # Step 4: Verify that the page title contains the search term "Quantum Computing"
        # Explanation:

        # - assertIn checks if "Quantum Computing" is a substring of the page title (self.driver.title).
        # - If "Quantum Computing" is found in the title, the test passes.
        # - If not, the test fails, and the message "Title does not contain search term" is displayed.
        self.assertIn("Quantum Computing", self.driver.title, "Title does not contain search term")

        # Step 5: Print the current URL and page title for reference
        print("URL:", self.driver.current_url)
        print("Title:", self.driver.title)

    @classmethod
    def tearDownClass(cls):
        # Close the browser after all tests are done
        cls.driver.quit()

if __name__ == "__main__":
    # Run the test
    unittest.main()
```
---

### Resources

For further learning, refer to:
- *Learning Selenium Testing Tools with Python* by Unmesh Gundecha
- [Software Testing Material - Selenium Python Tutorial](https://www.softwaretestingmaterial.com/selenium-python-tutorial/)

---

### Conclusion

This guide covers essential Selenium WebDriver commands, locator strategies, and usage of ChroPath for efficient element inspection. By mastering these tools, you can build reliable and robust test automation scripts.
