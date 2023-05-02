"""Sort events"""

def sort_by_date(event_list):
    """sorts function by date"""
    def my_func(temp_list):
        """allows sorting function to sort by date"""
        return temp_list.getDay()
    return event_list.sort(key=my_func)

def sort_by_category(event_list):
    """sorts function by category"""
    def my_func(temp_list):
        """allows sorting function to sort by category"""
        return temp_list.getCategory()
    return event_list.sort(key=my_func)
    