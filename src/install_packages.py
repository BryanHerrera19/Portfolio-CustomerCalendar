'''File that downloads the necessary libraries'''
import sys
import subprocess

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tk'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tkcalendar'])
