#!/usr/bin/python3
# repeat_generator.py
# diphia@2020
# This script is used to generate the tasks that repeat a fixed cyclic peroid

import os
from task_object import repeat_task
from read_todo import read_todo
from read_done import read_done

CONTEXT_LOC = os.environ['HOME'] + '/.vigtd_context/'
generator_config = CONTEXT_LOC + 'repeat_tasks.csv'
todo_list = CONTEXT_LOC + 'todo_list.csv'

def is_exist_in_list(repeat_task,target_task_list):
    for t in target_task_list:
        if(t.get_name() == repeat_task.get_task_name() and t.get_ddl() == repeat_task.get_ddl()):
            return True
    return False

def list_writer(repeat_task,done_task_list,todo_task_list):
    if(not is_exist_in_list(repeat_task,done_task_list) and not is_exist_in_list(repeat_task,todo_task_list)):
        with open(todo_list,'a') as f:
            to_write = '\"' + repeat_task.get_task_name() + '\",\"' + repeat_task.get_ddl() + '\"\n'
            f.write(to_write)
    
def repeat_generator():
    task_list_detained,task_list_today,task_list_tomorrow,task_list_this_week,task_list_this_month,task_list_long = read_todo()
    todo_list = task_list_detained + task_list_today + task_list_tomorrow + task_list_this_week + task_list_this_month + task_list_long
    done_list = read_done()
    with open(generator_config,'r') as f:
        for line in f:
            task_name = line.split(',')[0].strip()[1:-1]
            task_peroid = line.split(',')[1].strip()[1:-1]
            temp_task = repeat_task(task_name,task_peroid)
            list_writer(temp_task,done_list,todo_list)

if __name__=="__main__":
    repeat_generator()
