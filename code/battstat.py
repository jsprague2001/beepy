#!/usr/bin/python
import os

batt_percent_file = '/sys/firmware/beepy/battery_percent'

# Get battery percentage
with open(batt_percent_file) as f:
    batt_percent = f.readline()

batt_percent_num = int(batt_percent)

# Define the cow mode
def switch(batt_percent_num):
    if 31 <= batt_percent_num < 100:
        return '-p'
    if 21 <= batt_percent_num <= 30:
        return '-s'
    if 11 <= batt_percent_num <= 20:
        return '-t'
    if 0 <= batt_percent_num <= 10:
        return '-d'

cmd = 'cowsay ' + switch(batt_percent_num) + ' Battery ' + batt_percent + '%'
# print(cmd)
returned_value = os.system(cmd)
