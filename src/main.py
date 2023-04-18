# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring

import time
import tkinter as tk
from datetime import date
from tkinter import colorchooser
from tkinter import messagebox
from tkcalendar import Calendar
from tkcalendar import DateEntry


import time_help_functions as t1
from Event_Info import Event as eventInfo
from sort_dates import sort_by_date, sort_by_category

win = tk.Tk()
win.geometry('1200x900')
win.title("Magneton")
win.configure(background="white")

change = True

event_list = []
event_window_labels = []

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
# Buttons

def create_event():
    '''Create event window for calendar'''
    # pylint: disable-msg=too-many-locals
    # pylint: disable=too-many-statements
    top = tk.Toplevel(win)
    top.geometry('540x460')
    top.title("Creating Event")

    def set_event():
        '''Set event on calendar and color it'''
        # pylint: disable=global-statement
        # save event info
        user_Notes = note.get(1.0, "end-1c")
        save_start_time = start_hour_time.get() + ":" + start_minute_time.get()
        save_end_time = end_hour_time.get() + ":" + end_minute_time.get() + end_day.get()

        global event_list

        event_list.append(
            eventInfo(temp_cal.get_date(), save_start_time, start_day.get(), save_end_time, title.get(),
                      user_Notes, category.get()))
        # Sort event_list by their category and start time (chronological order)
        event_list.sort(key=lambda event: [event.category, event.day, event.start_time_day])
        event_list = eventInfo.sortStartTime(eventInfo, event_list)

        cal.calevent_create(date=temp_cal.get_date(), text="New Event", tags="Message")
        cal.tag_config("Message", background="MediumPurple1", foreground="white") #change color here later
        top.destroy()

    # Label Declarations
    main_label = tk.Label(top, text="Enter Event Details", font="Arial 14")
    date_label = tk.Label(top, text="Current Date Set: ", font="Arial 14")
    title_label = tk.Label(top, text="Title: ", font="Arial 14")
    note_label = tk.Label(top, text="Notes: ", font="Arial 14")
    time_label = tk.Label(top, text="Time: ", font="Arial 14")
    category_label = tk.Label(top, text="Category: ", font="Arial 14")
    start_time_colon_label = tk.Label(top, text=" : ", font="Arial 16")
    end_time_colon_label = tk.Label(top, text=" : ", font="Arial 16")
    to_label = tk.Label(top, text="to", font="Arial 10")
    date_selected = tk.StringVar()
    temp_cal = DateEntry(top, selectmode='day', showweeknumbers=False, textvariables=date_selected)

    # Button Declarations
    submit_btn = tk.Button(top, text="Submit", font="Arial 14", command=set_event)

    # Drop down date and time setup
    temp_cal.set_date(cal.get_date())
    start_day = tk.StringVar()
    start_day.set("AM/PM")
    start_day_drop = tk.OptionMenu(top, start_day, "AM", "PM")
    start_hour_time = tk.StringVar()
    start_hour_time.set("Hour")
    start_hour_time_drop = tk.OptionMenu(top, start_hour_time, "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11",
                                         "12")
    start_minute_time = tk.StringVar()
    start_minute_time.set("Minute")
    start_minute_time_drop = tk.OptionMenu(top, start_minute_time, "00", "05", "10", "15", "20", "25", "30", "35", "40",
                                           "45", "50", "55")
    end_day = tk.StringVar()
    end_day.set("AM/PM")
    end_day_drop = tk.OptionMenu(top, end_day, "AM", "PM")
    end_hour_time = tk.StringVar()
    end_hour_time.set("Hour")
    end_hour_time_drop = tk.OptionMenu(top, end_hour_time, "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11",
                                       "12")
    end_minute_time = tk.StringVar()
    end_minute_time.set("Minute")
    end_minute_time_drop = tk.OptionMenu(top, end_minute_time, "00", "05", "10", "15", "20", "25", "30", "35", "40",
                                         "45", "50", "55")

    category = tk.StringVar()
    category.set("Category")
    category_drop = tk.OptionMenu(top, category, "ARTS", "BIOL", "CHEM", "COMM", "COMP", "ECON", "EDUC", "ENGL", "GESC",
                                  "HIST", "MATH", "MEDX", "POLS", "PSYC", "SOCI", "THEA")

    # Color picker
    # do not uncomment this it will break the menu
    # color = tk.colorchooser()
    # color.set("Color") vs
    # color().set()

    # stores selected color
    def color():
        """Holds user choosen color"""
        # pylint: disable=unused-variable
        my_color = colorchooser.askcolor()

    color_btn = tk.Button(top, height=1, text="Pick a Color", command=color)  # pylint: disable=unused-argument

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
    start_hour_time_drop.place(x=170, y=150)
    start_time_colon_label.place(x=234, y=150)
    start_minute_time_drop.place(x=250, y=150)
    start_day_drop.place(x=330, y=150)
    to_label.place(x=250, y=175)
    end_hour_time_drop.place(x=170, y=200)
    end_time_colon_label.place(x=234, y=200)
    end_minute_time_drop.place(x=250, y=200)
    end_day_drop.place(x=330, y=200)

    category_label.place(x=50, y=250)
    category_drop.place(x=170, y=250)

    color_btn.place(x=280, y=252)


    note_label.place(x=50, y=300)
    note.place(x=170, y=300)
    submit_btn.place(x=250, y=420)

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
    event_window.geometry('460x640')
    event_window.title("Event List")
    paste_event_list_labels(event_window)


