# Lab 5: Selenium Python API for Element Interaction

Welcome to Lab 5! This lab focuses on using the Selenium Python API to automate a shopping workflow on the Magento e-commerce platform. Below, you’ll find detailed instructions and steps to complete the lab successfully.

---

## **Objective**
Learn and practice:
- Automating web interactions using Selenium.
- Writing test scripts to navigate, interact with web elements, and assert results.
- Working collaboratively in pairs to develop and document test automation scripts.

---
## **What is Selenium Python API?**
Selenium is a powerful open-source tool used for automating web browsers. It allows developers and testers to write scripts in various programming languages, including Python, to simulate user interactions with web applications. The **Selenium Python API** provides methods to:
- Locate web elements.
- Perform actions such as clicking, typing, or selecting.
- Extract data for validation.
- Automate workflows across different browsers like Chrome, Firefox, and Edge.

### **How Selenium Works**
- **WebDriver**: Acts as a bridge between your Python script and the web browser.
   - Example: ChromeDriver enables Selenium to interact with Google Chrome.
- **Browser Automation**: Uses commands to interact with web elements like buttons, text fields, and dropdowns.
- **Locators**: Identifies web elements using:
   - ID
   - Name
   - XPath
   - CSS Selector
   - Link Text
- **Assertions**: Validates expected outcomes in automated workflows.

## **Setup Instructions**
1. **Install Dependencies**:
   - Ensure Python and pip are installed on your system.
   - Install Selenium using pip:
     ```bash
     pip install selenium
     ```
   - Download the Chrome WebDriver matching your Chrome version and add it to your system’s PATH.

