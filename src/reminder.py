"""File is Used To Store Functions that will be used For Reminding The User"""
# pylint: disable=invalid-name
# pylint: disable=line-too-long

import datetime as DT

class Reminder:
    """Reminder Class used to Remind the User of when a Event is Prior to it occuring"""
    def __init__(self):
        """Initializing what reminders are turned on"""
        self.week = False
        self.day = False
        self.hour = False
    def setWeek(self, TF):
        """changes week Reminder Boolean"""
        self.week = TF
    def setDay(self, TF):
        """Changes Day Reminder Boolean"""
        self.day = TF
    def setHour(self, TF):
        """Changes Hour Reminder Boolean"""
        self.hour = TF
    def checkWeek(self, lis):
        """Checks if today is a week before event """
        for event in lis:
            today = DT.datetime.today()
            week_before = event.getDay() - DT.timedelta(days = 7)
            if (today == week_before):
                return True
            return False
    def checkDay(self, lis):
        """Checks if today is a week before event """
        for event in lis:
            today = DT.datetime.today()
            week_before = event.getDay() - DT.timedelta(days = 1)
            if (today == week_before):
                return True
            return False


