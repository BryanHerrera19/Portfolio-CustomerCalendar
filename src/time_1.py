# pylint: disable=missing-module-docstring
#from datetime import date

from datetime import datetime

import time_help_functions as of


now = datetime.now()
hour = now.strftime("%H")
minute = now.strftime("%M")
second = now.strftime("%S")
ante_post = now.strftime("%p")
hour = of.convert_hour(hour)
current_time = f"{hour}:{minute}:{second} {ante_post}"
