# pylint: disable=invalid-name
""" noinspection PyMissingOrEmptyDocstring"""
import tkinter as tk
from datetime import date
from datetime import datetime
from tkcalendar import Calendar
from tkcalendar import DateEntry
import time_help_functions as of
import time_1 as t1


win = tk.Tk()
win.geometry('1280x720')
win.title("Magneton")
change = True

cal = Calendar(win, font="Arial 14", selectmode="day",
               locale="en_US",
               showweeknumbers=False,
               headersbackground="white",
               background="white",
               foreground="black",  # font colour
               selectbackground="skyblue",
               normalbackground="white",
               weekendbackground="lightgray")

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

    #Label Declerations
    main_label = tk.Label(top, text="Enter Event Details", font="Arial 14")
    date_label = tk.Label(top, text="Current Date Set: ", font="Arial 14")
    temp_cal = DateEntry(top, selectmode='day',showweeknumbers=False)
    #Button Declarations
    submit_btn = tk.Button(top, text="Submit", font="Arial 14", command=set_event)
    #Label & Button Positioning
    main_label.pack(pady=5)
    date_label.pack(pady=10)
    temp_cal.pack(pady=10)
    submit_btn.pack(side=tk.BOTTOM)
    #Drop down date setup
    temp_cal.set_date(cal.get_date())
def update():
    """Updates the Displayed Day and Time every Second"""
    TODAY = of.convert_date(date.today())
    DATE["text"] = f"Current Day: {TODAY}"
    current_time = t1.get_time()
    timeLabel["text"] = f"Time: {current_time}"
    timeLabel.after(1000, update)
    DATE.after(1000,update)
#Labels
DATE = tk.Label(win, text = "Start",  font = "Arial 14")
timeLabel = tk.Label(win, text = "Start", font = "Arial 14",
    bd = 5, padx = 10, pady = 10)
timeLabel.pack()
DATE.pack()
#Buttons
tk.Button(win, text="Create New Event", command=create_event).pack(pady=20)
cal.pack(fill="both", expand=True)
update()
win.mainloop()
