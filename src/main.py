from datetime import datetime
import tkinter as tk
from tkcalendar import Calendar



win = tk.Tk()
win.title("Magneton")

calendar = Calendar(win, selectmode="day", year=2021, month=3, day=3,
                    showweeknumbers = False,
                    headersbackground ="white",
                    background = "white",
                    foreground = "black",  # Font colour
                    selectbackground = "skyblue",
                    normalbackground = "white",
                    weekendbackground = "lightgray",
                    weekendforeground = "white")



calendar.pack()

win.mainloop()