import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


try:
    url = "http://127.0.0.1:5000/blog/"
    browser = webdriver.Chrome()
    browser.get(url)
    assert 'Posts list' in browser.title
except AssertionError as error:
    print("Home page test failed\n", error)

try:
    button = browser.find_element(By.CSS_SELECTOR, "a.btn")
    time.sleep(1)
    button.click()
except NoSuchElementException as error:
    print("Button test failed\n", error)

finally:
    time.sleep(5)
    browser.quit()
