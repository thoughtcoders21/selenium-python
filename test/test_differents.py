import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class OrangeHRMLoginTest(unittest.TestCase):

    def setUp(self):
        # Initialize the WebDriver (Chrome in this case)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

    def test_login_valid_credentials(self):
        driver = self.driver

        # Locate the username field and enter the username
        username = driver.find_element(By.NAME, "username")
        username.send_keys("Admin")

        # Locate the password field and enter the password
        password = driver.find_element(By.NAME, "password")
        password.send_keys("admin123")

        # Locate the login button and click it
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()

        # Add some delay to wait for the page to load
        time.sleep(3)

        # Assertion to check if Dashboard is displayed
        dashboard = driver.find_element(By.XPATH, "//h6[text()='Dashboard']")
        self.assertTrue(dashboard.is_displayed(), "Login with valid credentials failed")

    def test_login_invalid_username(self):
        driver = self.driver

        # Locate the username field and enter an invalid username
        username = driver.find_element(By.NAME, "username")
        username.send_keys("InvalidUser")

        # Locate the password field and enter the password
        password = driver.find_element(By.NAME, "password")
        password.send_keys("admin123")

        # Locate the login button and click it
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()

        # Add some delay to wait for the page to load
        time.sleep(3)

        # Assertion to check if an error message is displayed
        error_message = driver.find_element(By.XPATH, "//p[contains(text(),'Invalid credentials')]")
        self.assertTrue(error_message.is_displayed(), "Login with invalid username did not show the expected error message")

    def test_login_invalid_password(self):
        driver = self.driver

        # Locate the username field and enter the username
        username = driver.find_element(By.NAME, "username")
        username.send_keys("Admin")

        # Locate the password field and enter an invalid password
        password = driver.find_element(By.NAME, "password")
        password.send_keys("InvalidPass")

        # Locate the login button and click it
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()

        # Add some delay to wait for the page to load
        time.sleep(3)

        # Assertion to check if an error message is displayed
        error_message = driver.find_element(By.XPATH, "//p[contains(text(),'Invalid credentials')]")
        self.assertTrue(error_message.is_displayed(), "Login with invalid password did not show the expected error message")

