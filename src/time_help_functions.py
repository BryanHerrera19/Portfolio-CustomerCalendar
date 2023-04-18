"""File is used to assist main.py in creating readable dates and time"""
# pylint: disable=line-too-long

from datetime import datetime
def convert_date(enter):
    """ Converts datetime to readable date"""
    new_input = str(enter)
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    output = ""
    day, month, year = "", "", ""
    date_index = 0
    date = [year, month, day]
    for character in new_input:
        if character == "-":
            date_index += 1
        else:
            date[date_index] += character
    date[1] = str(int(date[1]) - 1)
    month1, day1, year1 = months[int(date[1])], date[2], date[0]
    output = month1 + " " + day1 + ", " + year1
    return output
def convert_hour(enter):
    """Converts Time to a 12-hour system"""
    new_input = int(enter)
    if new_input > 12:
        output = new_input - 12
        return output
    return new_input
def get_time():
    """Grabs the current time in readable format"""
    now = datetime.now()
    hour = now.strftime("%H")
    minute = now.strftime("%M")
    second = now.strftime("%S")
    ante_post = now.strftime("%p")
    hour = convert_hour(hour)
    current_time = f"{hour}:{minute}:{second} {ante_post}"
    return current_time
