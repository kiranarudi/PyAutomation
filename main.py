#Scrape dynamic value from web page
#In this example, we will scrape a dynamic value from a web page using Selenium. We will use the Chrome WebDriver to open the web page and extract the dynamic value using XPath.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('disable-infobars')
    options.add_argument('start-maximized')
    options.add_argument('disable-dev-shm-usage')
    options.add_argument('no-sandbox')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument('disable-blink-features=AutomationControlled')
    driver = webdriver.Chrome()
    driver.get("http://automated.pythonanywhere.com/")
    return driver

def main():
    driver = get_driver()
    time.sleep(2)
    element = driver.find_element(By.XPATH, "/html/body/div[1]/div/h1[2]")
    return element

print(main().text)