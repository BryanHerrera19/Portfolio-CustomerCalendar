# pylint: disable=invalid-name
# pylint: disable=line-too-long
""" noinspection PyMissingOrEmptyDocstring"""

import tkinter as tk
from tkinter import messagebox
from datetime import date

from tkcalendar import Calendar
from tkcalendar import DateEntry

import time_help_functions as t1
from Event_Info import Event as eventInfo

win = tk.Tk()
win.geometry('1300x900')
win.title("Magneton")
win.configure(background="white")

change = True

event_list = []

cal = Calendar(win, font="Arial 14", selectmode="day",
               locale="en_US",
               showweeknumbers=False,
               disabledbackground="white",
               headersbackground="white",
               background="white",
               foreground="black",  # font colour
               selectbackground="skyblue",
               normalbackground="white",
               weekendbackground="lightgray",
               firstweekday="sunday")

cal.config(background="white")
cal.pack(pady=20)
def create_event():
    '''Create event window for calendar'''
    # pylint: disable-msg=too-many-locals
    top = tk.Toplevel(win)
    top.geometry('640x360')
    top.title("Creating Event")

    def set_event():
        '''Set event on calendar and color it'''
        # save event info
        print(f"date = {date_selected.get()}")
        user_Notes = note.get(1.0, "end-1c")
        save_time = hour_time.get() + " " + minute_time.get() + " " + day.get()
        event_list.append(eventInfo(temp_cal.get_date(), save_time, title.get(), user_Notes))

        cal.calevent_create(date=temp_cal.get_date(), text="New Event", tags="Message")
        cal.tag_config("Message", background="MediumPurple1", foreground="white")
        top.destroy()

    # Label Declerations
    main_label = tk.Label(top, text="Enter Event Details", font="Arial 14")
    date_label = tk.Label(top, text="Current Date Set: ", font="Arial 14")
    title_label = tk.Label(top, text="Title: ", font="Arial 14")
    note_label = tk.Label(top, text="Notes: ", font="Arial 14")
    time_label = tk.Label(top, text="Time: ", font="Arial 14")
    time_colon_label = tk.Label(top, text=" : ", font="Arial 16")
    date_selected = tk.StringVar()
    temp_cal = DateEntry(top, selectmode='day', showweeknumbers=False, textvariables=date_selected)
    # Button Declarations
    submit_btn = tk.Button(top, text="Submit", font="Arial 14", command=set_event)
    # Drop down date and time setup
    temp_cal.set_date(cal.get_date())
    day = tk.StringVar()
    day.set("AM/PM")
    day_drop = tk.OptionMenu(top, day, "AM", "PM")
    hour_time = tk.StringVar()
    hour_time.set("Hour")
    hour_time_drop = tk.OptionMenu(top, hour_time, "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12")
    minute_time = tk.StringVar()
    minute_time.set("Minute")
    minute_time_drop = tk.OptionMenu(top, minute_time, "0", "5", "10", "15", "20", "25", "30", "35", "40", "45", "50",
                                     "55", "60")
    # Event title entry box
    title = tk.Entry(top, width=30, font="Arial 14")
    # Event note textbox
    note = tk.Text(top, width=30, height=5, font="Arial 14")
    # Pack everything
    main_label.place(x=250, y=5)
    title_label.place(x=50, y=50)
    title.place(x=170, y=50)
    date_label.place(x=50, y=100)
    temp_cal.place(x=220, y=100)
    time_label.place(x=50, y=150)
    hour_time_drop.place(x=170, y=150)
    time_colon_label.place(x=234, y=150)
    minute_time_drop.place(x=250, y=150)
    day_drop.place(x=330, y=150)
    note_label.place(x=50, y=200)
    note.place(x=170, y=200)
    submit_btn.place(x=250, y=320)

def update():
    """Updates the Displayed Day and Time every Second"""
    TODAY = t1.convert_date(date.today())
    DATE["text"] = f"Current Day: {TODAY}"
    current_time = t1.get_time()
    timeLabel["text"] = f"Time: {current_time}"
    DATE.after(1000, update)


def open_tips():
    """Provides user with tips on how to reduce procrastination"""
    with open('tips.txt', 'r', encoding = 'utf-8') as file:
        tips = file.readlines()
    tip_string = ""
    for line in tips:
        tip_string += (line + "\n")
    messagebox.showinfo("Tips", tip_string)

def event_list_window():
    '''Creates a new window with a list of events'''
    event_window = tk.Toplevel(win)
    event_window.geometry('360x640')
    event_window.title("Event List")

    #looping through events in list
    for event in event_list:
        event_string = "Event: " + event.getName()
        date_string = "Date: " + str(event.getDay())
        time_string = "Time: " + str(event.getTime())
        description_string = "Description: " + event.getNotes()

        #labels
        event_string_label = tk.Label(event_window, text = event_string, font = "arial 14 bold")
        event_date_label = tk.Label(event_window, text = date_string, font = "arial 14")
        event_time_label = tk.Label(event_window, text = time_string, font = "arial 14")
        event_description_label = tk.Label(event_window, text = description_string, font = "arial 14", anchor='w', wraplength=360)
        #label packing
        event_string_label.place(x=0, y=0)
        event_date_label.place(x=0, y=25)
        event_time_label.place(x=0, y=50)
        event_description_label.place(x=0, y=75)


#Labels
DATE = tk.Label(win, text = "Start",  font = "Arial 14")
timeLabel = tk.Label(win, text = "Start", font = "Arial 14",
    bd = 5, padx = 10, pady = 10)
timeLabel.pack()
DATE.pack()
#Buttons
tk.Button(win, text="Create New Event", command=create_event, font = "arial 14 bold").pack(pady=5)
tk.Button(win, text = "Check Events", command = event_list_window, font = "arial 14 bold").pack(pady=5)
tk.Button(win, text = "General Study & Scheduling Tips", font = "arial 14 bold", command = open_tips).pack(pady=5)
cal.pack(fill="both", expand=True)
update()
win.mainloop()
