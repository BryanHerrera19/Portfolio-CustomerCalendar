# pylint: disable=invalid-name
# pylint: disable=line-too-long
"""Unit Tests"""

import unittest
from datetime import date

from Event_Info import Event as eventInfo


class Test(unittest.TestCase):
    """Test Cases for Checking if Calendar Successfully saves Events"""
    def test_Save_A_New_Event_Should_Return_True(self):
        """Test Case should return True"""
        event_list = [eventInfo(date.today(), "1:00PM", "2:00PM", "Class", "Online", "ARTS")]
        self.assertEqual(f"{event_list[0].getName()}", "Class")


if __name__ == '__main__':
    unittest.main()
