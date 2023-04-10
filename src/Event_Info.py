# pylint: disable=invalid-name
# pylint: disable=line-too-long
"""Class for holding event information"""


class Event:
    """Saves event date, time, title, and any notes"""
    def __init__(self, day, start_time, end_time, name, notes):
        self.day = day
        self.start_time = start_time
        self.end_time = end_time
        self.name = name
        self.notes = notes

    def getName(self):
        """returns event title"""
        return self.name

    def getNotes(self):
        """returns event notes"""
        return self.notes

    def getStartTime(self):
        """returns event start time"""
        return self.start_time

    def getEndTime(self):
        """returns event end time"""
        return self.end_time

    def getDay(self):
        """returns event day"""
        return self.day

    def setName(self, name):
        """changes event title"""
        self.name = name

    def setNotes(self, notes):
        """changes event notes"""
        self.notes = notes

    def setStartTime(self, start_time):
        """changes event start time"""
        self.start_time = start_time

    def setEndTime(self, end_time):
        """changes event end time"""
        self.end_time = end_time

    def setDay(self, day):
        """changes event day"""
        self.day = day
