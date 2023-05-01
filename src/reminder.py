"""File is Used To Store Functions that will be used For Reminding The User"""
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=too-many-function-args

import datetime as dt



class Reminder:
    """Reminder Class used to Remind the User of when an Event is Prior to it occurring"""

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
        today = str(dt.datetime.today())
        week_before = str(event.getDay() - dt.timedelta(days=7))
        if today[0:10] == week_before:
            return True
        return False

    def dayBefore(self, event):
        """Checks if today is a day before event """
        today = str(dt.datetime.today())
        DayBefore = str(vars(event)['day'] - dt.timedelta(days=1))
        if today[0:10] == DayBefore:
            return True
        return False

    def hourBefore(self, event):
        """Check if Today is an hour before event"""

        today = str(dt.datetime.today() + dt.timedelta(hours = 1))
        event_day = str(vars(event)['day'])
        now = dt.datetime.now()
        current_time = str(now.strftime("%H:%M"))

        event_time = vars(event)['start_time']
        print(f"Event_time: {event_time} || Event Day: {event_day}")
        print(f"Current_Time: {current_time} || Current Day: {today[0:10]}")
        if (event_day == today) and (event_time == current_time):
            return True
        return False

    def upcomingEvent(self, event):
        """Checks if event is upcoming"""
        #print(vars(event))

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
            if value:
                string += "ON"
            else:
                string += "OFF"
            string += "\n"
            i += 1
        return string
