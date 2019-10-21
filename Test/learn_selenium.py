from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

browser = webdriver.Chrome()
url = "https://www.baidu.com"
browser.get(url)

input = browser.find_element_by_id("kw")
input.send_keys('996.icu')
input.send_keys(Keys.ENTER)

pos = browser.find_element_by_id("//*[@id=1']/h3/a")

btn = pos.get_attribute("href")
btn.click()

browser.execute_script("alert('hahaha')")

time.sleep(3)

browser.close()
