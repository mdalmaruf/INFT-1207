# INFT 1207 - Test Automation of Banking Project

## Overview
This project involves automated testing of a **banking demo website** using **Selenium WebDriver with Python**. It simulates a corporate environment where the team is responsible for testing several modules of the banking system before its release.

## Demo Website
- **Website:** [http://demo.guru99.com/V4/](http://demo.guru99.com/V4/)
- **Login Credentials:** 
  - Visit [http://demo.guru99.com](http://demo.guru99.com) and enter your email to receive temporary credentials.  
  - Example credentials:  
    - **User ID:** mngr160860  
    - **Password:** pumagEm  
- Credentials are valid for **20 days**. Generate new ones if they expire.

## Project Scope
Your team will automate and test the following **Manager Role Modules**:

1. **New Customer**  
2. **Edit Customer**  
3. **Delete Customer**  
4. **New Account**  
5. **Edit Account**  
6. **Delete Account**  
7. **Balance Enquiry**  
8. **Mini Statement**  
9. **Customized Statement**

Each module has several test cases that must be executed to verify functionality.

---

## Project Tasks

### 1. Group Formation (Weeks 6-7)
- Form a team of **up to 4 members**.
- If needed, contact the professor for assistance in forming a group.
- Plan the task distribution equally among team members and document it in the **Project Report**.

### 2. Automation Setup (Weeks 8-12)
- **Start coding** using Python and Selenium to automate the test cases.
- Implement a **menu-driven program (`testsuite.py`)** to allow module-based test case execution.
- **Divide the 120 test cases** across members as follows:
  - New Customer: 28 cases
  - Edit Customer: 20 cases
  - Delete Customer: 8 cases
  - New Account: 16 cases
  - Edit Account: 8 cases
  - Delete Account: 8 cases
  - Balance Enquiry: 7 cases
  - Mini Statement: 8 cases
  - Customized Statement: 17 cases

### 3. Testing and Bug Tracking
- Execute all test cases and **record the results** in the provided **Test Case Suite Excel sheet**.
- Export **HTML results** for each test run.
- Log **failed tests** in the **Bug Tracker Report** for developers to address.

---

## Submission Requirements

### Files to Submit
1. **Source Code:** Submit all project files as a **zipped folder** named:  
   `INFT 1207 - Group#Project.zip`
2. **Video Recordings:** Each member records and explains their part of the project. Use one of the following naming conventions:
   - **Single recording:** `INFT 1207 - Group#ProjectRecording`
   - **Individual recordings:** `INFT 1207 - Group#Firstname`
3. **Test Results:** Export results to **HTML**.
4. **Test Case Suite:** Complete the provided Excel sheet with actual results and pass/fail status.  
   Name the file:  
   `INFT 1207 - Group#TestCasesuitesolution`
5. **Bug Tracker Report:** Use the provided template for any failed tests and submit as:  
   `INFT 1207 - Group#Bug Tracker Report`
6. **Project Report:** Submit the project report in **PDF** format named:  
   `INFT 1207 - Group#Projectreport`

### Demo Presentation (Week 14)
- **All team members must be present** during the demo. Failure to attend will result in **zero marks** for the absent member.
- The professor will ask team members to **execute specific test cases** during the demo.

---

## Grading Criteria (Total: 100 Marks)
| **Criteria**                                 | **Marks** |
|----------------------------------------------|-----------|
| Naming convention followed                   | 5         |
| Test Case Execution (0.42 marks per case)    | 50        |
| Completed Test Case Suite (Excel)            | 20        |
| HTML Test Results                            | 10        |
| Video Recordings (Single: 10 or 2.5 each)    | 10        |
| Bug Tracker Report                           | 5         |

---

## Important Notes
- Use **Week 13** to complete the project with assistance from the professor.
- If a group member fails to contribute, they will not receive marks, and the rest of the team will incur a **5% penalty**.
- Peer evaluation is mandatory, where each member will evaluate their teammates.

---

## How to Run the Project
1. Install **Python** and **Selenium WebDriver**.
2. Clone the repository and navigate to the project folder.
3. Install required dependencies using:
   ```bash
   pip install selenium
   ```
4. Run the menu-driven test suite using:
  ```bash
  python testsuite.py
  ```
5. Export the test results and generate HTML reports.



