# Testing

## Testing Plan and Strategies 

Our program required a way of keep track of the current date and time as well as event date and time. This is to compare the current day to a event in order to properly give the user reminders. Moreover, we also needed a way for the user to have a functioning study timer. To test this, we needed a way to make sure the inputs from users on the timer is valid. If the user input is invalid, our program should allow our user to re-enter a new value while letting them know that the current input is invalid. 

## Test Cases

### Test Cases for Reminders

Two main types of functions for reminders: one responsible for checking if the time is equal, while the other checking if the dates are equal. Results from the following tests show that that both a date time variable type and date has to be converted into a string from the datetime python library in order to properly compare them with other dates and times. Converting them into strings also allows us to manipulate them much easier. Parts of a date time had to be removed to focus on either just the date or just the time. 

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

### Test Cases for Timer

The timer can only take numerical inputs and all input boxes for the timer should be filled before it can run. Results from the follwing test cases indicate that we need a proper way of converting time into string and analyzing each parts of the timer for any non-numerical input. Moreover, all input boxes (there are three: hour, minute, second) must be filled and there must be a function that allows us to check in each of the input boxes.

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

