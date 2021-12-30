#!/usr/bin/python3

"""
Utilizing 'tkinter' to build a GUI interface to scan for Google 
Results


"""
import tkinter as tk 
import gui_model as gm


# project container
root = tk.Tk()

# set screen size 
HEIGHT = 500
WIDTH = 500 
canvas = tk.Canvas(root,height= HEIGHT, width=WIDTH)
canvas.pack()

# setting the frame
frame = tk.Frame(root, bg='#7ede7b')
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6)

# name label
label = tk.Label(frame,text="Enter a word you want to search")
# label.grid(row="0", column="0")
label.place(relx=0, rely=0.1, relwidth=0.6, relheight=0.1)


# entry field 
term_entry = tk.Entry(frame)
term_entry.place(relx=0.6, rely=0.1, relwidth=0.4, relheight=0.1)
# search_word = term_entry.get()

# pages label
label = tk.Label(frame,text="How many pages do you want to get?")
# label.grid(row="0", column="0")
label.place(relx=0, rely=0.4, relwidth=0.6, relheight=0.1)


# entry field 
page_entry = tk.Entry(frame)
page_entry.place(relx=0.6, rely=0.4, relwidth=0.4, relheight=0.1)
# get_pages = page_entry.get()

def get_results():
    search_word = term_entry.get()
    get_pages = page_entry.get()
    scan_page = int(get_pages)
    search_obj = gm.SearchTopic
    # the session activates but the keys are not being entered into search
    # problem fixed, but program cont after pages scanned
    search_obj.search_for(search_word)
    search_obj.next_page(scan_page)
    gm.ResultsData.show_data()

# search button 
# When this button is pressed, activate function 
button = tk.Button(frame, text="Start Search",command=get_results)
button.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)


# run the GUI
root.mainloop()
