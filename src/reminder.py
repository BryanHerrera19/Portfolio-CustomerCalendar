"""File is Used To Store Functions that will be used For Reminding The User"""
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=too-many-function-args

import datetime as DT

class Reminder:
    """Reminder Class used to Remind the User of when a Event is Prior to it occuring"""
    def __init__(self):
        """Initializing what reminders are turned on"""
        self.week = False
        self.day = False
        self.hour = False
    # Setters
    def setWeek(self, TF):
        """changes week Reminder Boolean"""
        self.week = TF
    def setDay(self, TF):
        """Changes Day Reminder Boolean"""
        self.day = TF
    def setHour(self, TF):
        """Changes Hour Reminder Boolean"""
        self.hour = TF
    # Getters
    def getWeek(self):
        """Gets Current Week Boolean"""
        return self.week
    def getDay(self):
        """Gets Current Day Boolean"""
        return self.day
    def getHour(self):
        """Gets Current Hour Boolean"""
        return self.hour
    
    def weekBefore(self, event):
        """Checks if today is a week before event """
        today = DT.datetime.today()
        week_before = event.getDay() - DT.timedelta(days = 7)
        if today == week_before:
            return True
        return False
    def dayBefore(self, event):
        """Checks if today is a day before event """
        today = DT.datetime.today()
        DayBefore = event.getDay() - DT.timedelta(days = 1)
        if today == DayBefore:
            return True
        return False
    def hourBefore(self, event):
        """Check if Today is a hour before event"""
        today = DT.datetime.today()
        hourBefore = event.getDay() - DT.timedelta(hours = 1)
        if today == hourBefore:
            return True
        return False
    def upcomingEvent(self, event):
        """Checks if event is upcoming"""
        print("Today", DT.datetime.today(), "\n")
        print("Week", event.getDay() - DT.timedelta(days = 7), "\n")
        print("Day", event.getDay() - DT.timedelta(days = 1), "\n")
        print("hour before", event.getDay() - DT.timedelta(hours = 1), "\n")

        if self.week:
            return self.weekBefore(event)
        if self.day:
            return self.dayBefore(event)
        if self.hour:
            return self.hourBefore(event)
        return False
    def status(self):
        """Return Status of Reminder"""
        string = "\n"
        lis = [self.week, self.day, self.hour]
        lis1 = ["Week Prior: ", "Day Prior: ", "Hour Prior: "]
        i = 0
        for value in lis:
            string += lis1[i]
            if value == True:
                string += "ON"
            else:
                string += "OFF"
            string += "\n"
            i += 1
        return string
