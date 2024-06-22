import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

from Base import Base


class OrangeHRMTest(unittest.TestCase):

    def setUp(self):
        # Initialize the WebDriver (Chrome in this case)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

        # Perform login
        self.login("Admin", "admin123")

    def login(self, username, password):
        driver = self.driver
        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)

    def test_dashboard_elements(self):
        driver = self.driver
        self.assertTrue(driver.find_element(By.XPATH, "//h6[text()='Dashboard']").is_displayed(),
                        "Dashboard header is not displayed")
        self.assertTrue(driver.find_element(By.ID, "menu_dashboard_index").is_displayed(),
                        "Dashboard menu item is not displayed")

    def test_navigate_to_pim_module(self):
        driver = self.driver
        pim_menu = driver.find_element(By.ID, "menu_pim_viewPimModule")
        pim_menu.click()
        time.sleep(3)
        self.assertTrue(driver.find_element(By.XPATH, "//h6[text()='PIM']").is_displayed(),
                        "Failed to navigate to PIM module")

    def test_add_employee(self):
        driver = self.driver
        driver.find_element(By.ID, "menu_pim_viewPimModule").click()
        time.sleep(10)
        driver.find_element(By.ID, "menu_pim_addEmployee").click()
        time.sleep(10)

        driver.find_element(By.ID, "firstName").send_keys("John")
        driver.find_element(By.ID, "lastName").send_keys("Doe")
        driver.find_element(By.ID, "btnSave").click()
        time.sleep(10)

        self.assertTrue(driver.find_element(By.XPATH, "//h1[text()='Personal Details']").is_displayed(),
                        "Failed to add employee")

    def test_search_employee(self):
        driver = self.driver
        driver.find_element(By.ID, "menu_pim_viewPimModule").click()
        time.sleep(2)
        driver.find_element(By.ID, "empsearch_employee_name_empName").send_keys("John Doe")
        driver.find_element(By.ID, "searchBtn").click()
        time.sleep(3)

        search_results = driver.find_element(By.XPATH, "//tbody/tr")
        self.assertTrue(search_results.is_displayed(), "Search results are not displayed")

    def test_logout(self):
        driver = self.driver
        driver.find_element(By.ID, "welcome").click()
        time.sleep(2)
        driver.find_element(By.LINK_TEXT, "Logout").click()
        time.sleep(3)

        self.assertTrue(driver.find_element(By.NAME, "username").is_displayed(),
                        "Logout failed, login page is not displayed")

    def test_verify_EmployeeLeave(self):
        base = Base()
        driver = base.launchBrowser()
        time.sleep(5)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(50)
        driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
        driver.find_element(By.XPATH, "//*[@type='submit']").click()
        time.sleep(5)
        title = driver.find_element(By.XPATH, "//*[text()='Employees on Leave Today']").text
        assert title == "Employees on Leave Today"
        driver.quit()

    def test_verify_TimeatWork(self):
        base = Base()
        driver = base.launchBrowser()
        time.sleep(5)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(10)
        driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
        driver.find_element(By.XPATH, "//*[@type='submit']").click()
        time.sleep(5)
        title = driver.find_element(By.XPATH, "//*[text()='Time at Work']").text
        assert title == "Time at Work"
        driver.quit()

    def test_verify_(self):
        base = Base()
        driver = base.launchBrowser()
        time.sleep(5)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(10)
        driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
        driver.find_element(By.XPATH, "//*[@type='submit']").click()
        time.sleep(5)
        title = driver.find_element(By.XPATH, "//*[text()='Time at Work']").text
        assert title == "Time at Work"
        driver.quit()

    def tearDown(self):
        # Close the browser
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
