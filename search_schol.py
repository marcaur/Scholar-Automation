#!/usr/bin/python3
import csv
import re
from pprint import pprint
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# store titles and links
articles = []
links = []

# initiate the program
driver = webdriver.Firefox()

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

def store_in_csv(file_name):
    print(input('What do you want to name the file?'))
    csv_file = open(file_name,'w',newline='')
    csv_output = csv.DictWriter(csv_file,['Title','Link'])
    csv_output.writeheader()
    csv_output.writerow({'Title':'Title', 'Link':'Link'})

    for title,link in info.items():
        csv_output.writerow({'Title':title, 'Link':link})


try:
    driver.get("https://scholar.google.com/")
    wait = WebDriverWait(driver,10)
    element = driver.find_element_by_id('gs_hdr_tsi')
    # change to user input
    # error checking?
    while True:
        print("What term do you want to search?"); search_topic = str(input())

        if re.search("^\s*$", search_topic):
            print("Enter a search term")
            continue

        else:
            print(f"You are searching for {search_topic} ")
            break

    element.send_keys(search_topic)
    # waits until search button can be clicked
    new_elem = wait.until(EC.element_to_be_clickable((By.ID, 'gs_hdr_tsb')))
    new_elem.click()


    # Program start
    # change to receive user input
    print("How many pages of results do you want to get?"); pages_to_get = int(input())

    pages_to_get += 1

    for page in range(1, pages_to_get) :
        get_results()
        print(f"Page {page} scanned. Moving to next page.")
        go_to_next_page()
        page += 1

    info = dict(zip(articles,links))


    print("All pages have been scanned. Goodbye!")
finally:
    driver.close()
    pprint(info)
