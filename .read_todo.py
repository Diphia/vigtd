#!/usr/bin/python3
# todo_read.py
# diphia@2020
# This script is used to read the todo_list file and return list data

import os
from task_object import task

CONTEXT_LOC = os.environ['HOME']+'/.vigtd_context/'

raw_inbox = CONTEXT_LOC + 'raw_inbox'
todo_list = CONTEXT_LOC + 'todo_list.csv'

def read_todo():
    task_list_detained = []
    task_list_today = []
    task_list_tomorrow = []
    task_list_this_week = []
    task_list_this_month = []
    task_list_long = []
    with open(todo_list,'r') as f:
        linum = 1
        for line in f:
            task_name = line.split(',')[0].strip()[1:-1]
            task_ddl = line.split(',')[1].strip()[1:-1]
            temp_task = task(task_name,'',task_ddl)
            temp_task.set_temp_linum(linum)
            if(temp_task.get_ddl() == 'long'):
                temp_task.set_temp_id('e'+str(len(task_list_long)+1))
                task_list_long.append(temp_task)
                break
            elif(temp_task.get_offset_day() < 0):
                temp_task.set_temp_id('z'+str(len(task_list_detained)+1))
                task_list_detained.append(temp_task)
            elif(temp_task.get_offset_day() == 0):
                temp_task.set_temp_id('a'+str(len(task_list_today)+1))
                task_list_today.append(temp_task)
            elif(temp_task.get_offset_day() == 1):
                temp_task.set_temp_id('b'+str(len(task_list_tomorrow)+1))
                task_list_tomorrow.append(temp_task)
            elif(temp_task.get_offset_day() < 7):
                temp_task.set_temp_id('c'+str(len(task_list_this_week)+1))
                task_list_this_week.append(temp_task)
            elif(temp_task.get_offset_day() < 30):
                temp_task.set_temp_id('d'+str(len(task_list_this_month)+1))
                task_list_this_month.append(temp_task)
            else:
                temp_task.set_temp_id('e'+str(len(task_list_long)+1))
                task_list_long.append(temp_task)
            linum += 1
    return task_list_detained,task_list_today,task_list_tomorrow,task_list_this_week,task_list_this_month,task_list_long
