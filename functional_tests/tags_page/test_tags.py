import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


try: # Tags page title name
    url = "http://127.0.0.1:5000/blog/tags/"
    browser = webdriver.Chrome()
    browser.get(url)
    assert 'Tags list' in browser.title
except AssertionError as error:
    print("Tags page title name test failed\n", error)

try: # Click on tag_link
    tag_link = browser.find_element(By.LINK_TEXT, "django")
    time.sleep(1)
    tag_link.click()
except NoSuchElementException as error:
    print("Click on Tags page tag_link test failed\n", error)

try: # Click on Read button
    read_button = browser.find_element(By.CSS_SELECTOR, "a.btn")
    time.sleep(1)
    read_button.click()
except NoSuchElementException as error:
    print("Read_button after click on tag_ling test failed\n", error)

try:
    nav_posts_button = browser.find_element(By.CSS_SELECTOR, "a.nav-posts")
    time.sleep(1)
    nav_posts_button.click()
except NoSuchElementException as error:
    print("Click on Navbar Posts button test failed\n", error)

finally:
    time.sleep(5)
    browser.quit()