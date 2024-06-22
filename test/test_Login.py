import time
import pytest
from selenium.webdriver.common.by import By

from Base import Base


def test_verify_login():
    base = Base()
    driver = base.launchBrowser()
    time.sleep(5)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(50)
    driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
    driver.find_element(By.XPATH, "//*[@type='submit']").click()
    time.sleep(5)
    title = driver.find_element(By.XPATH, "(//*[text()='Dashboard'])[1]").text
    assert title == "Dashboard"
    driver.quit()

def test_verify_InValid_login():
    base = Base()
    driver = base.launchBrowser()
    time.sleep(5)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(30)
    driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin1234")
    driver.find_element(By.XPATH, "//*[@type='submit']").click()
    time.sleep(5)
    wrongPasswordNotice = driver.find_element(By.XPATH, "//*[@class='oxd-text oxd-text--p oxd-alert-content-text'}").text
    assert wrongPasswordNotice =='Invalid credentials'
    driver.quit()