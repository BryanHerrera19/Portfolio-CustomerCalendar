"""Class for holding event information"""
# pylint: disable=invalid-name
# pylint: disable=line-too-long

import tkinter as tk
from datetime import date
from tkcalendar import Calendar
from tkcalendar import DateEntry

import time_help_functions as t1


class Event:
    def __init__(self, day, time, name, notes):
        self.day = day
        self.time = time
        self.name = name
        self.notes = notes

    def getName(self):
        return self.name

    def getNotes(self):
        return self.notes

    def getTime(self):
        return self.time

    def setName(self, name):
        self.name = name

    def setNotes(self, notes):
        self.notes = notes

    def setTime(self, time):
        self.time = time

    def setDay(self, day):
        self.day = day
