#Scrape dynamic value from web page
#In this example, we will scrape a dynamic value from a web page using Selenium. We will use the Chrome WebDriver to open the web page and extract the dynamic value using XPath.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
    driver.get("http://automated.pythonanywhere.com/login")
    return driver

def main():
    driver = get_driver()
    driver.find_element(By.ID, "id_username").send_keys("automated")
    time.sleep(2)
    driver.find_element(By.ID, "id_password").send_keys("automatedautomated" + Keys.RETURN)
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/nav/div/a").click()
    time.sleep(2)
    element = driver.find_element(By.XPATH, "/html/body/div[1]/div/h1[2]")
    return element


print(main().text)