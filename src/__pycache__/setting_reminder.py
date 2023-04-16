"""File is Used To Store Functions that will be used For Reminding The User"""
# pylint: disable=invalid-name
# pylint: disable=line-too-long
from datetime import date

def upcoming_event(event):
    """Not Complete, will need to include Time function"""
    eventDay = str(event.getDay())
    today = str(date.today())
    if eventDay == today:
        return True
    return False
