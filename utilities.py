#!/usr/bin/python3
# utilities.py
# diphia@2020
# This script is used to include some useful functions for vigtd

import os
import re
from task_object import task

CONTEXT_LOC = os.environ['HOME']+'/.vigtd_context/'
raw_inbox = CONTEXT_LOC + 'raw_inbox'
todo_list = CONTEXT_LOC + 'todo_list.csv'
done_list = CONTEXT_LOC + 'done_list.csv'

def parse_csv(target_file): # read a file and get the fields of a csv file, return as a list of lists
    fields_list = []
    with open(target_file,'r') as f:
        for line in f:
            line = line.strip()
            fields_list.append(re.split('(?<=\"),(?=\")',line))
        for i in range(len(fields_list)):
            for j in range(len(fields_list[i])):
                fields_list[i][j] = fields_list[i][j][1:-1]
    return fields_list

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
            try:
                task_parent = line.split(',')[2].strip()[1:-1]
            except:
                task_parent = ''
            temp_task = task(task_name,'',task_ddl)
            temp_task.set_temp_linum(linum)
            temp_task.set_parent(task_parent)
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

def retrieval_task_by_id(task_id):
    task_id = task_id.strip()
    task_type = task_id[0]
    target_list = select_list(task_type)
    for t in target_list:
        if(t.get_temp_id() == task_id):
            target_task = t
            break
    return target_task

def call_vim_single_line(prompt):
    with open('/tmp/raw_process_call_vim_single_line','w') as f:
        f.truncate()
        f.write(prompt+' : ')
    os.system('vim /tmp/raw_process_call_vim_single_line')
    with open('/tmp/raw_process_call_vim_single_line','r') as f:
        line = f.read().split('\n')[0]
        content = line.split(':')[1].strip()
    return content

def remove_line_from_file(target_file,linum):
    with open(target_file,'r') as f:
        counter = 1
        content = ''
        for line in f:
            if(counter == linum):
                l = ''
            else:
                l = line
            content += l
            counter += 1
    with open(target_file,'w') as f:
        f.truncate()
        f.write(content)

def add_line_to_file(target_file,content):
    with open(target_file,'a') as f:
        f.write(content)

