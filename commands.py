#!/usr/bin/python3
# commands.py
# diphia@2020
# This script is used to store the user commands

import os
from datetime import date,datetime,timedelta
from raw_process import reorganize
from show_tasks import show_raw,show_todo,show_done,show_cancelled,show_repeat
from utilities import select_list,retrieval_task_by_id,call_vim_single_line,remove_line_from_file,add_line_to_file
from repeat_generator import repeat_generator

CONTEXT_LOC = os.environ['HOME']+'/.vigtd_context/'
raw_inbox = CONTEXT_LOC + 'raw_inbox'
done_list = CONTEXT_LOC + 'done_list.csv'
todo_list = CONTEXT_LOC + 'todo_list.csv'
cancelled_list = CONTEXT_LOC + 'cancelled.csv'
generator_config = CONTEXT_LOC + 'repeat_tasks.csv'

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
        elif(type == 'done'):
            print(show_done(20))
            break
        elif(type == 'cancel' or type == 'cancelled'):
            print(show_cancelled(5))
            break
        elif(type == 'repeat'):
            print(show_repeat())
            break
        else:
            print('Please speciffic [raw], [todo] or [done] to show.')
            break

def raw_process():
    reorganize()

def done(task_id):
    try:
        target_task = retrieval_task_by_id(task_id)
    except:
        message = 'Task Not Found'
    to_write = '\"{0}\",\"{1}\",\"{2}\",\"{3}\"\n'.format(target_task.get_name(),target_task.get_ddl(),datetime.today().strftime("%Y-%m-%d"),target_task.get_parent())
    add_line_to_file(done_list,to_write)
    remove_line_from_file(todo_list,target_task.get_temp_linum())
    message = 'Done : ' + target_task.get_name()
    return message

def repeatgen():
    repeat_generator()

def postpone(task_id,new_ddl_or_offset):
    target_task = retrieval_task_by_id(task_id)
    if(new_ddl_or_offset.strip()[0] == '+'):
        offset = int(new_ddl_or_offset.strip()[1:])
        current_ddl = target_task.get_ddl()
        current_ddl_obj = datetime.strptime(current_ddl,"%Y-%m-%d")
        offset_obj = timedelta(days = offset)
        new_ddl_obj = current_ddl_obj + offset_obj
        new_ddl = new_ddl_obj.strftime("%Y-%m-%d")
    else:
        new_ddl = new_ddl_or_offset
    '''
    sed_add = "sed -i \'$a" + '\"' + target_task.get_name() + '\",\"' + new_ddl + "\"\' " + todo_list 
    os.system(sed_add)
    '''
    content = '\"' + target_task.get_name() + '\",\"' + new_ddl + '\"\n'
    add_line_to_file(todo_list,content)
    '''
    sed_delete = "sed \'" + str(target_task.get_temp_linum()) + "d\' -i " + todo_list
    os.system(sed_delete)
    '''
    remove_line_from_file(todo_list,target_task.get_temp_linum)
    message = 'Postponed : ' + target_task.get_name()
    return message

def cancel(task_id):
    target_task = retrieval_task_by_id(task_id)
    comment = call_vim_single_line('Reason')
    target_linum = target_task.get_temp_linum()
    remove_line_from_file(todo_list,target_linum)
    content = '\"{0}\",\"{1}\",\"{2}\",\"{3}\",\"{4}\"'.format(target_task.get_name(),target_task.get_ddl(),datetime.today().strftime("%Y-%m-%d"),comment,target_task.get_parent())
    #content = '\"'+target_task.get_name() + '\",\"' + target_task.get_ddl() + '\",\"' + datetime.today().strftime("%Y-%m-%d") + '\",\"' + comment + '\"\n'
    add_line_to_file(cancelled_list,content)
    message = 'Cancelled : ' + target_task.get_name()
    return message

def repeat_edit():
    os.system('vim ' + generator_config)

def add_child():
    parent = call_vim_single_line('Name of parent')
    task_name = call_vim_single_line('Task name')
    task_ddl = call_vim_single_line('DDL')
    to_write = '\"{0}\",\"{1}\",\"{2}\"\n'.format(task_name,task_ddl,parent)
    add_line_to_file(todo_list,to_write)
