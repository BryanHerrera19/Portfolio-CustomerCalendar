'''Handles file io for our calendar'''

def event_list_to_dictionary(eventlist):
    '''Function to save events to a list of dictionaries for easy file io'''
    saved_event_list = []
    for event in eventlist:
        saved_event_list.append(vars(event))
    return saved_event_list