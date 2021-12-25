#!/usr/bin/python3

import scholar_model as sm

try:
    while True:
        term = str(input("What term do you want to search for? "))
        pages = int(input("How many pages do you want to search for? "))
        search_obj = sm.SearchTopic
        search_obj.search_for(term)
        search_obj.next_page(pages)
        print("Do you want to search for another topic?");new_search = str(input("Press 'Y' to continue or any other button to quit ")).lower()
        if new_search != "y":
            break 
    print("All pages have been scanned. Goodbye!")
    
finally:
    print("These are the results")
    sm.ResultsData.show_data()
    sm.ResultsData.store_in_csv()

