# pylint: disable=missing-module-docstring
# pylint:disable=duplicate-code
#from datetime import date

from datetime import datetime
import time_help_functions as of



def get_time():
    """Grabs the current time in readable format"""
    now = datetime.now()
    hour = now.strftime("%H")
    minute = now.strftime("%M")
    second = now.strftime("%S")
    ante_post = now.strftime("%p")
    hour = of.convert_hour(hour)
    current_time = f"{hour}:{minute}:{second} {ante_post}"


    return current_time
