#!/usr/bin/python3
# read_done.py
# diphia@2020
# This script is used to read the done_list file and return list data

import os
from task_object import task

CONTEXT_LOC = os.environ['HOME']+'/.vigtd_context/'

done_list = CONTEXT_LOC + 'done_list.csv'

def read_done():
    task_list_done = []
    with open(done_list,'r') as f:
        for line in f:
            task_name = line.split(',')[0].strip()[1:-1]
            task_ddl = line.split(',')[1].strip()[1:-1]
            task_done_date = line.split(',')[2].strip()[1:-1]
            temp_task = task(task_name,'',task_ddl)
            temp_task.set_done_date(task_done_date)
            task_list_done.append(temp_task)
    return task_list_done
