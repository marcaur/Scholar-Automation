#!/usr/bin/python3
from pathlib import Path
from datetime import date 
import csv, re, os
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# store titles and links
articles = []
links = []

# SearchTerm.searchFor
class SearchTopic:
    def search_for(self):
        # SearchTopic.search_for("history")
        global driver
        driver = webdriver.Firefox()
        driver.get("https://scholar.google.com/")
        wait = WebDriverWait(driver,10)
    
        element = driver.find_element_by_id('gs_hdr_tsi')
        element.send_keys(self)
        new_elem = wait.until(EC.element_to_be_clickable((By.ID, 'gs_hdr_tsb')))
        new_elem.click()

    def scan_page():
        all_titles = driver.find_elements(By.CLASS_NAME, 'gs_rt')
        for title in all_titles:
            articles.append(title.text)

        all_links = driver.find_elements_by_css_selector('h3 > a')
        for li in all_links:
            links.append(li.get_attribute('href'))

    def next_page(self):
        for page in range(0, self):
            SearchTopic.scan_page()
            page += 1
            print(f"Page {page} scanned. Moving to next page.")
            next_page = driver.find_element(By.CLASS_NAME, 'gs_ico_nav_next')
            next_page.click()
            driver.close()
            

class ResultsData:
    def store_in_csv():
        print("What do you want to name the file?"); file_name = str(input())
        goog_res = f'{file_name}_{date.today()}.csv'
        new_file = Path(goog_res)
        csv_file = open(new_file,'w',newline='')
        csv_output = csv.DictWriter(csv_file,['Title','Link'])
        csv_output.writeheader()
        info = dict(zip(articles,links))

        for title,link in info.items():
            csv_output.writerow({'Title':title, 'Link':link})

    def show_data():
        info = dict(zip(articles,links))
        pprint(info)