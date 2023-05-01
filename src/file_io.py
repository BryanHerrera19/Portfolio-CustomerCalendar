# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import
'''Handles file io for our calendar'''

import json
from datetime import *

from Event_Info import Event as eventInfo


def event_list_to_dictionary(event_list):
    '''Function to save events to a list of dictionaries for easy file io'''
    saved_event_list = []
    for event in event_list:
        print(vars(event))
        saved_event_list.append(vars(event))
    return saved_event_list

def dictionary_list_to_file(saved_events):
    '''Saves dictionary to file'''
    with open('./src/eventlist.txt', 'w', encoding = 'utf-8') as file_write:
        for event in saved_events:
            file_write.write(json.dumps(event, indent=4, sort_keys=True, default=str))
    return True

def file_to_event_list():
    '''Reads dictionary from file'''
    loaded_dict_list = []
    with open('./src/eventlist.txt', 'r', encoding='utf-8') as file_read:
        data = file_read.read()
        js_data = json.loads(data)
        loaded_dict_list.append(js_data)
    return dictionary_to_event_list(loaded_dict_list)

def dictionary_to_event_list(loaded_dict_list):
    '''Changes ditionary to event_info class'''
    loaded_event_list = []
    for event in loaded_dict_list:
        loaded_event_list.append(eventInfo(datetime.strptime(event.get("day"), '%Y-%m-%d').date(), event.get("start_time"),
                                            event.get("start_time_day"), event.get("end_time"),
                                            event.get("name"), event.get("notes"),
                                            event.get("category")))
    print(loaded_event_list)
    return loaded_event_list
