# pylint: disable=invalid-name
# pylint: disable=line-too-long
"""Unit Tests"""

import unittest
from datetime import date

from Event_Info import Event as eventInfo


class Test(unittest.TestCase):
    def test_Save_A_New_Event_Should_Return_True(self):
        event_list = [eventInfo(date.today(), "1:00PM", "2:00PM", "Class", "Online", "ARTS")]
        self.assertEqual(f"{event_list[0].getName()}", f"Class")


if __name__ == '__main__':
    unittest.main()
