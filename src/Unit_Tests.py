# pylint: disable=invalid-name
# pylint: disable=line-too-long
"""Unit Tests"""

import unittest
from datetime import date

from Event_Info import Event as eventInfo


class Test(unittest.TestCase):
    """Test Cases for Calendar"""
    # Test Cases for Checking if Calendar Successfully saves Events"""
    def test_Save_A_New_Event_Should_Return_True(self):
        """Test Case should return True"""
        event_list = [eventInfo(date.today(), "1:00PM", "2:00PM", "Class", "Online", "ARTS")]
        self.assertEqual(f"{event_list[0].getName()}", "Class")

    # Test Cases to Check if Timer Input Checking is working Properly"""
    def test_Timer_with_Letter_Input(self):
        """Test Case Should Run Properly"""
        hourString, minuteString, secondString = "1","45", "A0" #Inputted as 1:45:A0
        with self.assertRaises(ValueError):
            t = int(hourString)*3600 + int(minuteString)*60 + int(secondString)
            print(t)
    def test_Timer_with_Missing_Input(self):
        """Test Case Should Run Properly"""
        hourString, minuteString, secondString = "","45", "23" #Inputted as :45:23
        with self.assertRaises(ValueError):
            t = int(hourString)*3600 + int(minuteString)*60 + int(secondString)
            print(t)
    def test_Timer_with_Symbol_Input(self):
        """Test Case Should Run Properly"""
        hourString, minuteString, secondString = "1","%35", "23" #Inputted as 1:%35:23
        with self.assertRaises(ValueError):
            t = int(hourString)*3600 + int(minuteString)*60 + int(secondString)
            print(t)


if __name__ == '__main__':
    unittest.main()
