"""Sort events"""

def sort_by_date(list):
    '''sorts function by date'''
    def my_func(e):
        '''allows sorting function to sort by date'''
        return e.getDay()
    list.sort(key=my_func)
    return list
