# pylint: disable=invalid-name
# pylint: disable=line-too-long
""" noinspection PyMissingOrEmptyDocstring"""
import tkinter as tk
from datetime import date
from tkcalendar import Calendar
from tkcalendar import DateEntry

import time_1 as t1
import time_help_functions as of

win = tk.Tk()
win.geometry('1300x900')
win.title("Magneton")
win.configure(background="white")



change = True


cal = Calendar(win, font="Arial 14", selectmode="day",
               locale="en_US",
               showweeknumbers=False,
               disabledbackground="white",
               headersbackground="white",
               background="white",
               foreground="black",  # font colour
               selectbackground="skyblue",
               normalbackground="white",
               weekendbackground="lightgray")

cal.config(background="white")
cal.pack(pady=20)
def create_event():
    '''Create event window for calendar'''
    top = tk.Toplevel(win)
    top.geometry('640x360')
    top.title("Creating Event")

    def set_event():
        '''Set event on calendar and color it'''
        cal.calevent_create(date=temp_cal.get_date(), text="New Event", tags="Message")
        cal.tag_config("Message", background="MediumPurple1", foreground="white")
        top.destroy()

    # Label Declerations
    main_label = tk.Label(top, text="Enter Event Details", font="Arial 14")
    date_label = tk.Label(top, text="Current Date Set: ", font="Arial 14")
    title_label = tk.Label(top, text="Title: ", font="Arial 14")
    note_label = tk.Label(top, text="Notes: ", font="Arial 14")
    temp_cal = DateEntry(top, selectmode='day', showweeknumbers=False)
    # Button Declarations
    submit_btn = tk.Button(top, text="Submit", font="Arial 14", command=set_event)
    # Label & Button Positioning
    main_label.pack(pady=5)
    date_label.pack(pady=10)
    temp_cal.pack(pady=10)
    title_label.pack(pady=10)
    submit_btn.pack(side=tk.BOTTOM)
    # Drop down date setup
    temp_cal.set_date(cal.get_date())
    # Event title entry box
    title = tk.Entry(top, width=30, font="Arial 14")
    title.pack()
    # note_label positioned after Title text box
    note_label.pack(pady=10)
    # Event note textbox
    note = tk.Text(top, width=30, height=30, font="Arial 14")
    note.pack()


def update():
    """Updates the Displayed Day and Time every Second"""
    TODAY = of.convert_date(date.today())
    DATE["text"] = f"Current Day: {TODAY}"
    current_time = t1.get_time()
    timeLabel["text"] = f"Time: {current_time}"
    # timeLabel.after(1000, update) this line was making my program stop less than a minute of running it - Marissa
    DATE.after(1000, update)


def open_tips():
    """Provides user with tips on how to reduce procrastination"""
#Labels
DATE = tk.Label(win, text = "Start",  font = "Arial 14")
timeLabel = tk.Label(win, text = "Start", font = "Arial 14",
    bd = 5, padx = 10, pady = 10)
timeLabel.pack()
DATE.pack()
#Buttons
tk.Button(win, text="Create New Event", command=create_event).pack(pady=20)
tk.Button(win, text = "Tips?", command = open_tips).pack(pady=20)
cal.pack(fill="both", expand=True)
update()
win.mainloop()
