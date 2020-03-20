#!/usr/bin/python3
# commands.py
# diphia@2020
# This script is used to store the user commands

import os
from datetime import date
from task_object import task

CONTEXT_LOC = os.environ['HOME']+'/.vigtd_context/'

raw_inbox = CONTEXT_LOC + 'raw_inbox'
todo_list = CONTEXT_LOC + 'todo_list.csv'
done_list = CONTEXT_LOC + 'done_list.csv'

def add():  # add new raw contents
    temp_file_path = '/tmp/vigtd_commands_add_buffer'
    with open(temp_file_path,'w') as f:
        f.truncate()
    os.system('vim ' + temp_file_path)
    shell_command = 'cat ' + temp_file_path + ' >> ' + raw_inbox
    os.system(shell_command)

def show_raw():
    with open(raw_inbox,'r') as f:
        counter = 1
        content = ''
        for line in f:
            content = content + str(counter) + '.'
            content += line
            counter += 1
    return content

def show_todo():
    task_list_today = []
    task_list_tomorrow = []
    task_list_this_week = []
    task_list_this_month = []
    task_list_long = []
    content = []
    with open(todo_list,'r') as f:
        for line in f:
            task_name = line.split(',')[0].strip()[1:-1]
            task_ddl = line.split(',')[1].strip()[1:-1]
            temp_task = task(task_name,'',task_ddl)
            if(temp_task.get_ddl() == 'long'):
                task_list_long.append(temp_task)
                break
            if(temp_task.get_offset_day() == 0):
                task_list_today.append(temp_task)
            elif(temp_task.get_offset_day() == 1):
                task_list_tomorrow.append(temp_task)
            elif(temp_task.get_offset_day() < 7):
                task_list_this_week.append(temp_task)
            elif(temp_task.get_offset_day() < 30):
                task_list_this_month.append(temp_task)
            else:
                task_list_long.append(temp_task)
    return content

def show(type): # show raw_inbox, todo_list or done_list
    while(True):
        if(type == 'raw'):
            print(show_raw(),end = '')
            break
        elif(type == 'todo'):
            print(show_todo())
            break
        #elif(type == 'done'):
            #print(show_done())
            #break
        else:
            print('Please speciffic [raw], [todo] or [done] to show.')

if __name__=="__main__":
    #add()
    show('todo')
    
