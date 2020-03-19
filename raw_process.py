#!/usr/bin/python3
# raw_process.py
# diphia@2020
# This script is used to process the raw_inbox 

import os

CONTEXT_LOC = os.environ['HOME']+'/.vigtd_context/'

raw_inbox = CONTEXT_LOC + 'raw_inbox'
todo_list = CONTEXT_LOC + 'todo_list.csv'

def call_vim_single_line(prompt):
    with open('/tmp/raw_process_call_vim_single_line','w') as f:
        f.truncate()
        f.write(prompt+' : ')
    os.system('vim /tmp/raw_process_call_vim_single_line')
    with open('/tmp/raw_process_call_vim_single_line','r') as f:
        line = f.read().split('\n')[0]
        content = line.split(':')[1].strip()
    return content
    
def process_line(line):
    print('Task: ',end='')
    print(line)
    print('Is this easy to complete ? If so, complete it now and input [done] ; or input [no]: ',end = '')
    while(True):
        selected = input()
        if(selected == 'done'):
            processed_line = 'DONE' + ',' + line
            break
        elif(selected == 'no'):
            date = call_vim_single_line('Plan to complete before')
            processed_line = 'TODO|' + date + ',' + line
            break
        else:
            print('input error, please input [done] or [no]:')
    return processed_line

def reorgnize():
    processed_lines = []
    with open(raw_inbox,'r') as f:
        lines = f.read().split('\n')[:-1]
        for l in lines:
            processed_lines.append(process_line(l))
    print(processed_lines)
    with open(raw_inbox,'w') as f:
        for l in processed_lines:
            f.write(l)
            f.write('\n')

if __name__=="__main__":
    reorgnize()
