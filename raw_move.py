#!/usr/bin/python3
# raw_move.py
# diphia@2020
# This script is used to move the data in raw_inbox to todo_list(save as csv) and done_list

import os

CONTEXT_LOC = os.environ['HOME']+'/.vigtd_context/'

raw_inbox = CONTEXT_LOC + 'raw_inbox'
todo_list = CONTEXT_LOC + 'todo_list.csv'

class task(object):
    def __init__(self, name, tag, ddl):
        self.name = name
        self.tag = tag
        self.ddl = ddl
    def get_name(self):
        return self.name
    def get_tag(self):
        return self.tag
    def get_ddl(self):
        return self.ddl

def raw_inbox_read():
    task_list_todo = []
    task_list_done = []
    with open(raw_inbox,'r') as f:
        for line in f:
            property_fields = line.split(',')[0].split('|')
            task_name = line.split(',')[1].strip()
            try:
                task_tag = property_fields[0]
                if(task_tag == 'TODO'):
                    task_ddl = property_fields[1]
                else:
                    task_ddl = ''
            except:
                pass
            temp_task = task(task_name,task_tag,task_ddl)
            if(task_tag == 'TODO'):
                task_list_todo.append(temp_task)
            elif(task_tag == 'DONE'):
                task_list_done.append(temp_task)
    return task_list_todo,task_list_done


if __name__=="__main__":
    task_list_todo,task_list_done = raw_inbox_read()
    