def study_timer():
    """Study Timer for User"""
    tWindow = tk.Toplevel(win)
    tWindow.title("Study Timer")
    tWindow.geometry("500x500")
    tWindow.configure(background = 'yellow')

    # Variables
    hourString, minuteString, secondString = tk.StringVar(), tk.StringVar(), tk.StringVar()

    # Input
    secondEntry = tk.Entry(tWindow, width = 3, font = "arial 14 bold", textvariable = secondString)
    minuteEntry = tk.Entry(tWindow, width = 3, font = "arial 14 bold", textvariable = minuteString)
    hourEntry = tk.Entry(tWindow, width = 3, font = "arial 14 bold", textvariable = hourString)

    # Entry Placement
    secondEntry.place(x = 270, y = 180)
    minuteEntry.place(x = 220, y = 180)
    hourEntry.place(x = 170, y = 180)

    # Def Run Timer Function
    def runTimer():
        """Runs the timer with exceptions"""
        try:
            clock_Time = int(hourString.get())*3600 + int(minuteString.get())*60 + int(secondString.get())
        except ValueError:
            messagebox.showinfo("Invalid Input(s)!!!", "Please check if all inputs are valid (Numerical)")
        while clock_Time > -1 :
            totalMinutes, totalSeconds = divmod(clock_Time, 60)
            totalHours = 0
            if totalMinutes > 60:
                totalHours, totalMinutes = divmod(totalMinutes, 60)
            hourString.set(f"{totalHours}")
            minuteString.set(f"{totalMinutes}")
            secondString.set(f"{totalSeconds}")
            # Update Constantly
            tWindow.update()
            time.sleep(1)
            if clock_Time == 0:
                messagebox.showinfo("Timer", "Timer Has Finished!")
                # To Close Timer
                tWindow.destroy()
            clock_Time -= 1
    setTimeButton = tk.Button(tWindow, text = 'Set Time', bd = 5, command=runTimer)
    setTimeButton.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    tWindow.mainloop()

def destroy_list_labels():
    '''Destroys the list of labels in the event window'''
    for label in event_window_labels:
        label.destroy()

def sort_event_window_labels_by_date(window):
    '''Sorts event list by date and pastes it to event window'''
    destroy_list_labels()
    sort_by_date(event_list)
    paste_event_list_labels(window)

def sort_event_window_labels_by_category(window):
    '''Sorts event list by category and pastes it to event window'''
    destroy_list_labels()
    sort_by_category(event_list)
    paste_event_list_labels(window)

def paste_event_list_labels(window):
    '''Pastes events onto the event list window'''
    # pylint: disable-msg=too-many-locals
    # pylint: disable=too-many-statements
    x_loc = 0
    y_loc = 25
    if event_list:
        for event in event_list:
            event_string = "Event: " + event.getName()
            date_string = "Date: " + str(event.getDay())
            start_time_string = "Time: " + str(event.getStartTime()) + event.getStartTimeDay() + " to " \
                                + str(event.getEndTime())
            section_string = "Category: " + str(event.getCategory())
            description_string = "Description: \n" + event.getNotes()

            # labels
            event_string_label = tk.Label(window, text=event_string, font="arial 14 bold")
            event_date_label = tk.Label(window, text=date_string, font="arial 14")
            event_time_label = tk.Label(window, text=start_time_string, font="arial 14")
            event_section_label = tk.Label(window, text=section_string, font="arial 14")
            event_description_label = tk.Label(window, text=description_string, font="arial 14", anchor='w',
                                               wraplength=360)
            sort_by_label = tk.Label(window, text="Sort by: ", font="arial 14")

            # label packing
            event_string_label.place(x=x_loc, y=y_loc)
            y_loc += 25
            event_date_label.place(x=x_loc, y=y_loc)
            y_loc += 25
            event_time_label.place(x=x_loc, y=y_loc)
            y_loc += 25
            event_section_label.place(x=x_loc, y=y_loc)
            y_loc +=25
            event_description_label.place(x=x_loc, y=y_loc)
            y_loc += 120
            sort_by_label.place(x=0,y=0)

            #appending labels to list to easily destroy
            event_window_labels.append(event_string_label)
            event_window_labels.append(event_date_label)
            event_window_labels.append(event_time_label)
            event_window_labels.append(event_section_label)
            event_window_labels.append(event_description_label)
            #button
            date_button = tk.Button(window, text="Date", command=lambda: sort_event_window_labels_by_date(window))
            category_button = tk.Button(window, text="Category/Class", command=lambda: sort_event_window_labels_by_category(window))
            date_button.place(x=75, y=0)
            category_button.place(x=150, y=0)
    else:
        no_event_label = tk.Label(window, text="No Events", font="arial 14 bold")
        no_event_label.place(x=135, y=200)

# Labels
DATE = tk.Label(win, text="Start", font="Arial 14")
timeLabel = tk.Label(win, text="Start", font="Arial 14",
                     bd=5, padx=10, pady=10)
timeLabel.pack()
DATE.pack()

# Buttons
tk.Button(win, text="Create New Event", command=create_event, font="arial 14 bold").pack(pady=50, padx=50, side=tk.LEFT)
tk.Button(win, text="Check Events", command=event_list_window, font="arial 14 bold").pack(pady=50, padx=50,
                                                                                          side=tk.LEFT)
tk.Button(win, text="General Study & Scheduling Tips", font="arial 14 bold", command=open_tips).pack(pady=50, padx=50,
                                                                                                     side=tk.LEFT)
tk.Button(win, text="Study Timer", font="arial 14 bold", command = study_timer).pack(pady=50, padx=50, side=tk.LEFT)
cal.pack(fill="both", expand=True)





update()
win.mainloop()
