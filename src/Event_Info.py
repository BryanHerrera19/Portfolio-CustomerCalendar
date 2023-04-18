# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=too-many-arguments
"""Class for holding event information"""


class Event:
    """Saves event date, time, title, and any notes"""

    def __init__(self, day, start_time, start_time_day, end_time, name, notes, category):
        self.day = day
        self.start_time = start_time
        self.start_time_day = start_time_day
        self.end_time = end_time
        self.name = name
        self.notes = notes
        self.category = category

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

    def getStartTimeDay(self):
        """returns event start time AM or PM"""
        return self.start_time_day

    def getDay(self):
        """returns event day"""
        return self.day

    def getCategory(self):
        """returns event category"""
        return self.category

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

    def setStartTimeDay(self, start_time_day):
        """changes event start time AM or PM"""
        self.start_time_day = start_time_day

    def setDay(self, day):
        """changes event day"""
        self.day = day

    def setCategory(self, category):
        """changes event category"""
        self.category = category

    def sortStartTime(self, event_list):
        """Split event_list into category lists to sort them using their start time within each category
         that returns a single sorted list"""

        events = event_list
        category_event_list = []
        sorted_event_list = []
        if len(events) <= 1:
            return events
        for event, next_event in enumerate(events[:-1]):
            if events[event].getCategory() != next_event.getCategory():
                category_event_list.append(events[event])
                sorted_event_list.extend(self.separateDayAndNightEvents(self, category_event_list))
                category_event_list.clear()
            category_event_list.append(events[event])
        lastIndex = len(events) - 1
        category_event_list.append(events[lastIndex])
        sorted_event_list.extend(self.separateDayAndNightEvents(self, category_event_list))
        return sorted_event_list

    def separateDayAndNightEvents(self, category_list):
        """Split category lists into AM and PM lists and then combine it into one sorted list"""

        day_event_list = []
        night_event_list = []
        sorted_category_events = []

        for event in category_list:
            if event.getStartTimeDay() == "AM":
                day_event_list.append(event)
                day_event_list.sort(key=lambda current_event: current_event.getStartTime())
            else:
                night_event_list.append(event)
                night_event_list.sort(key=lambda current_event: current_event.getStartTime())
        sorted_category_events.extend(day_event_list)
        sorted_category_events.extend(night_event_list)
        return sorted_category_events
