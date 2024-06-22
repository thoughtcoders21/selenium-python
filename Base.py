import urllib3
from selenium.webdriver.common.by import By
from chromeDriver import setup_driver


class Base:

    def launchBrowser(self):
        driver = setup_driver()
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        #driver = webdriver.Chrome(chromeDriverPath)
        driver.maximize_window()
        driver.implicitly_wait(45)
        driver.set_page_load_timeout(60)
        return driver

    def closeBrowser(self, driver):
        driver.close()

    def clickUsingJS(self, driver, xpath):
        element = driver.find_element(By.XPATH, xpath)
        driver.execute_script("arguments[0].click();", element)
a = Base()
a.launchBrowser()