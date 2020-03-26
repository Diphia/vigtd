#!/usr/bin/python3
# raw_read.py
# diphia@2020
# This script is used to process the raw_inbox file and reorganize tasks to deeper files

import os
from datetime import date
from task_object import task
from utilities import call_vim_single_line

CONTEXT_LOC = os.environ['HOME']+'/.vigtd_context/'

raw_inbox = CONTEXT_LOC + 'raw_inbox'
todo_list = CONTEXT_LOC + 'todo_list.csv'
done_list = CONTEXT_LOC + 'done_list.csv'

def process_line(line):
    task_name = line.strip()
    print('Task: ',end = '')
    print(task_name)
    print('Is this easy to complete (<2min) ? If so, complete it now and input [done] ; or input [no]: ',end = '')
    while(True):
        selected = input()
        if(selected == 'done'):
            task_tag = 'done'
            break
        elif(selected == 'no'):
            task_tag = 'todo'
            break
        else:
            print('input error, please input [done] or [no]: ',end = '')
    if(task_tag == 'todo'):
        task_ddl = call_vim_single_line('Plan to complete before')
    else:
        task_ddl = ''
    return task_name,task_tag,task_ddl

def raw_inbox_read():
    task_list_todo = []
    task_list_done = []
    with open(raw_inbox,'r') as f:
        for line in f:
            task_name,task_tag,task_ddl = process_line(line)
            temp_task = task(task_name,task_tag,task_ddl)
            if(temp_task.get_tag() == 'todo'):
                task_list_todo.append(temp_task)
            elif(temp_task.get_tag() == 'done'):
                task_list_done.append(temp_task)
    return task_list_done,task_list_todo

def write_to_todo(task_list_todo):
    try:
        f = open(todo_list,'a')
        for task in task_list_todo:
            to_write = '\"' + task.get_name() + '\",\"' + task.get_ddl() + '\"\n'
            f.write(to_write)
    finally:
        if(f):
            f.close()

def write_to_done(task_list_done):
    try:
        f = open(done_list,'a')
        for task in task_list_done:
            to_write = '\"' + task.get_name() + '\",\"' + date.today().strftime("%Y-%m-%d") + '",\"' + date.today().strftime("%Y-%m-%d") + '\"\n'
            f.write(to_write)
    finally:
        if(f):
            f.close()

def clear_file(file):
    command = 'cat ' + file + ' >> ' + file + '.bak'
    os.system(command)
    with open(file,'w') as f:
        f.truncate()

def reorganize():
    task_list_done,task_list_todo = raw_inbox_read()
    write_to_todo(task_list_todo)
    write_to_done(task_list_done)
    clear_file(raw_inbox)
