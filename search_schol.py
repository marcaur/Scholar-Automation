#!/usr/bin/python3

from pprint import pprint
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# initiate the program
driver = webdriver.Firefox()
driver.get("https://scholar.google.com/")
wait = WebDriverWait(driver,10)
element = driver.find_element_by_id('gs_hdr_tsi')
element.send_keys("social media")
# waits until search button can be clicked
new_elem = wait.until(EC.element_to_be_clickable((By.ID, 'gs_hdr_tsb')))
new_elem.click()

# store articles
articles = []
links = []

# This Is Where The Data Collection Is
def get_results():
    all_titles = driver.find_elements(By.CLASS_NAME, 'gs_rt')
    for title in all_titles:
        articles.append(title.text)

    all_links = driver.find_elements_by_css_selector('h3 > a')
    for li in all_links:
        links.append(li.get_attribute('href'))

def go_to_next_page():
    next_page = driver.find_element(By.CLASS_NAME, 'gs_ico_nav_next')
    next_page.click()

pages_to_get = 1

while pages_to_get < 6:
    get_results()
    print(f"Page {pages_to_get} scanned. Moving to next page.")
    go_to_next_page()
    pages_to_get += 1

info = dict(zip(articles,links))

print("All pages have been scanned. Goodbye!")
driver.close()
pprint(info)