# pylint: disable=invalid-name
# pylint: disable=missing-class-docstring
# pylint: disable=global-statement
# pylint: disable=wildcard-import
# pylint: disable=wildcard-import
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
        # pylint: disable=too-many-function-args
        event_list = [eventInfo(eventInfo, date.today(), "1:00", "PM", "2:00PM", "Class 123", "Online", "ARTS")]
        self.assertEqual(f"{event_list[0].getName()}", "Class")

    # Test Cases to Check if Timer Input Checking is working Properly"""
    def test_Timer_with_Letter_Input(self):
        """Test Case Should Run Properly"""
        hourString, minuteString, secondString = "1", "45", "A0"  # Inputted as 1:45:A0
        with self.assertRaises(ValueError):
            t = int(hourString) * 3600 + int(minuteString) * 60 + int(secondString)
            print(t)

    def test_Timer_with_Missing_Input(self):
        """Test Case Should Run Properly"""
        hourString, minuteString, secondString = "", "45", "23"  # Inputted as :45:23
        with self.assertRaises(ValueError):
            t = int(hourString) * 3600 + int(minuteString) * 60 + int(secondString)
            print(t)

    def test_Timer_with_Symbol_Input(self):
        """Test Case Should Run Properly"""
        hourString, minuteString, secondString = "1", "%35", "23"  # Inputted as 1:%35:23
        with self.assertRaises(ValueError):
            t = int(hourString) * 3600 + int(minuteString) * 60 + int(secondString)
            print(t)

    def test_check_if_Times_match(self):
        """Test Case Should Return False"""
        current_time = "1:45:23"
        event_start_time = "1:45"
        self.assertEqual(current_time, event_start_time)

    def test_check_if_dates_match(self):
        """Test Case Should Return False"""
        current_day = "2023-04-08"
        event_date= "2023-5-07"
        self.assertEqual(current_day, event_date)

    def test_check_if_Times_match_1(self):
        """Test Case Should Return False"""
        current_time = "1:43"
        event_start_time = "1:45"
        self.assertEqual(current_time, event_start_time)

    def test_check_if_dates_match_1(self):
        """Test Case Should Return False"""
        current_day = "2023-04-08"
        event_date= "2023-05-07"
        self.assertEqual(current_day, event_date)

    def test_check_if_Times_match_2(self):
        """Test Case Should Return True"""
        current_time = "1:45"
        event_start_time = "1:45"
        self.assertEqual(current_time, event_start_time)

    def test_check_if_dates_match_2(self):
        """Test Case Should Return True"""
        current_day = "2023-05-08"
        event_date= "2023-05-08"
        self.assertEqual(current_day, event_date)

    def test_check_if_Times_match_3(self):
        """Test Case Should Return True"""
        current_time = "1:46"
        event_start_time = "1:46"
        self.assertEqual(current_time, event_start_time)

    def test_check_if_dates_match_3(self):
        """Test Case Should Return True"""
        current_day = "2023-08-08"
        event_date= "2023-08-08"
        self.assertEqual(current_day, event_date)




if __name__ == '__main__':
    unittest.main()
