#!/usr/bin/python3
# show_tasks.py
# diphia@2020
# This script is used to show stored tasks

import os
import re
from datetime import date
from task_object import task
from utilities import read_todo,read_done,parse_csv

CONTEXT_LOC = os.environ['HOME']+'/.vigtd_context/'

raw_inbox = CONTEXT_LOC + 'raw_inbox'
todo_list = CONTEXT_LOC + 'todo_list.csv'
done_list = CONTEXT_LOC + 'done_list.csv'
cancelled_list = CONTEXT_LOC + 'cancelled.csv'
repeat_list = CONTEXT_LOC + 'repeat_tasks.csv'

def show_raw():
    with open(raw_inbox,'r') as f:
        counter = 1
        content = ''
        for line in f:
            content = content + str(counter) + '.'
            content += line
            counter += 1
    return content

def add_to_content(task_list,content,title):
    if(len(task_list) == 0):
        return content
    content = content + title + ':\n'
    #content += '======================================\n'
    counter = 1
    for task in task_list:
        #if(task_list == task_list_today or task_list == task_list_tomorrow):
        if(title == '(a) Today' or title == '(b) Tomorrow'):
            content = content + '    (' + str(counter) + ') ' + task.get_name() + '\n'
        else:
            content = content + '    (' + str(counter) + ') ' + task.get_name() + ' , DDL = ' + task.get_ddl() + '\n'
        counter += 1
    #content += '\n'
    return content

def show_todo():
    task_list_detained,task_list_today,task_list_tomorrow,task_list_this_week,task_list_this_month,task_list_long = read_todo()
    content = ''
    content = add_to_content(task_list_long,content,'(e) Long-term')
    content = add_to_content(task_list_this_month,content,'(d) This Month')
    content = add_to_content(task_list_this_week,content,'(c) This Week')
    content = add_to_content(task_list_tomorrow,content,'(b) Tomorrow')
    content = add_to_content(task_list_today,content,'(a) Today')
    content = add_to_content(task_list_detained,content,'(z) Detained')
    return content

def show_done(line_amount):
    line_amount = 20
    task_list = read_done()
    content = ''
    for t in task_list:
        content = content + t.get_name() + ', Plan@' + t.get_ddl() + ', Done@' + t.get_done_date() + '\n'
    return content


def show_cancelled(amount):
    content = ''
    fields_list = parse_csv(cancelled_list)
    for i in reversed(range(len(fields_list))):
        count = len(fields_list) - i
        if(count == amount):
            break
        content += '------------------------------\n'
        content += 'Task: {0}\n'.format(fields_list[i][0])
        content += 'Planned DDL: {0}\n'.format(fields_list[i][1])
        content += 'Cancelled Date : {0}\n'.format(fields_list[i][2])
        content += 'Comment : {0}\n'.format(fields_list[i][3])
    return content

def show_repeat():
    content = ''
    fields_list = parse_csv(repeat_list)
    for line in fields_list:
        content += '------------------------------\n'
        content += 'Task: {0}\n'.format(line[0])
        content += 'Peroid: {0}\n'.format(line[1])
    return content
