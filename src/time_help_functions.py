def convert_date(input):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    output = ""
    day, month, year = "", "", ""
    date_index = 0
    date = [year, month, day]
    
    for character in str(input):
        if character == "-":
            date_index += 1
        else:
            date[date_index] += character
    date[1]= str(int(date[1]) - 1)
    month1, day1, year1 = months[int(date[1])], date[2], date[0]
    output = month1 + " " + day1 + ", " + year1
    return output 


def convert_hour(input):
    if int(input) > 12:
        output = input -12
        return output
    return input



    

