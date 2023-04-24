'''Handles file io for our calendar'''

import json

def event_list_to_dictionary(event_list):
    '''Function to save events to a list of dictionaries for easy file io'''
    saved_event_list = []
    for event in event_list:
        print(vars(event))
        saved_event_list.append(vars(event))
    return saved_event_list

def dictionary_list_to_file(saved_events):
    '''Saves dictionary to file'''
    with open('./src/eventlist.txt', 'w') as file_write:
        for event in saved_events:
            file_write.write(json.dumps(event, indent=4, sort_keys=True, default=str))
    return True

def file_to_dictionary_list():
    '''Reads dictionary from file'''
    return True
