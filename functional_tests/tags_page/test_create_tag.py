import time
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def generate_tag(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

word_to_tag = generate_tag(5)


try:  # Create tag page title name
    url = "http://127.0.0.1:5000/blog/tag/create"
    browser = webdriver.Chrome()
    browser.get(url)
    assert 'Create tag' in browser.title
except AssertionError as error:
    print("Create tag page title name test failed\n", error)


try:  # Fill form
    title_input = browser.find_element(By.ID, "id_title")
    title_input.send_keys(word_to_tag)
    slug_input = browser.find_element(By.ID, "id_slug")
    slug_input.send_keys(word_to_tag)

    time.sleep(1)

    create_tag_button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    create_tag_button.click()

    time.sleep(1)
except NoSuchElementException as error:
    print("Create tag button not found on page\n", error)
finally:
    time.sleep(5)
    browser.quit()

