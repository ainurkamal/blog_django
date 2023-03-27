import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


try: # Posts page title name
    url = "http://127.0.0.1:5000/blog/"
    browser = webdriver.Chrome()
    browser.get(url)
    assert 'Posts list' in browser.title
except AssertionError as error:
    print("Posts page name title test failed\n", error)

try: # Click on Read some post
    read_button = browser.find_element(By.CSS_SELECTOR, "a.btn")
    time.sleep(1)
    read_button.click()
except NoSuchElementException as error:
    print("Click on Posts page Read button test failed\n", error)

try: # Return to Posts page
    nav_posts_button = browser.find_element(By.CSS_SELECTOR, "a.nav-posts")
    time.sleep(1)
    nav_posts_button.click()
except NoSuchElementException as error:
    print("Click on Navbar Posts button test failed\n", error)

finally:
    time.sleep(5)
    browser.quit()
