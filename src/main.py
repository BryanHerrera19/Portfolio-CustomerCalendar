""" noinspection PyMissingOrEmptyDocstring"""
import tkinter as tk

from tkcalendar import Calendar

win = tk.Tk()
win.geometry('1280x720')
win.title("Magneton")

cal = Calendar(win, font="Arial 14", selectmode="day",
               locale="en_US", year=2023, month=4, day=1,
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
    tk.Label(top, text="Enter Event Details", font="Arial 14")

tk.Button(win, text="Create New Event",
       command=create_event).pack(pady=20)

date = tk.Label(win, text="")

cal.pack(fill="both", expand=True)

win.mainloop()
