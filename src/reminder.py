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
        extra = "0"
        # Day
        today = str(dt.datetime.today() + dt.timedelta(days = 7)).strip()
        week_before = str(event.getDay()).strip()
        # Time
        now = dt.datetime.now()
        current_time = str(now.strftime("%I:%M")).strip()
        event_time = str(vars(event)['start_time']).strip()
        if len(event_time) == 4:
            event_time = extra + event_time
        print(f"Week|| Event_time: {event_time} || Event Day: {week_before}")
        print(f"Week|| Current_Time: {current_time} || Current Day: {today[0:10]}")
        if (today[0:10] == week_before) and (current_time == event_time):
            return True
        return False

    def dayBefore(self, event):
        """Checks if today is a day before event """
        extra = "0"
        # Day
        today = str(dt.datetime.today() + dt.timedelta(days = 1)).strip()
        DayBefore = str(vars(event)['day']).strip()
        # Time
        now = dt.datetime.now()
        current_time = str(now.strftime("%I:%M")).strip()
        event_time = str(vars(event)['start_time']).strip()
        if len(event_time) == 4:
            event_time = extra + event_time
        print(f"Day|| Event_time: {event_time} || Event Day: {DayBefore}")
        print(f"Day|| Current_Time: {current_time} || Current Day: {today[0:10]}")
        if today[0:10] == DayBefore and (current_time == event_time):
            return True
        return False

    def hourBefore(self, event):
        """Check if Today is an hour before event"""
        #Extra digit
        extra = "0"
        # Day
        today = str(dt.datetime.today() + dt.timedelta(hours = 1)).strip()
        event_day = str(vars(event)['day']).strip()
        # Time
        now = dt.datetime.now()
        current_time = str(now.strftime("%I:%M")).strip()
        event_time = vars(event)['start_time'].strip()
        if len(event_time) == 4:
            event_time = extra + event_time
        print(f"HOUR|| Event_time: {event_time} || Event Day: {event_day}")
        print(f"HOUR|| Current_Time: {current_time} || Current Day: {today[0:10]}")
        if (event_day == today[0:10]) and (event_time == current_time):
            return True
        return False

    def upcomingEvent(self, event):
        """Checks if event is upcoming"""
        #print(vars(event))
        if self.week:
            if self.weekBefore(event):
                return True
        if self.day:
            if self.dayBefore(event):
                return True
        if self.hour:
            if self.hourBefore(event):
                return True
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
