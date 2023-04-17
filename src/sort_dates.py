"""Sort events"""

from datetime import *
from Event_Info import *

def sort_by_date(list):
    '''sorts function by date'''
    def my_func(list):
        '''allows sorting function to sort by date'''
        return list.getDay()
    
    list.sort(key=my_func)
    return list