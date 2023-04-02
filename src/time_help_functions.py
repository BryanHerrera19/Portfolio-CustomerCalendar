def convert_date(input):
    input = str(input)
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    output = ""
    
    day, month, year = "", "", ""

    date_index = 0
    date = [year, month, day]
    
    for character in input:
        if(character == "-"):
            date_index += 1
        else:
            date[date_index] += character

    date[1]= str(int(date[1]) - 1)
    
    m, d, y = months[int(date[1])], date[2], date[0]
    output = m + " " + d + ", " + y

    return output 


def convert_hour(input):
    input = int(input)
    if input > 12:
        output = input -12
        return output
    return input



    

