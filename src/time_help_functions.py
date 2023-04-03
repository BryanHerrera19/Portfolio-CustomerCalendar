"""File is used to assist time_1 in creating readable dates and time"""
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
