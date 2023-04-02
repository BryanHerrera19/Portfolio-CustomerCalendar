""" noinspection PyMissingOrEmptyDocstring"""
import tkinter as tk
import tkcalendar

win = tk.Tk()
win.title("Magneton")

cal = tkcalendar.Calendar(win, font="Arial 14", selectmode="day",
                          locale="en_US", year=2023, month=4, day=1,
                          showweeknumbers=False,
                          headersbackground="white",
                          background="white",
                          foreground="black",  # font colour
                          selectbackground="skyblue",
                          normalbackground="white",
                          weekendbackground="lightgray")

cal.pack(fill="both", expand=True)

win.mainloop()
