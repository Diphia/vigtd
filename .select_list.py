#!/usr/bin/python3
# select_list.py
# diphia@2020
# This script is used to select a list by input task_type

from utilities import read_todo

def select_list(task_type):
    task_list_detained,task_list_today,task_list_tomorrow,task_list_this_week,task_list_this_month,task_list_long = read_todo()
    if(task_type == 'a'):
        target_list = task_list_today
    elif(task_type == 'b'):
        target_list = task_list_tomorrow
    elif(task_type == 'c'):
        target_list = task_list_this_week
    elif(task_type == 'd'):
        target_list = task_list_this_month
    elif(task_type == 'e'):
        target_list = task_list_long
    elif(task_type == 'z'):
        target_list = task_list_detained
    else:
        target_list = []
    return target_list
    
    
    
