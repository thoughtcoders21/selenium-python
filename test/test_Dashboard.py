from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initialize the WebDriver (Chrome in this case)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the OrangeHRM login page
driver.get("https://opensource-demo.orangehrmlive.com/")

# Maximize the browser window
driver.maximize_window()

# Add implicit wait
driver.implicitly_wait(10)

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
time.sleep(5)

# Validate the login by checking if the dashboard is displayed
try:
    dashboard = driver.find_element(By.XPATH, "//h6[text()='Dashboard']")
    print("Login successful, Dashboard is displayed.")
except:
    print("Login failed, Dashboard is not displayed.")

# Close the browser
driver.quit()