2. **Using PyCharm**:
   - Open PyCharm and create a new project for Lab 5:
     - Go to **File > New Project**.
     - Name the project `Lab5_GroupN` (replace `N` with your group number).
   - Inside the project, create a new Python file:
     - Name the file `Lab5_firstname1_firstname2.py` (replace with both group members' names).
   - Set up a virtual environment if necessary:
     - Go to **File > Settings > Project > Python Interpreter** and select or create a new virtual environment.
   - Install Selenium in the PyCharm terminal:
     ```bash
     pip install selenium
     ```

3. **Group Formation**:
   - Work in pairs to complete this lab.
   - Both partners must actively participate in coding and recording tasks.

---

## **Program Requirements**
### **Workflow Overview**
Automate the following shopping workflow:
1. Navigate to [Magento Demo Website](https://magento.softwaretestingboard.com/).
2. Perform shopping steps:
   - **Women > Tops > Hoodies & Sweatshirts**.
   - Filter products by:
     - Style: Pullover
     - Size: M
     - Price: $50.00 - $59.99
     - Color: Purple
     - Material: Polyester
   - Select a product and add it to the cart.
   - Proceed to checkout and assert the order summary.

3. Close the browser after completing the automation.

---

## **Steps to Complete the Lab**

### 1. **Navigate to the Product Page**
- Use Selenium’s `find_element` method to locate and click:
  - **"Women" menu**.
  - **"Tops" category**.
  - **"Hoodies & Sweatshirts"**.

### 2. **Filter Products**
- Apply filters for style, size, price, color, and material:
  - Use **XPath** or **CSS Selectors** to locate dropdowns or checkboxes.
  - Example code to select a filter:
    ```python
    style_filter = driver.find_element(By.XPATH, "//span[text()='Pullover']")
    style_filter.click()
    ```

### 3. **Select and Add to Cart**
- Select a filtered product and add it to the cart:
  - Handle **frames** if required:
    ```python
    driver.switch_to.frame("frame_name")
    add_to_cart_button = driver.find_element(By.ID, "add-to-cart")
    add_to_cart_button.click()
    driver.switch_to.default_content()
    ```

### 4. **View Cart and Proceed to Checkout**
- Click the cart icon and proceed to checkout:
  ```python
  cart_icon = driver.find_element(By.ID, "cart-icon")
  cart_icon.click()
  checkout_button = driver.find_element(By.XPATH, "//button[text()='Proceed to Checkout']")
  checkout_button.click()
  ```
### 5. **Assert the Order Summary**
- Validate the product in the order summary using `assert`:
  ```python
  order_summary = driver.find_element(By.CLASS_NAME, "order-summary")
  assert "Pullover" in order_summary.text, "Order summary does not include the selected item"
  ```
### 5. **Close the Browser**
- Ensure the browser closes after the test completes:
  ```bash
  driver.quit()
  ```

## **General Requirements**
- **Test-Case Fixtures**: Write separate test cases for each step to maintain modularity.
- **Comments**: Add meaningful comments explaining your code and element selections.
- **Video Recording**:
  - Showcase the workflow on the Magento website.
  - Explain your code and logic during the recording.
- **File Submission**: Zip your project folder and submit as required.

---

## **Example Code Structure**
```python
from selenium import webdriver
from selenium.webdriver.common.by import By

# Test Case 1: Navigate to Product Page
def test_navigate_to_product_page(driver):
    driver.get("https://magento.softwaretestingboard.com")
    driver.find_element(By.LINK_TEXT, "Women").click()
    driver.find_element(By.LINK_TEXT, "Tops").click()
    driver.find_element(By.LINK_TEXT, "Hoodies & Sweatshirts").click()

# Test Case 2: Apply Filters
def test_apply_filters(driver):
    driver.find_element(By.XPATH, "//span[text()='Pullover']").click()
    driver.find_element(By.XPATH, "//span[text()='M']").click()
    driver.find_element(By.XPATH, "//span[text()='Purple']").click()

# Test Case 3: Add to Cart and Assert
def test_add_to_cart(driver):
    driver.find_element(By.XPATH, "//button[text()='Add to Cart']").click()
    cart_icon = driver.find_element(By.ID, "cart-icon")
    cart_icon.click()
    assert "Pullover" in driver.find_element(By.CLASS_NAME, "order-summary").text

```

#Sample Working Example:
   ```python
   from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Test setup
def setup_driver():
    driver = webdriver.Chrome()  # Ensure the ChromeDriver is installed and in PATH
    driver.maximize_window()
    driver.get("https://magento.softwaretestingboard.com/")
    return driver

# Test Case 1: Navigate to Product Category
def test_navigate_to_category(driver):
    print("Navigating to Women -> Tops -> Hoodies & Sweatshirts")
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Women"))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Tops"))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Hoodies & Sweatshirts"))
    ).click()

# Test Case 2: Apply Filters
def test_apply_filters(driver):
    print("Applying filters: Style: Pullover, Size: M, Color: Purple, Price: $50-$59.99, Material: Polyester")
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Pullover']"))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='M']"))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Purple']"))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Polyester')]"))
    ).click()

# Test Case 3: Select Product and Add to Cart
def test_add_to_cart(driver):
    print("Selecting a product and adding to the cart")
    product = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'product-item-link')]"))
    )
    product.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@title='Add to Cart']"))
    ).click()

# Test Case 4: View Cart and Proceed to Checkout
def test_checkout(driver):
    print("Proceeding to checkout")
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'showcart')]"))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@title='Proceed to Checkout']"))
    ).click()

# Test Case 5: Validate Order Summary
def test_validate_order_summary(driver):
    print("Validating the order summary")
    summary = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "block-summary"))
    )
    assert "Pullover" in summary.text, "Order Summary does not contain the selected product"

# Main function to run all test cases
def main():
    driver = setup_driver()
    try:
        test_navigate_to_category(driver)
        test_apply_filters(driver)
        test_add_to_cart(driver)
        test_checkout(driver)
        test_validate_order_summary(driver)
        print("Test completed successfully!")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()

    ```


# Tips and Best Practices

## **Tips and Best Practices**
1. Use **ChroPath** to identify precise locators.
2. Modularize your code by dividing the workflow into separate test cases.
3. Verify all selectors and test thoroughly to ensure accuracy.
4. Collaborate effectively with your partner and document task distribution.

---

## **Common Challenges and Solutions**

### **Issue: Unable to locate an element**
- **Solution**: Use ChroPath to refine the locator and ensure the page is fully loaded before interaction.

### **Issue: Filters not applying correctly**
- **Solution**: Use explicit waits to ensure all elements are interactable:
  ```python
  from selenium.webdriver.support.ui import WebDriverWait
  from selenium.webdriver.support import expected_conditions as EC

  element = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.XPATH, "//button[text()='Add to Cart']"))
  )
  ```
# Submission Guidelines

## **File Format**
- Submit `Lab5_firstname1_firstname2.py` following naming conventions.

## **Video**
- Record a clear demonstration of your code and test execution.

## **Upload**
- Attach the zipped project folder to the assignment folder.
