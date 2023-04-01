from datetime import datetime
import tkinter as tk
from tkcalendar import Calendar



win = tk.Tk()

calendar = Calendar(win, selectmode="day",year= 2021, month=3, day=3,
                          showweeknumbers = False)



calendar.pack()

win.mainloop()