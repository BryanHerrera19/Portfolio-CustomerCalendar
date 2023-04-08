# pylint: disable=invalid-name
# pylint: disable=line-too-long
"""Class for holding event information"""


class Event:
    """Saves event date, time, title, and any notes"""
    def __init__(self, day, time, name, notes):
        self.day = day
        self.time = time
        self.name = name
        self.notes = notes

    def getName(self):
        """returns event title"""
        return self.name

    def getNotes(self):
        """returns event notes"""
        return self.notes

    def getTime(self):
        """returns event time"""
        return self.time

    def getDay(self, day):
        """returns event day"""
        self.day = day

    def setName(self, name):
        """changes event title"""
        self.name = name

    def setNotes(self, notes):
        """changes event notes"""
        self.notes = notes

    def setTime(self, time):
        """changes event time"""
        self.time = time

    def setDay(self, day):
        """changes event day"""
        self.day = day
