#!/usr/bin/python3
# commands.py
# diphia@2020
# This script is used to store the user commands

import os
from datetime import date
from raw_process import reorganize
from show_tasks import show_raw,show_todo
from read_todo import read_todo
from select_list import select_list

CONTEXT_LOC = os.environ['HOME']+'/.vigtd_context/'
raw_inbox = CONTEXT_LOC + 'raw_inbox'
done_list = CONTEXT_LOC + 'done_list.csv'
todo_list = CONTEXT_LOC + 'todo_list.csv'

def add():  # add new raw contents
    temp_file_path = '/tmp/vigtd_commands_add_buffer'
    with open(temp_file_path,'w') as f:
        f.truncate()
    os.system('vim ' + temp_file_path)
    shell_command = 'cat ' + temp_file_path + ' >> ' + raw_inbox
    os.system(shell_command)

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
            break

def raw_process():
    reorganize()

def done(task_id):
    task_id = task_id.strip()
    task_type = task_id[0]
    target_list = select_list(task_type)
    if(target_list == []):
        message = 'Invalid Task Type'
        return message
    for t in target_list:
        if(t.get_temp_id() == task_id):
            target_task = t
            break
    try:
        target_task
    except NameError:
        message = 'Invalid Task Number'
        return message
    with open(done_list,'a') as f:
        to_write = '\"' + target_task.get_name() + '\",\"' + target_task.get_ddl() + '",\"' + date.today().strftime("%Y-%m-%d") + '\"\n'
        f.write(to_write)
    shell_command = "sed \'" + str(target_task.get_temp_linum()) + "d\' -i " + todo_list
    os.system(shell_command)
    message = 'Done : ' + target_task.get_name()
    return message

if __name__=="__main__":
    #add()
    #raw_process()
    show('todo')
    #print(done('c1'))

    
