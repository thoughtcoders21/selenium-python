from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options
import os


current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
download_path = os.path.join(parent_dir, "testdata", "Download")

def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("use-fake-device-for-media-stream")
    chrome_options.add_argument("use-fake-ui-for-media-stream")
    chrome_options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.automatic_downloads": 1,
        "download.default_directory": download_path,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })
    driver = webdriver.WebDriver(options=chrome_options)
    return driver

