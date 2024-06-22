python -m venv venv

pip install -r requirements.txt

python script_name.py

python test_orangehrm_login.py


This project automates the login process for the OrangeHRM site using Python and Selenium. It includes various test scenarios with assertions to validate the outcomes

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).
- Google Chrome browser installed.
- Basic knowledge of Python and Selenium.

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/orangehrm-selenium-automation.git
    cd orangehrm-selenium-automation
    ```

2. **Create and activate a virtual environment**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Install ChromeDriver**:

    The script uses `webdriver_manager` to automatically manage the ChromeDriver installation.


