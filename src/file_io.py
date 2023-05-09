# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import
# pylint: disable=consider-using-f-string
"""Handles file io for our calendar"""

import json
import os
from datetime import *

from Event_Info import Event as eventInfo


def event_list_to_dictionary(event_list):
    """Function to save events to a list of dictionaries for easy file io"""
    saved_event_list = []
    for event in event_list:
        print(vars(event))
        saved_event_list.append(vars(event))
    return saved_event_list

def dictionary_list_to_file(saved_events):
    """Saves dictionary to file"""
    with open('./eventlist.txt', 'w', encoding='utf-8') as file_write:
        file_write.write(json.dumps(saved_events, indent=4, sort_keys=True, default=str))
    return True

def file_to_event_list():
    """Reads dictionary from file"""
    loaded_dict_list = []
    if os.path.getsize('./eventlist.txt') == 0:
        loaded_dict_list = []
    else:
        with open('eventlist.txt', 'r', encoding='utf-8') as file_read:
            data = file_read.read()
            js_data = json.loads(data)
            loaded_dict_list.append(js_data)
    return dictionary_to_event_list(loaded_dict_list)

def dictionary_to_event_list(loaded_dict_list):
    """Changes dictionary to event_info class"""
    loaded_event_list = []
    for tempdict in loaded_dict_list:
        for event in tempdict:
            loaded_event_list.append(eventInfo(datetime.strptime(event.get("day"),
                                                                '%Y-%m-%d').date(),
                                                                event.get("start_time"),
                                                                event.get("start_time_day"),
                                                                event.get("end_time"),
                                                                event.get("name"),
                                                                event.get("notes"),
                                                                event.get("category")))
    return loaded_event_list

def category_list_to_file(category_list):
    """Saves list of categories to file"""
    with open('./categories.txt', 'w', encoding='utf-8') as file_write:
        for cat in category_list:
            file_write.write("%s\n" % cat)

def file_to_category_list():
    """Loads list of categories from file to a list"""
    categories = []
    if os.path.getsize('./categories.txt') == 0:
        categories = []
    else:
        with open('./categories.txt', 'r', encoding='utf-8') as file_read:
            for line in file_read:
                read_line = line[:-1]
                categories.append(read_line)
    return categories

def category_colors_to_file(category_colors):
    """Saves list of category colors to file"""
    with open('./category_colors.txt', 'w', encoding='utf-8') as file_write:
        for cat_col in category_colors:
            file_write.write("%s\n" % cat_col)

def file_to_category_colors():
    """Loads list of category colors from file to a list"""
    category_colors = []
    if os.path.getsize('./category_colors.txt') == 0:
        category_colors = []
    else:
        with open('./category_colors.txt', 'r', encoding='utf-8') as file_read:
            for line in file_read:
                read_line = line[:-1]
                category_colors.append(read_line)
    return category_colors
