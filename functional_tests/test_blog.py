import time
from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    url = "http://127.0.0.1:5000/blog/"
    browser = webdriver.Chrome()
    browser.get(url)
    assert 'Posts list' in browser.title

except AssertionError as error:
    print("Home page test failed: ", error)

finally:
    time.sleep(5)
    browser.quit()
